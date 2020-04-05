#!/usr/bin/env python3
import argparse, re

def alternatives(ip):
    print('Other ways to write {} are listed below:\n'.format(ip))
    for octates in re.finditer(r'((?P<a>\d+)\.)((?P<b>\d+)\.)((?P<c>\d+)\.)(?P<d>\d+)', ip):
    	print(str(int(octates.group('a'))) + '.' + str(int(octates.group('b'))*256**2 + int(octates.group('c'))*256 + int(octates.group('d'))))
    	
    	print(str(int(octates.group('a'))) + '.' + str(int(octates.group('b'))) + '.' + str(int(octates.group('c'))*256 + int(octates.group('d'))))
    	
    	print(octates.group('a')+'.' + str(hex(int(octates.group('b'))))+'.' + str(hex(int(octates.group('c'))))+'.' + str(hex(int(octates.group('d')))))
    	
    	print(octates.group('a')+'.'+octates.group('b')+'.' + str(hex(int(octates.group('c'))))+'.' + str(hex(int(octates.group('d')))))
    	
    	print(octates.group('a')+'.'+octates.group('b')+'.' + octates.group('c')+'.'+str(hex(int(octates.group('d')))))
    	
    	print(re.sub('o', '', octates.group('a')+'.' + str(oct(int(octates.group('b'))))+'.' + str(oct(int(octates.group('c'))))+'.' + str(oct(int(octates.group('d'))))))
    	
    	print(re.sub('o', '', octates.group('a')+'.' + octates.group('b')+'.'+str(oct(int(octates.group('c'))))+'.' + str(oct(int(octates.group('d'))))))
    	
    	print(re.sub('o', '', octates.group('a')+'.' + octates.group('b')+'.'+octates.group('c')+'.' + str(oct(int(octates.group('d'))))))
    	
    	print(str(int(octates.group('a'))*256**3 + int(octates.group('b'))*256**2 + int(octates.group('c'))*256 + int(octates.group('d'))))
    	
    	print(str(hex(int(octates.group('a'))*256**3 + int(octates.group('b'))*256**2 + int(octates.group('c'))*256 + int(octates.group('d')))))
    	
    	print(str(hex(int(octates.group('a'))))+'.' + re.sub('o', '', str(oct(int(octates.group('b')))))+'.' + str(int(octates.group('c'))*256+int(octates.group('d'))))
    	
    	print(str(hex(int(octates.group('a'))))+'.' + str(hex(int(octates.group('b'))))+'.' + str(hex(int(octates.group('c'))))+'.' + str(hex(int(octates.group('d')))))
    	
    	print(str(hex(int(octates.group('a'))))+'.' + str(hex(int(octates.group('b'))))+'.' + str(hex(int(octates.group('c'))))+'.'+octates.group('d'))
    	
    	print(str(hex(int(octates.group('a'))))+'.' + str(hex(int(octates.group('b'))))+'.' + octates.group('c')+'.'+octates.group('d'))
    	
    	print(str(hex(int(octates.group('a'))))+'.' + octates.group('b')+'.'+octates.group('c')+'.'+octates.group('d'))
    	
    	print(str(hex(int(octates.group('a'))))+'.' + str(hex(int(octates.group('b'))))+'.'+str(int(octates.group('c')) * 256+int(octates.group('d'))))
    	
    	print(str(hex(int(octates.group('a'))))+'.' + str(int(octates.group('b'))*256**2+int(octates.group('c'))*256 + int(octates.group('d'))))
    	
    	print(re.sub('x', 'x00000000', str(hex(int(octates.group('a'))))+'.' + str(hex(int(octates.group('b'))))+'.' + str(hex(int(octates.group('c'))))+'.' + str(hex(int(octates.group('d'))))))
    	
    	print(re.sub('o', '', str(oct(int(octates.group('a')) * 256**3+int(octates.group('b'))*256**2 + int(octates.group('c'))*256 + int(octates.group('d'))))))
    	
    	print(re.sub('o', '', str(oct(int(octates.group('a')))) + '.'+str(oct(int(octates.group('b'))))+'.' + str(oct(int(octates.group('c'))))+'.' + str(oct(int(octates.group('d'))))))
    	
    	print(re.sub('o', '', str(oct(int(octates.group('a')))) + '.'+str(oct(int(octates.group('b'))))+'.' + str(oct(int(octates.group('c'))))+'.'+octates.group('d')))
    	
    	print(re.sub('o', '', str(oct(int(octates.group('a')))) + '.'+str(oct(int(octates.group('b'))))+'.' + octates.group('c')+'.'+octates.group('d')))
    	
    	print(re.sub('o', '', str(oct(int(octates.group('a')))) + '.'+octates.group('b')+'.'+octates.group('c')+'.'+octates.group('d')))
    	
    	print(re.sub('o', '', str(oct(int(octates.group('a')))) + '.'+str(oct(int(octates.group('b')))))+'.' + str(int(octates.group('c'))*256+int(octates.group('d'))))
    	
    	print(re.sub('o', '', str(oct(int(octates.group('a'))))) + '.'+str(int(octates.group('b'))*256**2+int(octates.group('c'))*256 + int(octates.group('d'))))
    	
    	print(re.sub('o', '', str(oct(int(octates.group('a'))))) + '.'+str(hex(int(octates.group('b'))))+'.' + str(int(octates.group('c'))*256+int(octates.group('d'))))
    	
    	print(re.sub('o', '0000000', str(oct(int(octates.group('a'))))+'.' + str(oct(int(octates.group('b'))))+'.' + str(oct(int(octates.group('c'))))+'.' + str(oct(int(octates.group('d'))))))
    	

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='ip', help='Valid IPv4 Address (e.g. \'192.168.56.101\')')
    args = parser.parse_args()
    if args.ip:
        alternatives(args.ip)
    else:
        parser.print_help()
