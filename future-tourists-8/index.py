scores = [4, 5, 6, 5]
ages = [2,1,2,1]

sortedPairs = sorted(zip(ages, scores), key=lambda x: x[0])
print(sortedPairs)

def solve(socres, ages):
    sortedPairs = sorted(zip(ages, scores), key=lambda x: x[0])

    def dp(i):
        if i == 0:
            return 0
        else:
            return max(dp(i - 1), dp(i - 2) + sortedPairs[i][1])