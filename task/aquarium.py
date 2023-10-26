def calculate_max_height(t, test_cases):
    results = []

    for i in range(t):
        n, x, a = test_cases[i]

        min_height = 1
        max_height = max(a)

        while min_height < max_height:
            mid_height = (min_height + max_height + 1) // 2

            water_needed = sum(max(0, ai - mid_height) for ai in a)

            if water_needed <= x:
                min_height = mid_height
            else:
                max_height = mid_height - 1

        results.append(max_height)

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, x, a))

results = calculate_max_height(t, test_cases)
for result in results:
    print(result)