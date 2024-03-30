import random 
while eval(input('p')):print(*[('C:'+random.choice('rps')+'\nP:'+input('RPS:').lower()+'\n'+(['T\n','W\n','L\n'][((ord(random.choice('rps'))-ord('r'))%3 - (ord(input('RPS:').lower())-ord('r')))%3])) if eval(input('a(y/n):')) else exit()])
