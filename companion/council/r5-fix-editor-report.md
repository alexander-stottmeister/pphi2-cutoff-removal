# R5-fix editor report: the verifier's text findings applied (24 October 2026)

*Saved by the orchestrator from the editor agent's hand-back message, unchanged. This
editor was a fresh agent (the R4 editor's session had ended); it edited only
`companion/sections/*.tex` and built in a scratch copy. The orchestrator's final build
and the disposition of every finding are in `../PLAN.md`, Part 10.*

---

**R5-fix editor report.** I applied all nine items (V12–V18, N1, N4). The scratch build is 20 pages and every gate is 0. I edited only `companion/sections/*.tex` and ran no git, no kb, and no build in ROOT.

**What I read this session:** PLAN.md (all of it); r4-editor-report.md (all); r5-verifier-report.md (all); BRIEF.md ll. 80–110; labels.md; preamble.tex; companion.tex; all 12 section files; r3-return-cqft.md (D1); docs/imports.md ll. 1–30. In main.tex: ll. 355–452, 480–525, 580–612, 815–830, 880–950, 1150–1252, 1468–1625, 1900–1925, 2040–2135, 2222–2240, 2398–2440, 2515–2530. In main.pdf (pdftotext): pp. 6, 9, 32, 33. Status files: part_ii/README.md (status lines), strategy.md ll. 2203–2212, v4_assembly.tex ll. 1002–1012, README.md ll. 50–56. I also rendered GJ3 PDF p. 9 (printed p. 211) myself; it reads "There is a subsequence of the ω_n which converges w* to ω".

## Changes (ROOT/companion/sections, line numbers as now)

- **V14, s6 ll. 70–74.** The checkpoint box is now main.tex ll. 1908–1911 verbatim: "Let g∈𝒞_H, write H=H(g), Ω=Ω_g, β_t=β^g_t, and assume (G_γ). Let B⊂ℝ be compact, … for a bounded interval O. If R:=dist(B,O)>0 satisfies γR≥1, then", followed by the display. At l. 66 I removed "with H=H(g) and Ω=Ω_g,". I kept "an implication under (G_γ)", which rule 5 requires.
- **V16, s1 l. 118 (Table 1).** "Proposition 12.1 (29): for any (g_n)⊆𝒢 with d(g_n,O)→∞ for every bounded interval O and ω_{g_n} converging in norm on every 𝔄(O)."
- **V17, s8a ll. 25–26.** "…Hypothesis 13.1 \rec{Remark~13.3}{32}; \rec{\S14, \emph{Beyond weak coupling}}{33}, whose four items…". pdftotext confirms the heading is on printed p. 33.
- **V18, s2 l. 39.** "…converges $w^*$ to it".
- **V13, s9 l. 30.** "The scope amendment of 5 September 2026 gave U_GJS (A8(vi)) the status described in §4". I did not write "re-based U_GJS": the amendment changed the status (title page l. 76), not the inequality.
- **N1, s8b ll. 54–57.** "…`part_ii/README.md` says that phase closure was not yet reached, and the repository README says the gate is open; this companion uses the README's wording." I updated the source comment (ll. 2–4). I kept D1's "not yet", because the source prints "NOT yet reached".
- **N4, s4 ll. 106–109 (A6 cell).** "(i) speed one, the Trotter formula; (ii) (P): …; the cutoff cone is Proposition 2.7". The row stays at 3 lines; the longer wordings I tried took 4–5.
- **V15**
  - (a) s1 ll. 13–15: "the Glimm–Jaffe dynamics α, a g-independent one-parameter automorphism group of 𝔄 \rec{A6(ii)}{9}" (main.tex l. 593; A6 is on p. 9).
  - (b) s1 ll. 9–10 and 16–17: "the time-zero free field φ₀ of mass m₀>0 and covariance C=(2μ)⁻¹, μ=(−∂ₓ²+m₀²)^{1/2}" and "(coupling λ, C-Wick order)". "C-Wick ordering" is the record's term (Remark 2.5, l. 823).
  - (c) s1 ll. 35–36: "…at the gap parameter γ=m₁, an explicit function of the distance d stated in §6."
  - (d) s4 ll. 98–100: "the Euclidean interaction 𝒰_h in every L^p, e^{−ϱ𝒰_h} integrable (ϱ>0), so the measures dq_h are well defined". I defined the symbols by name rather than by formula, because the formula needs Φ, which §5 introduces later.
- **V12 (judgement; each paragraph now has three steps)**
  - §5 Piece II (s5 ll. 32–40): "Steps 1–4 of the proof of Theorem 5.1 treat Q_V=V(h)² as one observable of the GJS class… gives ‖Q_V‖≤M²/C₈ [(5)]" → (2)+(U_GJS) give (6) → weak closedness passes the bound to Ω_g.
  - §5 Piece IV (ll. 73–81): "…only if, with Ω_g, they span a dense subspace. They do [Thm 7.7], by…" → Checkpoint III kills 1_{[0,β]}(H(g))ψ_Q → "by density it is the projection onto ℂΩ_g; that is, H(g) has no spectrum in (0,m₁)". This also fixes the old "these vectors are total", which was inaccurate: centred vectors are orthogonal to Ω_g (Thm 7.7, ll. 1540–1542).
  - §6 Piece VII (ll. 96–104), in the record's order: Step 1 (d≥d₀, "Lemma 10.3 applies to every cell") → Step 2 (splitting) → "Summing the cells shell by shell … and integrating over s gives Proposition 10.4 … (Steps 3–4 of its proof)". No display or box was added.
- **Space recovered, from §§5–6 only (rule 11)**
  - s6 l. 9: "\rec{Lemma~10.5, eq.~(29)}{28}" became "of \rec{(29)}{28},".
  - s6 l. 44: "and obtains, for" became "; for".
  - s5 Piece II: lighter wording, with "at most nine" kept.

## Build (scratch copy, `pdflatex` ×3)

| check | result |
|---|---|
| errors (`^!`) | 0 |
| Overfull | 0 (none in any file, including fig-spine) |
| undefined | 0 |
| Underfull | 0 |
| pdftotext grep | empty |
| pages ("Output written") | 20 |

- The last page ends at y=645.2 pt, the same as the pre-edit baseline I built from the same snapshot. Slack is about 112 pt (≈0.17 pp).
- Section and float pages are unchanged from the baseline: Fig. 4 and §6 on p. 11; Fig. 6 on p. 15, inside §7; §8 at the top of p. 16. Page endings from p. 10 to p. 20 are identical to the baseline.
- At the end of my work, companion.tex, preamble.tex, bib.tex and figures/ in ROOT were byte-identical to my snapshot.
- Banned-word counts on the rendered text are identical to the baseline.
- **Fragility, seen in intermediate builds:**
  - one or two extra lines before §7 move Fig. 6 into §8 and strand the §8 heading;
  - about three extra lines in §§1–3 split the A8(vi) box around Fig. 2;
  - about two extra lines in §5 put Fig. 4 on a page before §6.

  Rebuild and check these three spots after any figure or caption change.

## Declined or adapted
- N4: I left out "the patched dynamics α" and "derived/not an import" to keep the row at 3 lines. The italic title already says "the dynamics α".
- V13: I used other wording than the brief, for the reason given above.

## Not done / Not verified / Not run
- **Not run:** any build in ROOT (so ROOT's companion.pdf and .log do not reflect these sections); git; kb.
- **Not verified:**
  - the three-step counts are my judgement, and other paragraphs were not re-audited;
  - s3 ll. 23–25 has the same ambiguous attachment ("for every O whose states converge…"); it is not on my list and is unchanged;
  - App B's V(h) row is unchanged; its symbols are now defined in §1.
- **Line numbers:** the brief's main.tex lines for A6 are off by one. As I read them, A6(i) is ll. 590–592, A6(ii) is ll. 593–599, and Scope is ll. 603–605.

**Scratch (outside the repo):** the session scratchpad (`edbuild`, the build; `edbase`, the pre-edit baseline build; `edorig`, the pre-edit section files).

**Files changed:** s1-result, s2-open, s4-import, s5-euclidean, s6-lppl, s8a-boundaries, s8b-part2, s9-record (.tex), all in `companion/sections/`.
