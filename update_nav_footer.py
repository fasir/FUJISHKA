import os
import re
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove from navbar
    # Look for the Blogs and FAQ <li> items in the nav area
    # Regex to match <li><a href="blogs.html"...>Blogs</a></li> (with possible newlines)
    content = re.sub(r'^\s*<li[^>]*>\s*<a href="blogs\.html"[^>]*>.*?</a>\s*</li>\r?\n', '', content, flags=re.MULTILINE|re.IGNORECASE)
    content = re.sub(r'^\s*<li[^>]*>\s*<a href="faq\.html"[^>]*>.*?</a>\s*</li>\r?\n', '', content, flags=re.MULTILINE|re.IGNORECASE)

    # 2. Add to footer
    # Find the Company section in the footer which has:
    # <h5>Company</h5>
    # <ul>
    #   <li><a href="#"><i class="fa-solid fa-chevron-right" style="font-size:10px;"></i> About Us</a></li>
    #   <li><a href="#"><i class="fa-solid fa-chevron-right" style="font-size:10px;"></i> Blogs</a></li>
    #   ...
    
    # Let's replace the whole Company list to fix links and add FAQ.
    # Current Company block usually starts with <h5>Company</h5> and ends with </ul>
    
    company_block_regex = r'(<h5>Company</h5>\s*<ul>)(.*?)(</ul>)'
    
    def replacer(match):
        prefix = match.group(1)
        inner = match.group(2)
        suffix = match.group(3)
        
        # Replace href="#" for About Us, Blogs, Contact Us
        inner = re.sub(r'<a href="#">([^<]*<i[^>]*></i>\s*About\s*Us)</a>', r'<a href="about-us.html">\1</a>', inner, flags=re.IGNORECASE)
        inner = re.sub(r'<a href="#">([^<]*<i[^>]*></i>\s*Blogs)</a>', r'<a href="blogs.html">\1</a>', inner, flags=re.IGNORECASE)
        inner = re.sub(r'<a href="#">([^<]*<i[^>]*></i>\s*Contact\s*Us)</a>', r'<a href="contact.html">\1</a>', inner, flags=re.IGNORECASE)
        
        # If FAQ doesn't exist, add it before Contact Us
        if 'FAQ</a>' not in inner:
            faq_item = '\n                <li><a href="faq.html"><i class="fa-solid fa-chevron-right" style="font-size:10px;"></i> FAQ</a></li>'
            # Insert before Contact Us if present, otherwise at end
            if 'Contact Us</a>' in inner:
                inner = re.sub(r'(<li[^>]*><a href="contact\.html"[^>]*>.*?Contact\s*Us</a>\s*</li>)', faq_item + r'\n                \1', inner, flags=re.IGNORECASE)
            else:
                inner += faq_item
        
        return prefix + inner + suffix

    new_content = re.sub(company_block_regex, replacer, content, flags=re.DOTALL)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")
