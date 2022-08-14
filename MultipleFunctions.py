from array import array
from concurrent.futures import process
from itertools import count
import random
from threading import Thread
import threading
import glob

#Generate list with random unique numbers
lst = random.sample(range(0, 100), 100)

new_low = []
new_high = []
mid = []

#split the list in three files
def split_list(list):
    while list:
            for x in list:
                if x < 33:
                    new_low.append(x)
                    list.remove(x)
                elif 33 <= x < 66:
                    new_high.append(x)
                    list.remove(x)
                else:
                    mid.append(x)
                    list.remove(x)
    #print(new_low)
    #print(new_high)
    #print(mid)
    with open("source/f1.txt", mode = "w") as f1:
        f1.write(str(new_low))
    with open("source/f2.txt", mode = "w") as f2:
        f2.write(str(new_high))
    with open("source/f3.txt", mode = "w") as f3:
        f3.write(str(mid))

    print('done')
    print(list)

split_list(lst)

#order numbers from file f1.txt and write them in f11.txt
def read_f1(filereadf1):
    a = []
    new_a = []
    with open('source/f1.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
        print(new_a)
    length2 = str(len(new_a))
    new_b=str(new_a)[1:-1]
    print("Length is " + length2)
    with open("f11.txt", mode = "w") as f11:
        f11.write(str(new_b) + ', ')

#read_f1('source/f1.txt')

#order numbers from file f2.txt and write them in f21.txt
def read_f2(filereadf2):
    a = []
    new_a = []
    with open('source/f2.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
        print(new_a)
    print(a)
    length2 = str(len(new_a))
    new_b=str(new_a)[1:-1]
    print("Length is " + length2)
    with open("f21.txt", mode = "w") as f21:
        f21.write(str(new_b) + ', ')

#read_f2('source/f2.txt')

#order numbers from file f3.txt and write them in f31.txt
def read_f3(filereadf3):
    a = []
    new_a = []
    with open(filereadf3, 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
        print(new_a)
    print(a)
    length2 = str(len(new_a))
    new_b=str(new_a)[1:-1]
    print("Length is " + length2)
    with open("f31.txt", mode = "w") as f31:
        f31.write(str(new_b))

#read_f3('source/f3.txt')

#Run the functions in parallel
threading.Thread(target=read_f1('source/f1.txt')).start()
threading.Thread(target=read_f2('source/f2.txt')).start()
threading.Thread(target=read_f3('source/f3.txt')).start()

#Combine contents from files
read_files = glob.glob('*.txt')

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())


