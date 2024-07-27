
subjects = ["C","BASIC", "Perl", "Rubi","C++", "C#", "Python", "JAVA"]

print(len(subjects))

'''subjects.append("TOC")
print(subjects)

'''
'''
print(len(subjects))
subjects.insert(2, "OS")
print(subjects)
'''

subjects.remove("JAVA")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()
print(subjects)
'''
subjects.clear()
print(subjects)
'''
subjects2 = subjects.copy()
print(subjects2)

pos = subjects.index("Perl")
print(pos)
posn = subjects.count("Perl")
print(posn)


subjects.sort(reverse=True)
print(subjects)