## 1. Jupyter console ##

/home/dq$ ipython

In [1]: print(10)
10
In [2]: exit

## 2. Getting help ##

/home/dq$ ipython
In [1]: dq?
In [2]: help(dq)
In [3]: help()
In [4]: exit

## 3. Persistent sessions ##

/home/dq$ ipython
In [1]: dq = 5
In [2]: dq_10 = dq * 10
In [3]: exit

## 4. Jupyter magics ##

/home/dq$ touch script.py
/home/dq$ nano script.py
  x = 5
  print(x)
/home/dq$ ipython
In [1]: %run script.py
In [2]: %who
In [3]: exit


## 5. Accessing the shell ##

/home/dq$ ipython
In [1]: !ls
In [2]: exit

## 6. Pasting in code ##

/home/dq$ ipython

%cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:for i in range(10):
:    if i < 5:
:        print(i)
:    else:
:        print(i * 2)
