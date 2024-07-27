import re
pattern = r"[aeiou]"

if re.match(pattern, "ahahadat"):
    print("Matched")

if re.match(pattern, "mmmmmh"):
    print("again matched")