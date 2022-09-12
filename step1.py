
import bit

y = 22416810028847082123
last = 194087394801004738104
profit='out3.txt'
def func(y2):
        k = bit.PrivateKey.from_int(y2)
        with open(profit,'a') as out:
               out.write('{}\n'.format(k.address))
while y<last:
        y +=1
        func(y)


