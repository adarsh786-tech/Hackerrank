import math


def compare_the_triplets(a, b):
    alice = 0
    bob = 0
    for i in range(0, len(a)):
        if a[i] < b[i]:
            alice += 1
        elif a[i] > b[i]:
            bob += 1
        else:
            pass
    print(bob, alice)


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    compare_the_triplets(a, b)
