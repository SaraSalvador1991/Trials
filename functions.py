import numpy


def fun_Prime(x):
    flag = False

    if x == 1:
        print(x, "is not a prime number")
    elif x > 1:
        for i in range(2, x):
            print(i)
            if (x % i) == 0:
                flag = True
                break

        if flag:
            print(x, "is not a prime number")
        else:
            print(x, "is a prime number")


def sgn(x):
    if x>0:
        print('{0} is a positive number'.format(x))
    elif x==0:
        print('{0} is the number zero'.format(x))
    else:
        print('{0} is a negative number'.format(x))



def Fibonacci(n):
    fib = [0] * n
    fib[0] = 0  # first component (INDEX 0)
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]

    print(fib)


def transpose(X):

  r=len((X)) # rows
  c=len((X[0])) # cols
  import numpy as np
  t = np.empty((c,r))
  for i in range(c):
      for j in range(r):
          t[i][j]=X[j][i]

  print(t)






