## 1. Adding and appending ##

/home/dq$ echo "99 bottles of beer on the wall..." > beer.txt
/home/dq$ echo "Take one down, pass it around, 98 bottles of beer o
n the wall..." >> beer.txt

## 2. Sorting and sorting in reverse ##

/home/dq$ sort < beer.txt
99 bottles of beer on the wall...
Take one down, pass it around, 98 bottles of beer on the wall...
/home/dq$ sort -r < beer.txt
Take one down, pass it around, 98 bottles of beer on the wall...
99 bottles of beer on the wall...

## 3. Creating text file coffee.txt. Adding and appending strings ##

/home/dq$ touch coffee.txt
/home/dq$ echo "Coffee is almost as good as beer," > coffee.txt
/home/dq$ echo "But I could never drink 99 bottles of it" >> coffee
.txt

## 4. Using grep command ##

/home/dq$ grep "bottles of" beer.txt coffee.txt
beer.txt:99 bottles of beer on the wall...
beer.txt:Take one down, pass it around, 98 bottles of beer on the w
all...
coffee.txt:But I could never drink 99 bottles of it

## 5. Special characters and star wildcard ##

/home/dq$ touch beer1.txt
/home/dq$ touch beer2.txt
/home/dq$ grep "beer" beer?.txt
/home/dq$ grep "beer" *.txt
beer.txt:99 bottles of beer on the wall...
beer.txt:Take one down, pass it around, 98 bottles of beer on the w
all...
coffee.txt:Coffee is almost as good as beer,

## 6. Piping output ##

/home/dq$ touch python.py
/home/dq$ nano python.py

  """import random
  for i in range(100):
    print(random.randint(1,5))"""

/home/dq$ tail -n 4 python.py | grep 4
/home/dq$ python python.py | grep 4

## 7. Chaining commands ##

/home/dq$ echo "Added line" >> beer.txt && cat beer.txt
99 bottles of beer on the wall...
Take one down, pass it around, 98 bottles of beer on the wall...
Added line
