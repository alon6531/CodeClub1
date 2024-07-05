
def ToBainery():
    num = int(input())
    size = int(input())
    bain = ""
    for i in range(size - 1, -1, -1):
        if 2 ** i <= num:
            bain += "1"
            num -= (2 ** i)
        else:
            bain +="0"

    return bain

def not_bain(bain):
    new_bain = ""

    for i in range(len(bain)):
        if bain[i] == "0":
            new_bain += "1"
        else:
            new_bain += "0"

    return new_bain


def add(binery: str, carry: int = 1):
  if int(binery[-1]) + carry < 2:
    return binery[:-1] + str(int(binery[-1]) + carry)
  else:
    return add(binery[:-1], 1) + "1"


def mashlimt_to_tow(bain):
    bain = not_bain(bain)
    index = len(bain) - 1
    b2 = ""
    carry = True
    while index >= 0:
        num = int(bain[index])
        if carry:
            num += 1
        if num == 1:
            carry = False
        if num == 2:
            num = 0
        b2 = str(num) + b2
        index -= 1
    return b2


num = ToBainery()
print(mashlimt_to_tow(num))