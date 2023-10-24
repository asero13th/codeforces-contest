def solve():
    d, sum_time = map(int, input().split())
    schedule = []
    min_total = 0
    max_total = 0

    for _ in range(d):
        min_time, max_time = map(int, input().split())
        schedule.append([min_time, max_time])
        min_total += min_time
        max_total += max_time

    if not min_total <= sum_time <= max_total:
        return "NO"

    result = [x[0] for x in schedule]
    remaining = sum_time - min_total

    for i in range(d):
        take = min(remaining, schedule[i][1] - schedule[i][0])
        result[i] += take
        remaining -= take

    return "YES\n" + " ".join(map(str, result))

print(solve())