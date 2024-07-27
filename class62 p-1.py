# Regular expressions

import re
pattern = r"color"
"""
if (re.match(pattern,"Red is a color, I love red color")):
    print("Match")
else:
    print("Not matched")"""

"""
if (re.search(pattern,"Red is a color, I love red color")):
    print("Match")
else:
    print("Not matched")
"""

print(re.findall(pattern, "Red is a color, I love red color"))
