#WAF to print the elements of a list in a single line. (list is the parameter)

heroes = ["spiderman", "ironman", "chotabhim", "thor", "captain america", "balck spiderman"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print()


