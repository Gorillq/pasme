import sys
import time
import random
import string

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("Time = ", current_time)
c = {"!", "?", "%", "@", "#", "$"}
characters = string.ascii_letters + string.digits + '!' + '?' + '%' + '@' + '$' + '*' + '=' + '+'
a = input("Generate Password? Y/N \n")
def mypas():
    passq = ''.join(random.choice(characters) for i in range(12))
    print('Random password: ', passq)
    time.sleep(5)
    b = input("Try Again? Y/N: \n")
    if b == "N" or b == 'n':
        exit()
    else:
        return
while a == "Y" or a == 'y':
    mypas()
else:
    exit()
