Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = '홍길동'
>>> age = 30
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
>>> age = 30
>>> f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'
>>> d = {'name':'홍길동', 'age':30}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
>>> f'{"hi":<10}'
'hi        '
>>> f'{"hi":>10}'
'        hi'
>>> f'{"hi":^10}'
'    hi    '
>>> f'{"hi":=^10}'
'====hi===='
>>> f'{"hi":!<10}'
'hi!!!!!!!!'
>>> y = 3.42134234
>>> f'{y:0.4f}'
'3.4213'
>>> f'{y:10.4f}'
'    3.4213'
>>> f'{{ and }}'
'{ and }'
>>> # 연습문제
>>> f'{"python":!^12}'
'!!!python!!!'
>>> "{0:!^12}".format('python')
'!!!python!!!'
>>> 
>>> # 문자열 관련 함수
>>> a = "hobby"
>>> a.count('b')
2
>>> a = "Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
-1
>>> a = "Life is too short"
>>> a.index('t')
8
>>> a.index('k')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.index('k')
ValueError: substring not found
>>> ",".join('abcd')
'a,b,c,d'
>>> ",".join(['a', 'b', 'c', 'd'])
'a,b,c,d'
>>> a = "hi"
>>> a.upper()
'HI'
>>> a = "HI"
>>> a.lower()
'hi'
>>> a = " hi "
>>> a.lstrip()
'hi '
>>> a = " hi "
>>> a.rstrip()
' hi'
>>> a = " hi "
>>> a.strip()
'hi'
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':')
['a', 'b', 'c', 'd']
>>> 