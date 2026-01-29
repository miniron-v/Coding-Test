from collections import defaultdict

n = int(input())

correct = defaultdict(bool)
counter = defaultdict(int)

for _ in range(n):
    arr = list(map(str, input().split()))

    if(arr[1] == 'megalusion'):
        continue

    if(arr[2] == '4'):
        correct[arr[1]] = True

    if(correct[arr[1]] == False):
        counter[arr[1]] += 1

correct_count = sum(1 for value in correct.values() if value == True)
wrong_count = sum(value for name, value in counter.items() if correct[name] == True)

print(correct_count / (correct_count + wrong_count) * 100 if correct_count + wrong_count > 0 else 0)