import flask
from array import array
from itertools import count
import random
import threading

import flask
from array import array
from concurrent.futures import process
from itertools import count
import random
from threading import Thread
import threading
import glob
from google.cloud.storage import Blob
from google.cloud import storage
from os import path, environ

#Generate list with random unique numbers
lst = random.sample(range(0, 100000), 100000)

g1 = []
g2 = []
g3 = []
g4 = []
g5 = []
g6 = []
g7 = []
g8 = []
g9 = []
g10 = []

#split the list in three files
def split_list(list):
    while list:
            for x in list:
                if x < 10000:
                    g1.append(x)
                    list.remove(x)
                elif 10000 <= x < 20000:
                    g2.append(x)
                    list.remove(x)
                elif 20000 <= x < 30000:
                    g3.append(x)
                    list.remove(x)
                elif 30000 <= x < 40000:
                    g4.append(x)
                    list.remove(x)
                elif 40000 <= x < 50000:
                    g5.append(x)
                    list.remove(x)
                elif 50000 <= x < 60000:
                    g6.append(x)
                    list.remove(x)
                elif 60000 <= x < 70000:
                    g7.append(x)
                    list.remove(x)
                elif 70000 <= x < 80000:
                    g8.append(x)
                    list.remove(x)
                elif 80000 <= x < 90000:
                    g9.append(x)
                    list.remove(x)
                else:
                    g10.append(x)
                    list.remove(x)
    with open("/tmp/f1.txt", mode = "w") as f1:
        f1.write(str(g1))
        f1.close()
    with open("/tmp/f2.txt", mode = "w") as f2:
        f2.write(str(g2))
        f2.close()
    with open("/tmp/f3.txt", mode = "w") as f3:
        f3.write(str(g3))
        f3.close()
    with open("/tmp/f4.txt", mode = "w") as f4:
        f4.write(str(g4))
        f4.close()
    with open("/tmp/f5.txt", mode = "w") as f5:
        f5.write(str(g5))
        f5.close()
    with open("/tmp/f6.txt", mode = "w") as f6:
        f6.write(str(g6))
        f6.close()
    with open("/tmp/f7.txt", mode = "w") as f7:
        f7.write(str(g7))
        f7.close()
    with open("/tmp/f8.txt", mode = "w") as f8:
        f8.write(str(g8))
        f8.close()
    with open("/tmp/f9.txt", mode = "w") as f9:
        f9.write(str(g9))
        f9.close()
    with open("/tmp/f10.txt", mode = "w") as f10:
        f10.write(str(g10))
        f10.close()

split_list(lst)

#order numbers from file f1.txt and write them in f11.txt
def read_f1(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f1.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f11.txt", mode = "w") as f11:
        f11.write(str(new_b) + ', ')
        f11.close()

#read_f1('/tmp/f1.txt')

#order numbers from file f1.txt and write them in f21.txt
def read_f2(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f2.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f21.txt", mode = "w") as f21:
        f21.write(str(new_b) + ', ')
        f21.close()

#read_f2('/tmp/f2.txt')

#order numbers from file f1.txt and write them in f31.txt
def read_f3(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f3.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f31.txt", mode = "w") as f31:
        f31.write(str(new_b))
        f31.close()

#read_f3('/tmp/f3.txt')

#order numbers from file f1.txt and write them in f41.txt
def read_f4(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f4.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f41.txt", mode = "w") as f41:
        f41.write(str(new_b))
        f41.close()

#read_f4('/tmp/f4.txt')

#order numbers from file f1.txt and write them in f51.txt
def read_f5(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f5.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f51.txt", mode = "w") as f51:
        f51.write(str(new_b))
        f51.close()

#read_f5('/tmp/f5.txt')

#order numbers from file f1.txt and write them in f61.txt
def read_f6(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f6.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f61.txt", mode = "w") as f61:
        f61.write(str(new_b))
        f61.close()

#read_f6('/tmp/f6.txt')

#order numbers from file f1.txt and write them in f71.txt
def read_f7(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f7.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f71.txt", mode = "w") as f71:
        f71.write(str(new_b))
        f71.close()

#read_f7('/tmp/f7.txt')

#order numbers from file f1.txt and write them in f81.txt
def read_f8(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f8.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f81.txt", mode = "w") as f81:
        f81.write(str(new_b))
        f81.close()

#read_f8('/tmp/f8.txt')

#order numbers from file f1.txt and write them in f91.txt
def read_f9(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f9.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f91.txt", mode = "w") as f91:
        f91.write(str(new_b))
        f91.close()

#read_f9('/tmp/f9.txt')

#order numbers from file f1.txt and write them in f101.txt
def read_f10(filereadf1):
    a = []
    new_a = []
    with open('/tmp/f10.txt', 'r+') as fileR:
        a = fileR.read()
        a = str(a)[1:-1]
        a = a.split(',')
        a = [int(i) for i in a]
        fileR.close()
        while a:
            min = a[0]
            for x in a:
                if x < min:
                    min = x
            new_a.append(min)
            a.remove(min)
    new_b=str(new_a)[1:-1]
    with open("/tmp/f101.txt", mode = "w") as f101:
        f101.write(str(new_b))
        f101.close()

#read_f10('/tmp/f10.txt')

#Run the functions
threading.Thread(target=read_f1('/tmp/f1.txt')).start()
threading.Thread(target=read_f2('/tmp/f2.txt')).start()
threading.Thread(target=read_f3('/tmp/f3.txt')).start()
threading.Thread(target=read_f4('/tmp/f4.txt')).start()
threading.Thread(target=read_f5('/tmp/f5.txt')).start()
threading.Thread(target=read_f6('/tmp/f6.txt')).start()
threading.Thread(target=read_f7('/tmp/f7.txt')).start()
threading.Thread(target=read_f8('/tmp/f8.txt')).start()
threading.Thread(target=read_f9('/tmp/f9.txt')).start()
threading.Thread(target=read_f10('/tmp/f10.txt')).start()


#joining files
def joiningfiles():
    with open("/tmp/f11.txt", 'r+') as fileR1:
        a = str(fileR1.read())
        fileR1.close()
    with open("/tmp/f21.txt", 'r+') as fileR2:
        b = str(fileR2.read())
        fileR2.close()
    with open("/tmp/f31.txt", 'r+') as fileR3:
        c = str(fileR3.read())
        fileR3.close()
    with open("/tmp/f41.txt", 'r+') as fileR4:
        d = str(fileR4.read())
        fileR4.close()
    with open("/tmp/f51.txt", 'r+') as fileR5:
        e = str(fileR5.read())
        fileR5.close()
    with open("/tmp/f61.txt", 'r+') as fileR6:
        f = str(fileR6.read())
        fileR6.close()
    with open("/tmp/f71.txt", 'r+') as fileR7:
        q = str(fileR7.read())
        fileR7.close()
    with open("/tmp/f81.txt", 'r+') as fileR8:
        h = str(fileR8.read())
        fileR8.close()
    with open("/tmp/f91.txt", 'r+') as fileR9:
        i = str(fileR9.read())
        fileR9.close()
    with open("/tmp/f101.txt", 'r+') as fileR10:
        j = str(fileR10.read())
        fileR10.close()
    k = [a, b, c, d, e, f, q, h, i, j]
    l = "".join(k)
    with open("/tmp/final.txt", mode = "w") as f111:
        f111.write(l)
        f111.close()
joiningfiles()

app = flask.Flask(__name__)

@app.get("/")

def hello():
#printing results on screen
    with open("/tmp/final.txt", 'r+') as filefinal:
        f = str(filefinal.read())
        filefinal.close()
    return f    

if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)