import os
import getpass
import secrets
import sys
import pyfiglet
from termcolor import colored
from colorama import init

init()


A = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'o', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def f(x):
  store = []
  for s in x:
    count = 0
    for i in range(36):
        if A[i].lower() == s.lower():
          store.append(i)
          count = 1
          break
    if count == 0:
      store.append(' ')
  return tuple(store)                

    
def rf(x):
    store = []
    q = ''
    for s in x:
        try:
            store.append(A[s])
        except(IndexError, TypeError):
            store.append(' ')
    q = ''.join(store)
    return q
    
def ikey(x):
    seed = list(range(36))
    masterkey = []
    for i in range(len(x)):
        masterkey.append(secrets.choice(seed))
    return tuple(masterkey)


def en(msg):
    ciphertxt = []
    x = f(msg)
    y = ikey(msg)
    for i in range(len(x)):
            if type(x[i]) is int:
                ciphertxt.append(((x[i]+y[i]) % 36))
            else:
                ciphertxt.append(' ')
    ctxt = rf(tuple(ciphertxt))
    shk = rf(y)
    return (ctxt, shk)


def de(c, k):
    ciphertxt = []
    x = f(c)
    y = f(k)
    if len(x) <= len(y):
        for i in range(len(x)):
            if type(x[i]) is int and type(y[i]) is int:
                ciphertxt.append(((x[i]-y[i]) % 36))
            else:
                ciphertxt.append(' ')
    else:
        x = input('Incorrect Input!!!\nPress any key to continue...')
        sys.exit(1)
    return rf(tuple(ciphertxt))

    
def sprocess():
    table = []
    print(colored(pyfiglet.figlet_format("Split Secret"), "yellow"))
    while 1:
        try:
            x = int(input('\nEnter the number of shares:'))
            if 1 < x < 11:
                break
        except ValueError:
            print('\nPlease enter a valid integer greater than 1 but less than or equal to 10!\n')
    msg = getpass.getpass('Enter the secret:')
    table += list(en(msg))
    for i in range(2, x):
        tmp = table[-1]
        table.pop()
        table += list(en(tmp))
    for i in range(len(table)):
        print('SHARE', i+1, ':', table[i])


def cprocess():
    table = []
    print(colored(pyfiglet.figlet_format("Combine Secret"), "yellow"))
    while 1:
        try:
            x = int(input('\nEnter no. of shares to combine:'))
            if 1 < x < 11:
                break
        except ValueError:
                print('\nPlease enter a valid integer greater than 1 but less than or equal to 10!\n')
    for i in range(x):
            table.append(getpass.getpass(str('Enter Share '+str(i+1)+':')))
    for i in range(x-1):
            hook = []
            a, b = table[-2], table[-1]
            table.pop()
            table.pop()
            hook.append(de(a, b))
            table += hook
    print()
    print("Original text is")
    print(colored(pyfiglet.figlet_format("".join(table)), "green"))
        

def mm():
   print(colored(pyfiglet.figlet_format("Welcome to Share Chat"), "yellow"))
   print('\n1) Split a secret into codes.')
   print('2) Combine codes to recover secret.')
   print('3) "exit" for quiting the program.')
   cmd = input('\nEnter command:')
   if cmd == '1':
       sprocess()
       mm()
   elif cmd == '2':
       cprocess()
       mm()
   elif cmd.lower() == 'c' or cmd.lower() == 'close':
      sys.exit()
   elif cmd.lower() == "exit":
      sys.exit()
   else:
      print('please enter 1 or 2 or \'c to exit!')
      mm()


mm()
