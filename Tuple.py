Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t1 = ()
>>> t2 = (1,)
>>> t3 = (1,2,3)
>>> t4 = 1, 2, 3
>>> t5 = ('a', 'b', ('ab', 'cd'))
>>> 
>>> #1. 튜플 요솟값을 삭제하려 할 때
>>> t1 = (1, 2, 'a', 'b')
>>> del t1[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    del t1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> #2. 튜플 요솟값을 변경하려 할 때
>>> t1 = (1, 2, 'a', 'b')
>>> t1[0] = 'c'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t1[0] = 'c'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # 튜플 다루기
>>> #1. 인덱싱하기
>>> t1 = (1, 2, 'a', 'b')
>>> t1[0]
1
>>> t1[3]
'b'
>>> #2. 슬라이싱하기
>>> t1 = (1, 2, 'a', 'b')
>>> t1[1:]
(2, 'a', 'b')
>>> #3. 튜플 더하기
>>> t2 = (3, 4)
>>> t1 + t2
(1, 2, 'a', 'b', 3, 4)
>>> 
>>> #4. 튜플 곱하기
>>> t2 * 3
(3, 4, 3, 4, 3, 4)
>>> #5. 튜플 길이 구하기
>>> t1 = (1, 2, 'a', 'b')
>>> len(t1)
4
>>> 
>>> #연습문제
>>> a = (1,2,3)
>>> a+(4,)
(1, 2, 3, 4)
>>> 