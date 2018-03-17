import os
import re
from threading import Thread

def run_threads(filename,module_name, c):
    obj = re.split(r'[\\]', filename)[-1:]
    with open(filename, "r") as f:
        for line in f.readlines():
            if module_name in line:
                c += 1
    if c == 1:
        print "Found in {} \n".format(filename)
    else:
        print "{} modules has same name in {} \n".format(c, "".join(obj))
    

Dir = "C:\Users\sanjay\PycharmProjects\Find_module"
order = "{}\order.txt".format(Dir)
register = "C:\Users\sanjay\PycharmProjects\Find_module\Register.txt"
mnm = "{}\mnm.txt".format(Dir)
c = 0
ans = raw_input("Enter module name : ")

thread = Thread(target = run_threads, args = (order, ans, c))
thread2 = Thread(target = run_threads, args = (register, ans, c))
thread3 = Thread(target = run_threads, args = (mnm, ans, c))
thread.start()
thread2.start()
thread3.start()
thread.join()
#print "order completed"
thread.join()
#print "Register completed"
thread.join()
#print "mnm completed"
