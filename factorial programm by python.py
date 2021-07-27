Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def factorial(n):
	final=1
	for i in range(1,n+1):
		final*=i
	return final

>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(2)
2
>>> factorial(3)
6
>>> factorial(4)
24
>>> factorial(5)
120
>>> factorial(6)
720
>>> factorial(7)
5040
>>> factorial(8)
40320
>>> factorial(9)
362880
>>> factorial(10)
3628800
>>> 