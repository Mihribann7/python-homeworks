def is_prime(num):
    if num < 2:
        return False
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt == 2

print(is_prime(8))