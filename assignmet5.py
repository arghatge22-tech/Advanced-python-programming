def LCS(X, Y):
    m = len(X)
    n = len(Y)

    lcs_table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    index = lcs_table[m][n]
    lcs_string = [''] * index

    i = m
    j = n

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs_string)

X = "VIRAT"
Y = "KOLHI"

result = LCS(X, Y)

print("String X:", X)
print("String Y:", Y)
print("Longest Common Subsequence:", result)
print("Length of LCS:", len(result))
