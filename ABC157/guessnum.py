import sys

N, M = tuple(int(n) for n in input().split())

str_list = ['0' for n in range(N)]
str_state = [0 for n in range(N)] #0 if digit unchanged, 1 if changed

#print(str_list)
#print(str_state)


for i in range(M):
    si, ci = tuple(int(n) for n in input().split())
    #print('si: %d, ci: %d' % (si, ci))
    ci = str(ci)
    if str_state[si - 1] == 0:
        str_list[si - 1] = ci
        str_state[si - 1] = 1
        #print(str_list)
        #print(str_state)
    elif str_list[si - 1] != ci:
        print(-1)
        sys.exit(0)
    #else:
    #    pass

for i in range(len(str_list)):
    if str_list[i] != '0':
        break
    else:
        if i == len(str_list) - 1:
            break
        if str_state[i] == 0:
            str_list[i] = '1'
            break

num = str(int(''.join(str_list)))
if len(num) == N:
    print(num)
else:
    print(-1)
