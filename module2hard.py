def find_password(n):
    result = ""
    used_numbers = set()


    for i in range(1, 21):
        if i == n:
            continue


        for j in range(1, 21):
            if j == n or j in used_numbers:
                continue


            sum_of_pair = i + j
            if n % sum_of_pair == 0:
                result += f"{i}{j}"
                used_numbers.add(j)


    return result


n = 3
password = find_password(n)
print(password)

n = 4
password = find_password(n)
print(password)

n = 5
password = find_password(n)
print(password)

n = 6
password = find_password(n)
print(password)

n = 7
password = find_password(n)
print(password)

n = 8
password = find_password(n)
print(password)

n = 9
password = find_password(n)
print(password)

n = 10
password = find_password(n)
print(password)

n = 11
password = find_password(n)
print(password)

n = 12
password = find_password(n)
print(password)

n = 13
password = find_password(n)
print(password)

n = 14
password = find_password(n)
print(password)

n = 15
password = find_password(n)
print(password)

n = 16
password = find_password(n)
print(password)

n = 17
password = find_password(n)
print(password)

n = 18
password = find_password(n)
print(password)

n = 19
password = find_password(n)
print(password)

n = 20
password = find_password(n)
print(password)




