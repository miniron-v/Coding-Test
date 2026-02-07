while (arr := input().lower()) != '#':
    print(sum(arr.count(v) for v in 'aeiou'))