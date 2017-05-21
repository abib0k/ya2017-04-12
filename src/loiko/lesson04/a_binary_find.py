import os

task='''
В первой строке источника данных даны:
        - целое число 1<=n<=100000 (размер массива)
        - сам массив A[1...n] из n различных натуральных чисел,
          не превышающих 1E9, в порядке возрастания,
Во второй строке
        - целое число 1<=k<=10000 (сколько чисел нужно найти)
        - k натуральных чисел b1,...,bk не превышающих 10E9 (сами числа)
Для каждого i от 1 до kk необходимо вывести индекс 1<=j<=n,
для которого A[j]=bi, или -1, если такого j нет.

        Sample Input:
        5 1 5 8 12 13
        5 8 1 23 1 11

        Sample Output:
        3 1 -1 1 -1

(!) Обратите внимание на смещение начала индекса массивов относительно условий задачи
'''


def binaryFind(array, value):
    index=None
    # ваше решение
    l=0
    r=len(array)-1
    while l<=r:
        c=(l+r)//2
        if array[c]==value:
            return c+1
        elif array[c]>value:
            r=c-1
        else:
            l=c+1
    return -1


def main():
    fn = os.path.dirname(os.path.abspath(__file__)) + "/dataA.txt"
    f=open(fn)
    s1=f.readline().replace("\n","").split(" ")
    s2=f.readline().replace("\n","").split(" ")
    size=int(s1[0])
    array=[]
    values=[]
    for i in range(0,size):
        array.append(int(s1[i+1]))
        values.append(int(s2[i+1]))
    res=[]
    print(" array=",array)
    print("values=",values)
    for value in values:
        index = binaryFind(array,value)
        res.append(index)
    print(" index=",res)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
