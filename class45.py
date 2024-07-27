file = open("student.txt", "r+")
"""
#print(file.writable())
text = file.read()
print(text)
size = len(text)
print(size)

"""

"""
Shahadat Hossain - Facebook Ads Expert
Rakib Alam - YouTube SEO Expert
Irfan Hossain - Video Editor
Tanvir - Entrepreneur
"""


"""
text1 = file.readlines()
print(text1)

file.close()
"""

for line in file:
    print(line)

file.close()
