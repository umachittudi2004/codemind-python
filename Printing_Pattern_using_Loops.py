def print_pattern(n):
    for i in range(1, 2 * n):
        for j in range(1, 2 * n):
            print(max(abs(n - i), abs(n - j)) + 1, end=" ")
        print()

n = int(input())  # Change this value to control the size of the pattern
print_pattern(n)
