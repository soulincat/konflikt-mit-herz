#!/usr/bin/env python3
"""
Script to help visualize and reorder HTML sections.
Target order:
1. Hero
2. Scientific Truth ("Du wurdest nicht gelehrt")  
3. Mission ("Wir sind auf der wilden Mission")
4. Guides ("Deine Guides")
5. Final CTA ("Die Gespräche, die Du vermeidest")
6. Offer ("Conflict Competence with Heart")
7. Framework ("How It Works")
8. Testimonials
9. Photo Section (NEW - to be added)
10. FAQ
"""

import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all section markers
section_pattern = r'(<!-- SECTION.*?-->)'
sections = re.findall(section_pattern, content)

print("Current sections found:")
for i, section in enumerate(sections, 1):
    print(f"{i}. {section}")

