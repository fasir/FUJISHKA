import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Case insensitive replacement for B-QUICK ERP -> Fujishka ERP
    content = re.sub(re.escape('B-QUICK ERP'), 'Fujishka ERP', content, flags=re.IGNORECASE)
    
    # Case insensitive replacement for Fujeeka Van Sales -> Fujishka R-POS
    content = re.sub(re.escape('Fujeeka Van Sales'), 'Fujishka R-POS', content, flags=re.IGNORECASE)

    # Some might use B-Quick ERP
    content = re.sub(re.escape('B-Quick ERP'), 'Fujishka ERP', content, flags=re.IGNORECASE)
    
    # Write back if changed
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Processed {filepath}")
