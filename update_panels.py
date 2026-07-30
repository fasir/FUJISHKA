import re

filepath = r"c:\FUJISHKA\FUJISHKA\assets\css\fujishka-custom.css"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Panel 2 background
content = content.replace('background: rgba(3, 16, 22, 0.98) !important;', 'background: rgba(232, 247, 234, 0.88) !important;')
# Panel 4 background
content = content.replace('background: linear-gradient(135deg, rgba(5, 24, 30, 0.96) 0%, rgba(3, 18, 24, 0.98) 100%) !important;', 'background: rgba(232, 247, 234, 0.88) !important;')
# Panel 6 background
content = content.replace('background: linear-gradient(135deg, rgba(8, 28, 20, 0.96) 0%, rgba(5, 18, 24, 0.98) 100%) !important;', 'background: rgba(232, 247, 234, 0.88) !important;')

# For panels 2, 4, 6, change h3 and showcase-item strong color to #111827
panels = [2, 4, 6]
for p in panels:
    # h3
    target_h3 = f".fj-hscroll-panel:nth-child({p}) .fj-product-showcase h3 {{\n  color: #ffffff !important;\n}}"
    repl_h3 = f".fj-hscroll-panel:nth-child({p}) .fj-product-showcase h3 {{\n  color: #111827 !important;\n}}"
    content = content.replace(target_h3, repl_h3)
    
    # showcase-desc
    target_desc = f".fj-hscroll-panel:nth-child({p}) .fj-product-showcase .showcase-desc {{\n  color: rgba(255, 255, 255, 0.65) !important;\n}}"
    repl_desc = f".fj-hscroll-panel:nth-child({p}) .fj-product-showcase .showcase-desc {{\n  color: #4b5563 !important;\n}}"
    content = content.replace(target_desc, repl_desc)
    
    # showcase-item background
    target_item_bg = f".fj-hscroll-panel:nth-child({p}) .fj-showcase-item {{\n  background: rgba(255, 255, 255, 0.05) !important;"
    repl_item_bg = f".fj-hscroll-panel:nth-child({p}) .fj-showcase-item {{\n  background: rgba(255, 255, 255, 0.85) !important;"
    content = content.replace(target_item_bg, repl_item_bg)
    
    # showcase-item strong
    target_strong = f".fj-hscroll-panel:nth-child({p}) .fj-showcase-item strong {{\n  color: #ffffff !important;\n}}"
    repl_strong = f".fj-hscroll-panel:nth-child({p}) .fj-showcase-item strong {{\n  color: #111827 !important;\n}}"
    content = content.replace(target_strong, repl_strong)
    
    # Also fix mobile dark brand panels
    # .fj-hscroll-panel:nth-child(2) { ... background: rgba(12, 36, 22, 0.75) !important; }
    # I'll just change the mobile ones using regex
    pat_mobile = rf"(\.fj-hscroll-panel:nth-child\({p}\)\s*{{[^}}]*?background:\s*)rgba\([^)]+\)( !important;)"
    content = re.sub(pat_mobile, r"\g<1>rgba(232, 247, 234, 0.88)\g<2>", content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated CSS successfully.")
