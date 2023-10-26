t = int(input())
for _ in range(t):
    n = int(input())
    health = list(map(int, input().split()))
    
    spell2_count = 0
    total_spell1 = 0
    
    health.sort(reverse=True)
    
    for h in health:
        if h > 1:
            h -= 1
            total_spell1 += 1
        elif h == 1:
            spell2_count += 1
        if spell2_count == 2:
            total_spell1 += 1
            spell2_count = 0
    
    print(total_spell1)