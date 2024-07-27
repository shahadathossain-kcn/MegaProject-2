# Queue Example


from collections import deque
bank = deque(["A", "B", "C", "D"])
bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()
print(bank)

if not bank:
    print("NO person left!")
