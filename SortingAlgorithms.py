import random as rd
import SortingAnimation

def bubblesort(win, t):
    for i in range(len(t) - 1):
        for j in range(len(t) - 1 - i):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                SortingAnimation.draw(win, t, len(t), {j: (255, 0, 0)}, True)

def insertionsort(win, t):
    for i in range(len(t)):
        j = i
        while j > 0 and t[j] < t[j - 1]:
            t[j], t[j - 1] = t[j - 1], t[j]
            j -= 1
            SortingAnimation.draw(win, t, len(t), {j: (255, 0, 0), i: (255, 255, 255)}, True)

def selectionsort(win, t):
    for i in range(len(t)):
        ind = i
        for j in range(i + 1, len(t)):
            if t[j] < t[ind]:
                ind = j
            SortingAnimation.draw(win, t, len(t), {j: (255, 0, 0), i-1: (255, 255, 255)}, True)
        t[i], t[ind] = t[ind], t[i]

def quicksort(win, t, l, r):
    if l < r:
        j = l
        i = l - 1
        piv = rd.randint(l, r)
        t[piv], t[r] = t[r], t[piv]
        x = t[r]
        while j <= r:
            if t[j] <= x:
                i += 1
                t[i], t[j] = t[j], t[i]
            j += 1
            SortingAnimation.draw(win, t, len(t), {j: (255, 0, 0), i: (255, 255, 255)}, True)
        quicksort(win, t, l, i - 1)
        quicksort(win, t, i + 1, r)


def heapify(win, t, size, i, vis):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < size and t[l] > t[largest]:
        largest = l

    if r < size and t[r] > t[largest]:
        largest = r

    if largest != i:
        t[i], t[largest] = t[largest], t[i]
        heapify(win, t, size, largest, vis)

    if vis:
        SortingAnimation.draw(win, t, size, {i: (255, 0, 0)}, True)

def heapsort(win, t, size):
    for i in range(size // 2 - 1, -1, -1):
        heapify(win, t, size, i, 1)

    for i in range(size - 1, 0, -1):
        t[0], t[i] = t[i], t[0]
        heapify(win, t, i, 0, 0)
        SortingAnimation.draw(win, t, size, {i: (255, 255, 255)}, True)

def randomize(t, size):
    for i in range(size):
        t[i] = i
    rd.shuffle(t)