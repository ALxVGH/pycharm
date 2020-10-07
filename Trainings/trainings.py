from random import *
A = []


def generate_list(n):
    global A
    for i in range(n):
        A.append(randint(0, 10000))


def hanoy(n, start, stop):
    """
        :param n: количество элементов
        :param start: откудва переносим
        :param stop: куда переносим
    """
    if n == 1:
        print("переместить с ", start, " на ", stop)
    else:
        temp = 6-start-stop
        hanoy(n-1, start, temp)
        hanoy(1, start, stop)
        hanoy(n-1, temp, stop)


def connect(A, B):
    """
        :param A: принимает список
        :param B: Принимает второй список
        :return:  Возвращает объединенный список, элементы которого отсортированы по возрастанию
    """
    i = 0
    j = 0
    tm = []
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            tm.append(B[j])
            j += 1
        else:
            tm.append(A[i])
            i += 1
    while i < len(A):
        tm.append(A[i])
        i += 1
    while j < len(B):
        tm.append(B[j])
        j += 1
    return tm


def rotate(a, first_index=0, second_index=1):
    a[first_index], a[second_index] = a[second_index], a[first_index]


def sort_in(A):
    """ Сортирует слиянием список А """
    if len(A) <= 1:
        return
    elif len(A) == 2:
        if A[0] > A[1]:
            rotate(A)
            #A[0], A[1] = A[1], A[0]
        return
    elif len(A) > 2:
        B = []
        C = []
        for i in range(len(A)):
            if i < len(A)/2:
                B.append(A[i])
            else:
                C.append(A[i])
        sort_in(B)
        sort_in(C)
        T = connect(B, C)
        for e in range(len(A)):
            A[e] = T[e]
        return


def h_sort(A, increment=True):
    if len(A) <= 1:
        return
    barr = A[0]
    L = []
    R = []
    M = []
    for i in range(len(A)):
        if A[i] > barr:
            R.append(A[i])
        elif A[i] < barr:
            L.append(A[i])
        else:
            M.append(A[i])
    if increment == True:
        h_sort(L)
        h_sort(R)
    else:
        h_sort(L, False)
        h_sort(R, False)
    k = 0
    if increment == True:
        for el in L+M+R:
            A[k] = el
            k += 1
    else:
        for el in R+M+L:
            A[k] = el
            k += 1


def sort_bubble(a):
    end = 1
    while len(a)-end > 0:
        for i in range(len(a)-end):
            if a[i] > a[i+1]:
                rotate(a, i, i+1)
                #a[i], a[i+1] = a[i+1], a[i]
        end += 1
    return


def check_sort(A, increment=True):
    if increment:
        word ="increment"
    else:
        word ="discrement"
    flag = True
    m = 2*int(increment)-1
    for i in range(1, len(A)):
        if m*A[i] >= m*A[i-1]:
                pass
        else:
            flag = False
            break
    if flag:
        print("list is sorted by "+word)
    else:
        print("list is unsorted by "+word)


s_array = 1000
TE = [5, 6, 11, 50, 8, 1, 19, 30, 6, 17, 82, 8, 12, 8, 1, 72, 100]
TE1 = ['Mask', 'apple', 'tree']
generate_list(s_array)
print(A)
check_sort(A)
#h_sort(A)
#sort_in(A)
sort_bubble(A)
print(A)
check_sort(A)

#hanoy(4, 1, 2)
