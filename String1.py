Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 1. 큰따옴표(")로 양쪽 둘러싸기
>>> # 2. 작은따옴표(')로 양쪽 둘러싸기
>>> # 3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
>>> # 4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
>>> 
>>> # 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
>>> food = "Python's favorite food is perl"
>>> food
"Python's favorite food is perl"
>>> food = 'Python's favorite food is perl'
SyntaxError: invalid syntax
>>> say = '"Python is very easy." he says.'
>>> print(say)
"Python is very easy." he says.
>>> food = 'Python\'s favorite food is perl'
>>> print(food)
Python's favorite food is perl
>>> say = "\"Python is very easy.\" he says."
>>> print(say)
"Python is very easy." he says.
>>> 
>>> # 여러 줄인 문자열을 변수에 대입하고 싶을 때
>>> multiline = "Life is too short\nYou need python"
>>> print(multiline)
Life is too short
You need python
>>> multiline = '''
...Life is too short
...You need python
...'''
>>> print(multiline)

...Life is too short
...You need python
...
>>> multiline = """
...Life is too short
...You need python
..."""
>>> print(multiline)

...Life is too short
...You need python
...
>>> 
>>> #문자열 연산하기
>>> head = "Python"
>>> tail = " is fun!"
>>> head + tail
'Python is fun!'
>>> a = "python"
>>> a * 2
'pythonpython'
>>> a = "Life is too short"
>>> len(a)
17
>>> 
>>> #문자열 인덱싱과 슬라이싱
>>> a = "Life is too short, You need python"
>>> a[3]
'e'
>>> a[0]
'L'
>>> a[12]
's'
>>> a[-1]
'n'
>>> a[-0]
'L'
>>> a[-2]
'o'
>>> a[-5]
'y'
>>> a = "Life is too short, You need python"
>>> b = a[0] + a[1] + a[2] + a[3]
>>> b
'Life'
>>> a[0:4]
'Life'
>>> a[0:3]
'Lif'
>>> a[0:5]
'Life '
>>> a[0:2]
'Li'
>>> a[5:7]
'is'
>>> a[12:17]
'short'
>>> a[19:] # a[시작번호:끝번호]에서 끝 번호 생략
'You need python'
>>> a[:17] # a[시작번호:끝번호]에서 시작 번호 생략
'Life is too short'
>>> a[:] # a[시작번호:끝번호]에서 시작 번호와 끝 번호 생략
'Life is too short, You need python'
>>> a[19:-7]
'You need'
>>> a = "20010331Rainy"
>>> date = a[:8]
>>> weather = a[8:]
>>> date
'20010331'
>>> weather
'Rainy'
>>> a = "20010331Rainy"
>>> year = a[:4]
>>> day = a[4:8]
>>> weather = a[8:]
>>> year
'2001'
>>> day
'0331'
>>> weather
'Rainy'
>>> 
>>> #Pithon 문자열을 Python으로 바꾸려면?
>>> a = "Pithon"
>>> a[1]
'i'
>>> a[1] = 'y'
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a[1] = 'y'
TypeError: 'str' object does not support item assignment
>>> a = "Pithon"
>>> a[:1]
'P'
>>> a[2:]
'thon'
>>> a[:1] + 'y' + a[2:]
'Python'
>>> 
>>> #문자열 포매팅
>>> "I eat %d apples." % 3
'I eat 3 apples.'
>>> "I eat %s apples." % "five"
'I eat five apples.'
>>> number = 3
>>> "I eat %d apples." % number
'I eat 3 apples.'
>>> number = 10
>>> day = "three"
>>> "I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'
>>> "I have %s apples" % 3
'I have 3 apples'
>>> "rate is %s" % 3.234
'rate is 3.234'
>>> 
>>> #포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
>>> "Error is %d%." % 98
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    "Error is %d%." % 98
ValueError: incomplete format
>>> "Error is %d%%." % 98
'Error is 98%.'
>>> 
>>> "%10s" % "hi"
'        hi'
>>> "%-10sjane" % 'hi'
'hi        jane'
>>> "%0.4f" % 3.42134234
'3.4213'
>>> "%10.4f" % 3.42134234
'    3.4213'
>>> "I eat {0} apples".format(3)
'I eat 3 apples'
>>> "I eat {0} apples".format("five")
'I eat five apples'
>>> number = 3
>>> "I eat {0} apples".format(number)
'I eat 3 apples'
>>> number = 10
>>> day = "three"
>>> "I ate {0} apples. so I was sick for {1} days.".format(number, day)
'I ate 10 apples. so I was sick for three days.'
>>> "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
'I ate 10 apples. so I was sick for 3 days.'
>>> "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
'I ate 10 apples. so I was sick for 3 days.'
>>> "{0:<10}".format("hi")
'hi        '
>>> "{0:>10}".format("hi")
'        hi'
>>> "{0:^10}".format("hi")
'    hi    '
>>> "{0:=^10}".format("hi")
'====hi===='
>>> "{0:!<10}".format("hi")
'hi!!!!!!!!'
>>> y = 3.42134234
>>> "{0:0.4f}".format(y)
'3.4213'
>>> "{0:10.4f}".format(y)
'    3.4213'
>>> "{{ and }}".format()
'{ and }'