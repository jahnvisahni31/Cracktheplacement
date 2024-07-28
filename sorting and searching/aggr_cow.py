def largest_minimum_distance(N, C, x):
    x.sort()
    low, high = 1, x[-1] - x[0]

    while low <= high:
        mid = (low + high) // 2
        cow_count = 1
        last_pos = x[0]

        for i in range(1, N):
            if x[i] - last_pos >= mid:
                cow_count += 1
                last_pos = x[i]

        if cow_count >= C:
            low = mid + 1
        else:
            high = mid - 1

    return high

# Example usage
t = int(input())
for _ in range(t):
    N, C = map(int, input().split())
    x = [int(input()) for _ in range(N)]
    print(largest_minimum_distance(N, C, x))
