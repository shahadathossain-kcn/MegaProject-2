nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)


x = 49
idx = 0

for el in nums:
    if (el == x):
        print("numbe found at idx", idx)
        break
    idx += 1