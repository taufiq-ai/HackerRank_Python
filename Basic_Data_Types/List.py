List = []
n = int(input())
for i in range(n):
    cmd = input().split()
    
    if cmd[0] == 'insert':
        List.insert(int(cmd[1]), int(cmd[2]))

    elif cmd[0] == 'print':
        print(List)

    elif cmd[0] == 'remove':
        List.remove(int(cmd[1]))

    elif cmd[0] == 'append':
        List.append(int(cmd[1]))
    
    elif cmd[0] == 'sort':
        List.sort()

    elif cmd[0] == 'reverse':
        List.reverse()

    elif cmd[0] == 'pop':
        List.pop()