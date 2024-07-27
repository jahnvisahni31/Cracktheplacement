def radixSort(arr, n):
    # code here
    def co(arr, exp):
        n = len(arr)
        c = [0]* (10)
        te = [0] * n
        for i in range(n):
            di = (arr[i]//exp) % 10
            c[di] += 1
        for i in range(1, 10):
            c[i] += c[i-1]
        for i in range(n-1, -1, -1):
            di = (arr[i]//exp) % 10
            cn = c[di]
            te[cn-1] = arr[i]
            c[di] -= 1
        i = 0
        for el in te:
            arr[i] = el
            i += 1
    
    max_n = max(arr)
    ex = 1
    while (max_n//ex) > 0:
        co(arr, ex)
        ex *= 10
    
