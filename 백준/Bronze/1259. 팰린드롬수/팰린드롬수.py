def fun(n):
    data_len = len(n)
    half_data_len = data_len // 2

    if data_len % 2 == 0:
        left = n[0:half_data_len]
        right = n[half_data_len : data_len]
        right = right[::-1]
    else:
        left = n[0:half_data_len]
        right = n[half_data_len+1:data_len]
        right = right[::-1]

    if left == right :
        print("yes")
    else:
        print("no")

while True:
    n = input()
    if n == '0':
        break
    fun(n)