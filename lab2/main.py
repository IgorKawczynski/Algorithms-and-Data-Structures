from typing import List


def rec(i):
    # warunek brzegowy - konczymy rekurencje gdy
    # wartosc parametru i spadnie ponizej zera
    if i < 0:
        return

    print(f'i: {i}')

    rec(i - 1)


rec(10)     # zaczynamy z parametrem i = 10


def numbers(n: int):
    if n < 0:
        return

    print(f'n: {n}')
    numbers(n - 1)


print("\nZAD1 :")
numbers(24)


def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)


x = 9
print("\nZAD2 :")
print("FIB({}) = {}".format(x, fib(x)))


def power(number: int, n: int) -> int:
    # if n < 0:
    #     return 1/number
    if n == 0:
        return 1
    if n == 1:
        return number
    return number * power(number, n-1)


print("\nZAD3 :")
print(power(4, 3))
print(power(2, 0))
print(power(3, 4))


# ITERACYJNIE
# def reverse(txt: str) -> str:
#     temp_str = ""
#     len_txt = len(txt)
#     i = len_txt-1
#     while i >= 0:
#         temp_str = temp_str + txt.__getitem__(i)
#         i = i - 1
#     return temp_str


def reverse(txt: str) -> str:
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]


print("\nZAD4 :")
txt_1 = "halinka"
txt_1_reversed = reverse(txt_1)
print(txt_1_reversed)


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)


print("\nZAD5 :")
print("Factorial(5) = {}".format(factorial(5)))


def prime(n: int) -> bool:
    def prime_support(n, s):
        if s > (n // 2):  # div (divide) with integral result
            return True
        elif n <= 1 or n % s == 0:
            return False
        else:
            return prime_support(n, s+1)
    return prime_support(n, 2)


print("\nZAD6 :")
print(prime(5))
print(prime(3))
print(prime(21))
print(prime(7))
print(prime(25))
print(prime(23))
print(prime(24))

# iterative
# def get_digit(number, n):
#     return number // 10 ** n % 10
#
#
# def n_sums(n: int) -> List[int]:
#     temp_list1 = [n]
#     temp_list = []
#     temp_sum_nieparz = 0
#     temp_sum_parz = 0
#     temp_start = 10 ** (n-1)
#     temp_end = (10 ** n)
#     i = n-1
#     while temp_start < temp_end and i >= 0:
#         if i % 2 == 0:
#             temp_sum_parz = temp_sum_parz + get_digit(n, i)
#             i = i - 1
#         if i % 2 != 0:
#             temp_sum_nieparz = temp_sum_nieparz + get_digit(n, i)
#             i = i - 1
#         if temp_sum_parz == temp_sum_nieparz:
#             temp_list.append(temp_start)
#         temp_start = temp_start + 1
#     return temp_list

# wtf version from intermarché
def n_sums(n: int, result='', diff=0):
    temp_list = []
    # if the number is less than n–digit
    if n > 0:

        ch = ord('0')

        # special case: number cannot start from 0
        if result == '':
            ch = ord('1')

        # consider every valid digit and put it in the current
        # index and recur for the next index
        while ch <= ord('9'):

            # update difference between odd and even digits
            if n & 1:
                # add value to `diff` if the digit is odd
                absdiff = diff + (ch - ord('0'))
            else:
                # subtract a value from `diff` if even
                absdiff = diff - (ch - ord('0'))

            n_sums(n - 1, result + chr(ch), absdiff)
            ch = ch + 1

    # if the number becomes n–digit with an equal sum of even and odd
    # digits, print it
    elif n == 0 and abs(diff) == 0:
        temp_list.append(result)
        print(temp_list[0])


print("\nZAD7 :")
print(n_sums(3))


# wtf version from intermarché
def combinationsRec(arr, elem, n):
    # if all elements are filled,
    # print the solution
    temp_small_list = []
    temp_big_list = [temp_small_list]
    if elem > n:
        for i in arr:
            print(i, end=" ")
        print("")  # endl
        return
        # Try all possible combinations
        # for element elem
    for i in range(0, 2 * n):
        if arr[i] == -1 and i + elem + 1 < 2 * n and arr[i + elem + 1] == -1:  # if position i and (i+elem+1) are
            # not occupied in the vector
            # place elem at position
            # i and (i+elem+1)
            arr[i] = elem
            arr[i + elem + 1] = elem

            # recurse for next element
            combinationsRec(arr, elem + 1, n)

            # backtrack (remove elem from
            # position i and (i+elem+1) )
            arr[i] = -1
            arr[i + elem + 1] = -1


def combinations(n: int) -> list[list[int]]:
    # create a vector of double
    # the size of given number with
    arr = [-1] * (2 * n)

    # all its elements initialized by 1
    elem = 1

    # start from element  1
    return combinationsRec(arr, elem, n)


n = 3
print("\nZAD8 :")
combinations(n)


def remove_duplicates(txt: str) -> str:
    if len(txt) == 0:
        return txt
    if len(txt) == 1:
        return txt
    if txt[0] == txt[1]:
        return txt[0] + remove_duplicates(txt[2:])
    else:
        return txt[0] + remove_duplicates(txt[1:])


txt_1 = "HalinkaxxRGB11"
txt_1_removed_duplicates = remove_duplicates(txt_1)
print("\nZAD8 :")
print(txt_1_removed_duplicates)


# wtf version from intermachę
def balanced_parentheses(n: int) -> str:
    str_support = [""] * 2 * n
    if n > 0:
        balanced_parentheses_support(str_support, 0, n, n/2, n/2)
    return str(str_support)


def balanced_parentheses_support(str_support, index, n, opening_brackets, closing_brackets):
    if closing_brackets == n:
        for i in str_support:
            print(i, end="")
        print()
        return
    else:
        if opening_brackets > closing_brackets:
            str_support[index] = ')'
            balanced_parentheses_support(str_support, index + 1, n, opening_brackets, closing_brackets + 1)
        if opening_brackets < n:
            str_support[index] = '('
            balanced_parentheses_support(str_support, index + 1, n, opening_brackets + 1, closing_brackets)


print("\nZAD9 :")
print("n=0: ")
n0 = 0
balanced_parentheses(n0)

print("n=1: ")
n1 = 1
balanced_parentheses(n1)

print("n=2: ")
n2 = 2
balanced_parentheses(n2)

print("n=4: ")
n4 = 4
balanced_parentheses(n4)

print("n=6: ")
n6 = 6
balanced_parentheses(n6)






