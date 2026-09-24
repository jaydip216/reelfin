"""Dependency-free portability checks, not a full CSS parser or visual test."""
from pathlib import Path
import re

css = Path(__file__).with_name('netflix-inspired.css').read_text()
errors = []
checks = {
    'item/user/library ID selectors': r'\[data-(?:id|userid|parentid)\s*=',
    'embedded asset URLs or imports': r'url\s*\(|@import\b',
    'server addresses or local paths': r'https?://|192\.168\.|127\.0\.0\.1|localhost|/Users/|/Items/',
    'old personal branding': r'\bagni\b',
    'blanket home aspect ratio': r'#homeTab\s+\.cardPadder\s*\{',
    'unguarded first-section scroll snapping': r'\.section0\s+\.(?:scrollX|card)\s*\{[^}]*scroll-snap',
}
for label, pattern in checks.items():
    if re.search(pattern, css, re.I):
        errors.append(label)
# Remove comments and quoted strings before checking delimiter nesting.
tokens = re.sub(r'/\*.*?\*/|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', '', css, flags=re.S)
stack = []
for char in tokens:
    if char in '{([':
        stack.append(char)
    elif char in '})]':
        if not stack or stack.pop() != dict(zip('})]', '{(['))[char]:
            errors.append('unbalanced CSS delimiters')
            break
if stack:
    errors.append('unclosed CSS delimiters')
if errors:
    raise SystemExit('FAILED: ' + ', '.join(errors))
print('PASS: portability patterns and CSS delimiter checks. Browser testing still required.')
