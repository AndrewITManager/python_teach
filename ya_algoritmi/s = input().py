# s = input()# ввод строки
# ans = '' #пустая строка
# anscnt = 0 
# print(set(s))
# for now in set(s):
#     nowcnt = 0
#     for j in range(len(s)):
#         if now == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = now
#         anscnt = nowcnt
# print(ans)
# print(anscnt)

s = input()# ввод строки
anscnt = 0 
dct = {}
for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
    if dct[now] > anscnt:
        anscnt = dct[now]
        ans = now
print(ans)
print(anscnt)
