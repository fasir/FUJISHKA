import os

css_path = r"c:\FUJISHKA\FUJISHKA\assets\css\fujishka-custom.css"

append_css = """

/* --- Overrides for Seamless "One Sheet" Look --- */
.fj-products {
  background: rgba(232, 247, 234, 0.88) !important;
}

.fj-hscroll-panel,
.fj-hscroll-panel:nth-child(1),
.fj-hscroll-panel:nth-child(2),
.fj-hscroll-panel:nth-child(3),
.fj-hscroll-panel:nth-child(4),
.fj-hscroll-panel:nth-child(5),
.fj-hscroll-panel:nth-child(6) {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}

.fj-hscroll-panel .fj-product-showcase,
.fj-hscroll-panel:nth-child(1) .fj-product-showcase,
.fj-hscroll-panel:nth-child(2) .fj-product-showcase,
.fj-hscroll-panel:nth-child(3) .fj-product-showcase,
.fj-hscroll-panel:nth-child(4) .fj-product-showcase,
.fj-hscroll-panel:nth-child(5) .fj-product-showcase,
.fj-hscroll-panel:nth-child(6) .fj-product-showcase {
  background: transparent !important;
  box-shadow: none !important;
  border: none !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
}

.fj-hscroll-panel .fj-product-showcase::before {
  display: none !important;
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(append_css)

print("Appended seamless sheet styles to CSS.")
