import time
import sys
import bit
from bit import Key

from bit.crypto import ECPrivateKey, ripemd160_sha256

profit='C:\\bitgen\\out2.txt'
y=22416810028847082123
def func(y):
        k = bit.PrivateKey.from_int(y)
        prvkey = ECPrivateKey.from_int(y)
        hexprvkey = k.to_hex()
        with open(profit,'a') as out:
                out.write('{},{}\n'.format(y, k.address))

while True:
        func(y)
        y +=1
