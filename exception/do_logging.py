'''
Created on Sep 9, 2016

@author: sheldonshen
'''
#logging
import logging
logging.basicConfig(level=logging.INFO)
s="1"
n=int(s)
logging.info("n=%d" %n)
print(10/n)

import pdb 
s="0"
n=int(s)
pdb.set_trace()
print(10/n)
