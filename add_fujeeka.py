import glob

html_files = glob.glob('*.html')

search_str = """                  <li><a href="van-sales.html"><i class="fa-solid fa-truck"
                        style="color:#3EB649;margin-right:8px;"></i>Fujishka R-POS</a></li>"""

replace_str = """                  <li><a href="van-sales.html"><i class="fa-solid fa-truck"
                        style="color:#3EB649;margin-right:8px;"></i>Fujishka R-POS</a></li>
                  <li><a href="#"><i class="fa-solid fa-layer-group"
                        style="color:#3EB649;margin-right:8px;"></i>Fujeeka</a></li>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_str in content:
        content = content.replace(search_str, replace_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
