# Meta characters

import re
"""
pattern = r"colo.r"

if re.match(pattern, "colour"):
    print("Matched")
"""

pattern = r"^colo..r$"
if re.match(pattern, "colouur"):
    print("Matched")
if re.match(pattern, "colouaa"):
    print("Matched")