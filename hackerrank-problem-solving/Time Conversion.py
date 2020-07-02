def timeConversion(str):
    h, m, s = map(int, str[:-2].split(':'))
    p = str[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    print(('%02d:%02d:%02d') % (h, m, s))


if __name__ == '__main__':
    str = input().strip()
    timeConversion(str)