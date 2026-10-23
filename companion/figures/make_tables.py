#!/usr/bin/env python3
"""Write the pgfplots tables of the companion's computed figures.

    python3 companion/figures/make_tables.py        # from the repository root

Nothing is computed here.  The curves come from docs/figures/curves.json, which
docs/figures/make_figures.py generates from the manuscript's own formulas (the filter
W_gamma of Lemma 9.1 and the two summands of the rate function Psi_gamma of Lemma 10.5),
so the companion's figures and the site's are the same numbers.  The one addition is a
sampling of the filter's Fourier transform hat W_gamma(E) = chi(E)/E, taken from the same
chi() that make_figures.py uses, which is a drawing of the definition (17) and evaluates
nothing beyond it.

Output, one file per table, whitespace-separated with a header line:
    filter_g<gamma>.dat      t  absW        |W_gamma(t)| on the graded grid of the site
    filter_env_g<gamma>.dat  t  absW        the local maxima of |W_gamma|, its envelope
    psi_g<gamma>.dat         d  exp  tail  psi   the two summands at M = 1, and Psi itself
                                              with the max{2, .} clause below d0 = 4 + 2/gamma
    hatW_g<gamma>.dat        E  hatW        chi(E)/E on [-3 gamma, 3 gamma]
"""
import json, pathlib, sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "docs" / "figures"))
from make_figures import chi                                                       # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
curves = json.loads((ROOT / "docs" / "figures" / "curves.json").read_text())["series"]


def write(name, header, rows):
    lines = [header] + [" ".join("%.6g" % v for v in r) for r in rows]
    (HERE / name).write_text("\n".join(lines) + "\n")
    print("  wrote %s (%d rows)" % (name, len(rows)))


for key, s in curves.items():
    gam = float(key)
    tag = key.replace(".", "p")
    write("filter_g%s.dat" % tag, "t absW",
          [(t, w) for t, w in zip(s["t"], s["absW"]) if w > 0])
    write("filter_env_g%s.dat" % tag, "t absW", list(zip(s["envT"], s["envW"])))
    d0 = s["d0"]
    rows = []
    for d, e, tl in zip(s["d"], s["psiExp"], s["psiTail"]):
        psi = e + tl if d >= d0 else max(2.0, e + tl)
        rows.append((d, e, tl, psi))
    write("psi_g%s.dat" % tag, "d exp tail psi", rows)
    E = np.linspace(-3 * gam, 3 * gam, 1201)
    hat = np.where(E != 0, chi(E, gam) / np.where(E != 0, E, 1.0), 0.0)
    write("hatW_g%s.dat" % tag, "E hatW", list(zip(E, hat)))
print("L1 norms and d0 per gamma:",
      {k: (s["L1"], s["d0"]) for k, s in curves.items()})
