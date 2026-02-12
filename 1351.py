n, p, q = map(int, input().split())

dic = { 0 : 1 }

def dfs(i):
    if i not in dic:
        dic[i] = dfs(i // p) + dfs(i // q)

    return dic[i]

print(dfs(n))