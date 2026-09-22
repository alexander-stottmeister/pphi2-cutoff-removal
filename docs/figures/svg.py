"""Minimal SVG writer for the figures of docs/.

No dependencies, no charting library: the curves here are exponentials, power laws and
one Fourier transform, and hand-written SVG keeps the output diffable in review, which
matters more for this repository than convenience.

Colours are LITERAL in the output, never CSS custom properties.  librsvg -- and any
number of other renderers -- do not resolve var(), and a figure that depends on them
renders as a black rectangle.  Figures that appear in the README must survive whatever
renders them.  Each figure is therefore emitted twice, light and dark, and the README
selects between them with <picture> and prefers-color-scheme, which GitHub supports.

Figure code writes tokens like "var(--acc)"; save() substitutes the theme's literal
value and refuses to write a file with any token left over.
"""
import re

LIGHT = {"bg": "#ffffff", "fg": "#1f2328", "mut": "#6e7781", "line": "#d0d7de",
         "acc": "#0969da", "warn": "#bc4c00", "cond": "#8250df", "ok": "#1a7f37",
         "fill": "#ddf4ff", "cfill": "#f3eefc"}
DARK = {"bg": "#0d1117", "fg": "#e6edf3", "mut": "#8d96a0", "line": "#30363d",
        "acc": "#4493f8", "warn": "#db6d28", "cond": "#c297ff", "ok": "#3fb950",
        "fill": "#0c2d6b", "cfill": "#2a1f45"}

_BASE = """
  text{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
       fill:%(fg)s}
  .mut{fill:%(mut)s} .sm{font-size:11px} .xs{font-size:9.5px} .b{font-weight:600}
  .ax{stroke:%(line)s;stroke-width:1;fill:none}
  .gr{stroke:%(line)s;stroke-width:.5;fill:none;opacity:.6}
"""


class Svg:
    def __init__(self, w, h, title, desc="", theme=None):
        self.w, self.h, self.theme = w, h, theme or LIGHT
        self.p = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
                  'height="%d" role="img" aria-labelledby="figtitle figdesc">' % (w, h, w, h),
                  '<title id="figtitle">%s</title>' % esc(title),
                  '<desc id="figdesc">%s</desc>' % esc(desc or title),
                  '<style>%s</style>' % (_BASE % self.theme),
                  '<rect width="%d" height="%d" fill="var(--bg)"/>' % (w, h)]

    def add(self, s):
        self.p.append(s); return self

    def line(self, x1, y1, x2, y2, cls="ax", **kw):
        return self.add('<line x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" class="%s"%s/>'
                        % (x1, y1, x2, y2, cls, attrs(kw)))

    def rect(self, x, y, w, h, **kw):
        return self.add('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f"%s/>'
                        % (x, y, w, h, attrs(kw)))

    def path(self, d, **kw):
        return self.add('<path d="%s"%s/>' % (d, attrs(kw)))

    def poly(self, pts, **kw):
        return self.path("M" + " L".join("%.2f %.2f" % q for q in pts), **kw)

    def circle(self, cx, cy, r, **kw):
        return self.add('<circle cx="%.2f" cy="%.2f" r="%.2f"%s/>' % (cx, cy, r, attrs(kw)))

    def text(self, x, y, s, cls="", **kw):
        return self.add('<text x="%.2f" y="%.2f"%s%s>%s</text>'
                        % (x, y, ' class="%s"' % cls if cls else "", attrs(kw), esc(s)))

    def render(self):
        out = "\n".join(self.p + ["</svg>"]) + "\n"
        out = re.sub(r"var\(--(\w+)\)", lambda m: self.theme[m.group(1)], out)
        left = re.findall(r"var\(--\w+\)", out)
        if left:
            raise ValueError("unresolved colour tokens: %s" % sorted(set(left)))
        return out

    def save(self, path):
        path.write_text(self.render()); return path


def attrs(kw):
    return "".join(' %s="%s"' % (k.replace("_", "-"), v) for k, v in kw.items())


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
