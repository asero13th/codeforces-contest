str1, str2 = list(input()), list(input())

def delete_from_left(str1, str2):
    len1, len2 = len(str1), len(str2)
    i = min(len1, len2)

    while i > 0 and str1[-1] == str2[-1]:
        str1.pop()
        str2.pop()
        if len1 == 0 or len2 == 0:
            break
     
        i -= 1

    print(len(str1) + len(str2))

delete_from_left(str1, str2)