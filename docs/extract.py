#!/usr/bin/env python3
"""Extract the result inventory of part_i/main.tex.

Reads the manuscript and its .aux and writes docs/results.json (consumed by the
interactive figures) and docs/results.md (the navigable inventory).  Nothing here is
hand-maintained: numbers come from the .aux, statements and provenance from the .tex,
and the dependency graph from the \\ref edges of each statement and its proof.

    python3 docs/extract.py            # from the repository root
    python3 docs/extract.py --check    # exit 1 if the committed output is stale
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEX, AUX = ROOT / "part_i" / "main.tex", ROOT / "part_i" / "main.aux"
OUT_JSON, OUT_MD = ROOT / "docs" / "results.json", ROOT / "docs" / "results.md"
OUT_JS = ROOT / "docs" / "results.js"

KINDS = {"theorem": "Theorem", "proposition": "Proposition", "lemma": "Lemma",
         "corollary": "Corollary", "hypothesis": "Hypothesis", "definition": "Definition",
         "remark": "Remark", "srcfact": "Source Fact", "assumption": "Assumption"}
# A8 is the GJS package; its item (vi) is U_GJS, the one non-literal import.
GJS_LABEL, UGJS_EQ = "A:gjs", "eq:UGJS"


def balanced(text, i, open_ch, close_ch):
    """Return (content, index after the closing delimiter) for text[i] == open_ch."""
    depth, j = 0, i
    while j < len(text):
        if text[j] == open_ch:
            depth += 1
        elif text[j] == close_ch:
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced delimiter at %d" % i)


def load_numbers():
    nums = {}
    if not AUX.exists():
        sys.exit("part_i/main.aux is missing: build the manuscript first "
                 "(cd part_i && pdflatex main.tex), then re-run.")
    for lab, num, page in re.findall(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}\{(\d+)\}", AUX.read_text()):
        nums[lab] = {"number": num, "page": int(page)}
    return nums


def load_macros(tex):
    """KaTeX macro map, read from the manuscript's own preamble."""
    macros = {}
    for name, body in re.findall(r"\\newcommand\{\\(\w+)\}\{([^\n]*?)\}\s*$", tex, re.M):
        macros["\\" + name] = body
    for name, nargs, body in re.findall(r"\\newcommand\{\\(\w+)\}\[(\d)\]\{(.*?)\}\s*$", tex, re.M):
        macros["\\" + name] = body
    for name, op in re.findall(r"\\DeclareMathOperator\{\\(\w+)\}\{([^}]*)\}", tex):
        macros["\\" + name] = r"\operatorname{%s}" % op
    return macros


def sections(tex):
    out = []
    for m in re.finditer(r"\\(sub)?section\*?\{", tex):
        title, after = balanced(tex, m.end() - 1, "{", "}")
        lab = re.match(r"\s*\\label\{([^}]*)\}", tex[after:])
        out.append({"pos": m.start(), "level": 2 if m.group(1) else 1,
                    "title": title, "label": lab.group(1) if lab else None})
    return out


def section_of(secs, pos):
    cur = None
    for s in secs:
        if s["pos"] > pos:
            break
        if s["level"] == 1:
            cur = s
    return cur


def refs_in(s):
    out = []
    for m in re.finditer(r"\\(?:eq)?ref\{([^}]*)\}", s):
        out.extend(x.strip() for x in m.group(1).split(","))
    return out


def extract():
    tex = TEX.read_text()
    nums, macros, secs = load_numbers(), load_macros(tex), sections(tex)
    results, pat = [], re.compile(r"\\begin\{(%s)\}" % "|".join(KINDS))
    for m in pat.finditer(tex):
        kind, i = m.group(1), m.end()
        title = None
        if i < len(tex) and tex[i] == "[":
            title, i = balanced(tex, i, "[", "]")
        lab = re.match(r"\s*\\label\{([^}]*)\}", tex[i:])
        if not lab:
            continue                      # unnumbered (srcfactstar) or inline use
        label = lab.group(1)
        end = tex.index(r"\end{%s}" % kind, i)
        body = tex[i + lab.end():end]
        # provenance: % src: lines just above the environment, and inside it
        above = tex[max(0, m.start() - 400):m.start()].splitlines()[-4:]
        src = [l.strip()[2:].strip() for l in above + body.splitlines()
               if l.strip().startswith("% src:")]
        # the proof that follows, if any
        tail = tex[end:end + 6000]
        pm = re.match(r"\\end\{%s\}\s*(%%[^\n]*\n\s*)*\\begin\{proof\}" % kind, tail)
        proof = ""
        if pm:
            pstart = end + pm.end()
            proof = tex[pstart:tex.index(r"\end{proof}", pstart)]
        sec = section_of(secs, m.start())
        statement = "\n".join(l for l in body.splitlines() if not l.strip().startswith("%")).strip()
        results.append({
            "label": label, "kind": KINDS[kind], "title": title,
            "number": nums.get(label, {}).get("number"), "page": nums.get(label, {}).get("page"),
            "section": {"title": sec["title"], "number": nums.get(sec["label"], {}).get("number"),
                        "label": sec["label"]} if sec else None,
            "statement": statement, "provenance": sorted(set(src)),
            "uses": sorted({r for r in refs_in(body) if r != label}),
            "proof_uses": sorted({r for r in refs_in(proof) if r != label}),
            "has_proof": bool(proof),
        })

    # transitive dependence on the GJS package and on U_GJS itself
    by_label = {r["label"]: r for r in results}
    def closure(label, seen=None):
        """Labels reachable from `label`.  Assumptions are leaves: they are hypotheses,
        not derived statements, so the chain stops at A1-A8 instead of running on into
        whatever their own text happens to reference."""
        seen = seen or set()
        r = by_label.get(label)
        if not r or (r["kind"] == "Assumption" and seen):
            return seen
        for e in set(r["uses"]) | set(r["proof_uses"]):
            if e not in seen:
                seen.add(e)
                closure(e, seen)
        return seen
    for r in results:
        dep = closure(r["label"])
        r["imports_A8"] = GJS_LABEL in dep or r["label"] == GJS_LABEL
        r["cites_UGJS"] = UGJS_EQ in dep
    return {"generated_from": {"tex": "part_i/main.tex", "aux": "part_i/main.aux"},
            "note": "Generated by docs/extract.py. Do not edit by hand.",
            "macros": macros, "results": results}


def markdown(data):
    rs = [r for r in data["results"] if r["number"]]
    order = {}
    for r in rs:
        s = r["section"]
        key = (s["number"] or "", s["title"] if s else "")
        order.setdefault(key, []).append(r)
    L = ["---", "title: Results", "---", "",
         "# Result inventory", "",
         "Every numbered statement of `part_i/main.tex`, in order, generated by",
         "`docs/extract.py` from the manuscript and its `.aux`. **Do not edit by hand.**", "",
         "`imports A8` marks a statement whose own proof chain reaches Assumption A8, the",
         "GJS package. Item A8(vi) of that package is U_GJS, the single import that is not a",
         "literal quotation of a printed theorem, so everything marked here inherits the",
         "conditionality of [Theorem 12.2](status.md). `cites U_GJS` marks the narrower set",
         "that reaches the displayed inequality itself.", "",
         "| # | kind | statement | section | p. | imports A8 | cites U_GJS |",
         "|---|---|---|---|---|---|---|"]
    for r in rs:
        s = r["section"]
        L.append("| `%s` | %s | %s | %s %s | %d | %s | %s |" % (
            r["number"], r["kind"], (r["title"] or "").replace("|", "\\|"),
            (s["number"] or "") if s else "", (s["title"] if s else "").replace("|", "\\|"),
            r["page"], "yes" if r["imports_A8"] else "-", "yes" if r["cites_UGJS"] else "-"))
    L += ["", "## Statements", ""]
    for (_, stitle), group in sorted(order.items()):
        L.append("### %s" % stitle)
        for r in group:
            L += ["", "#### %s %s%s" % (r["kind"], r["number"],
                                        " (%s)" % r["title"] if r["title"] else ""),
                  "", "`%s` &middot; page %d%s%s" % (
                      r["label"], r["page"],
                      " &middot; imports A8" if r["imports_A8"] else "",
                      " &middot; proof in the manuscript" if r["has_proof"] else ""), ""]
            L += ["```latex", r["statement"], "```", ""]
            if r["provenance"]:
                L.append("Provenance: " + "; ".join("`%s`" % p for p in r["provenance"]) + "")
            dep = [d for d in r["uses"] + r["proof_uses"] if d in {x["label"] for x in rs}]
            if dep:
                L.append("Uses: " + ", ".join("`%s`" % d for d in sorted(set(dep))))
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    data = extract()
    js, md = json.dumps(data, indent=1, ensure_ascii=False) + "\n", markdown(data)
    # The interactive graph imports this statically rather than fetching it, so there
    # is no loading state to race.  (It does NOT make the pages work from file://:
    # module scripts are blocked there by the origin rules, and the page renders an
    # empty frame.  Serve docs/ over http to try them locally.)
    mod = ("// Generated by docs/extract.py. Do not edit by hand.\n"
           "export const RESULTS = "
           + json.dumps([r for r in data["results"] if r["number"]],
                        separators=(",", ":"), ensure_ascii=False) + ";\n")
    if "--check" in sys.argv:
        stale = [p.name for p, new in ((OUT_JSON, js), (OUT_MD, md), (OUT_JS, mod))
                 if not p.exists() or p.read_text() != new]
        print("stale: " + ", ".join(stale) if stale else "up to date")
        sys.exit(1 if stale else 0)
    OUT_JSON.write_text(js); OUT_MD.write_text(md); OUT_JS.write_text(mod)
    n = len(data["results"])
    print("%d statements -> docs/results.json, docs/results.md (%d import A8, %d cite U_GJS)"
          % (n, sum(r["imports_A8"] for r in data["results"]),
             sum(r["cites_UGJS"] for r in data["results"])))
