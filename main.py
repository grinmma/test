# lst = [x for x in input().split('; ')
#        if len(x) % 2 != 0 and x[len(x) // 2] in 'aeyuio']
# print(input().join(lst))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

test = c[-1]
res = list((set(a) ^ set(b) ^ set(c)) - (set(a) & set(b) & set(c)))
print('!!'.join([str(x) for x in res if x < test]))
