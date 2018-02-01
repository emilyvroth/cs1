
def fib(n):
	if n <= 1:
		return n
	else: 
		l = [0, 1]
		for i in range(2, n+1):
			l.append(l[i-1]+l[i-2])
		num = l.pop()	
		return num

if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
