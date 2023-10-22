stack = []

n = int(input())

for _ in range(n):
    command = input().split()
    action = int(command[0])
    
    if action == 1:
        number = int(command[1])
        stack.append(number)
    elif action == 2:
        if stack:
            stack.pop()
    elif action == 3:
        if stack:
            print(max(stack))
    elif action == 4:
        if stack:
            print(min(stack))
    elif action == 5:
        print(len(stack))

while stack:
    print(stack.pop(), end=" ")