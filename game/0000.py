__author__ = 'sherry'

import random
import string
import MySQLdb

chars = string.ascii_letters + string.digits

def getrandom():
    L = []
    for i in range(4):
        str = string.join(random.sample(chars,4))
        code =  str.upper()
        s = code.replace(' ','')
        L.append(s)
    return L

def concatenate():
    return "-".join(getrandom())

def generate(n):
    code = [concatenate() for i in range(n)]
    return list(set(code))

# conn =  MySQLdb.connect(
#         host = 'hg014',
#         prot = '3306',
#         user = 'huangxt',
#         passwd = '123456',
#         db = 'hxt',
# )
#
# cur = conn.cursor()
if __name__ == '__main__':
    print generate(100)

help(random.choice)