#!/usr/bin/env python

import random

def random_funct():

 # 64 random hexadecimal characters (0-9 and A-F)
 char = 'F696283D000F2102ABB8DB915EAA847E7536E74B2173D5C10F3594AB31CF226C' 

 length_object = raw_input('Choose your length password :')
 length_object = int(length_object)

 for b in range(15):
  password = ''

  for h in range(length_object):
   password += random.choice(char)

  print(password)

def main():

 random_funct()

main()
