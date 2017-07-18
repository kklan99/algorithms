def rotateImage(a):
    n = len(a) - 1
    # rotate the square matrix by each layer
    for i in range((n//2) + 1):
        # for each layer, rotate each element by 90 deg
        for j in range(i, n-i):
            temp = a[i][j]
            a[i][j] = a[n-j][i]
            a[n-j][i] = a[n-i][n-j]
            a[n-i][n-j] = a[j][n-i]
            a[j][n-i] = temp
    return a