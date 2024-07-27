# xargs

def student(id, name):
    print(id, name)
student(100, "Shahadat")

def student(*details):
    print(details)

student("Shahadat", 11001, "XII")


def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(10, 20, 30)
add(10,20, 30, 40,50)