# Search And Replace
import re
pattern = r"color"
text1 = "My favourite color is red. I love blue color as well."

text2 = re.sub(pattern, "colour", text1)
print(text2)
