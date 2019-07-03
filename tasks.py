

# ---------Перебор в двоичном коде--------------#

CELL_BORDER_CNT = 4
RABBITS_CNT = 5
TOTAL_DIGITS_CNT = CELL_BORDER_CNT + RABBITS_CNT
DIGIT_SET = "01"


def check_sum(s) -> bool:
    return sum(int(digit) for digit in str(s)) == CELL_BORDER_CNT


def brute(S, N) -> list:
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
# -----------------------------------------------#

#-------------Сочетания из N по K----------------#

SYNBOLS_SET = ["1", "2", "3"]
RESTRICTION = 2

def сombinations(N, K):
    if K == 0: yield ""
    for digit in N:
        N.remove(digit)
        for symbol in сombinations(N, K - 1):
            yield digit + symbol
        N.append(digit)
    
def set_uniq(gen):
    ret = []
    for i in gen:
        ret.append(i)
    return list(set(ret))

# -----------------------------------------------#

if __name__ == "__main__":
    for i in brute(DIGIT_SET, TOTAL_DIGITS_CNT):
        print(i)
# -----------------------------------------------#
    for i in set_uniq(сombinations(SYNBOLS_SET, RESTRICTION)):
        print(i)