# Storing input
n = int(input())
a = [int(digit) for digit in input().split()]

# Counting ways
ways = 0
for i in range(n):
    for j in [x for x in range(n) if x != i]:
        for k in [x for x in range(n) if (x != i and x != j)]:
            if (a[i] + a[j]) == a[k]:
                ways += 1
print(ways)