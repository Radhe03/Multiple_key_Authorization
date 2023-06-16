import os
import getpass
import secrets
import sys
import pyfiglet
from termcolor import colored
from colorama import init

init()


A = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'o', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


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

def mm():
   print(colored(pyfiglet.figlet_format(" MKA"), font = "doh"))
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

res= pyfiglet.figlet_format("Welcome to MKA",font = "doh")   
# Printing the result in the output  
print('The input text is printed in the default format will look as follow: ')  
print(res)  