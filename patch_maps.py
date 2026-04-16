import re
import urllib.parse

file_path = '/Users/jeffchang/Documents/Jeff/Jeff/6F-9/5F-29-PTO-Jap.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def repl(match):
    full_block = match.group(0)
    
    # Extract loc and item
    loc_match = re.search(r"loc:\s*'([^']+)'", full_block)
    item_match = re.search(r"item:\s*'([^']+)'", full_block)
    
    if loc_match and item_match:
        loc = loc_match.group(1)
        item = item_match.group(1)
        
        # Clean emojis
        item_clean = re.sub(r'[\U00010000-\U0010ffff]', '', item).strip()
        
        if '→' in loc:
            loc = loc.split('→')[-1].strip()
            
        if '羽田' in loc and ('飯店' in loc or loc == '羽田'):
            query = 'Hotel Villa Fontaine Grand Haneda Airport'
        elif loc == '可選' or loc == '':
            query = item_clean
        else:
            query = loc
            
        url = f"https://maps.google.com/?q={urllib.parse.quote(query)}"
        # Replace only the empty mapUrl
        new_block = re.sub(r"mapUrl:\s*''", f"mapUrl: '{url}'", full_block)
        return new_block

    return full_block

# Match a whole schedule entry (from `{ time:` to `}`) that has `mapUrl: ''`
pattern = r"\{\s*time:[^}]+mapUrl:\s*''[^}]+\}"
new_content = re.sub(pattern, repl, content)

# Check if there's any remaining `mapUrl: ''` that were not formatted as exact objects
new_content = re.sub(r"mapUrl:\s*''", f"mapUrl: 'https://maps.google.com/?q=Tokyo'", new_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("JavaScript mapUrl fields successfully updated!")
