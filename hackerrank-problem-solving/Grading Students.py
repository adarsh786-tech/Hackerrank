import math
def check_multiple_of_five(n):
    x=n%5
    n= n+(5-x)
    return n



def grades_check(grades, n):
    for i in range(n):
        if(grades[i] < 38):
            pass
        else:
            x= check_multiple_of_five(grades[i])
            if((x - grades[i]) < 3):
                grades[i] = x
            elif((x-grades[i]) == 3):
                pass
    return grades


if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input().strip())
        grades.append(grades_item)
    res = grades_check(grades,n)
    for i in range(n):
        print(res[i])