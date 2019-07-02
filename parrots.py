def check_sum(S) -> bool:
    sum = 0
    for digit in S:
        sum += int(digit)
    return sum == 9


def placement(S, N) -> list:
    l = []
    M = len(S)
    for i in range(0, M ** N):
        line = ""
        k = i
        for j in range(0, N):
            line = S[int(k % M)] + line
            k /= M
        if check_sum(line):
            l.append(line)
    return l

if __name__ == "__main__":
    l = placement("0123456789", 5)
    print(l)