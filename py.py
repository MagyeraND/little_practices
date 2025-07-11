#!/usr/bin/env python3

leng= int(input('enter the length: '))
wid = int(input('enter the width: '))
per = leng + wid
print("the per is ",per, "cm")

if leng==wid:
	print('a square')
elif leng>wid:
	print('a rectangle')
else:
    print('go back and learn geometry')
	
#dont use linux terminals for python scripting its not worth it use it for shell scripting maybe	
