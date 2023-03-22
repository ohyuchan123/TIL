# Python 문법 정리
> 기본적인 python 문법에 관해서 정리하였습니다  
> 변수란? ~ 리스트
## 자료형
> 문자의 값을  
> 숫자로 인식 할 지  
> 문자로 인식할 지  
> 구분할 수 있게 해줌  
>
> 컴퓨터는 사람 처럼  
> 문자인지 숫자인지 바로 알 수 없음

- 숫자 
- 문자열
- 불 : 참,거짓을 나타내는 자료형
- 변수
- 리스트
- 튜플
- 딕셔너리
- 집합 

```
자료에 대한 타입 : 숫자,문자열,불
어떤 값을 담는 자료구조 : 변수,리스트,튜플,딕셔너리,집합
```

## Hello Wolrd

```python
print("Hello World")
```

## 변수
- 어떤 값을 담는 상자이다.
  
```python
a = 3
3이라는 숫자 자룔르 a라는 상자(변수)에 담는다.

a = a+
# 오른쪽에 있는 값을
# 왼쪽 상자(변수)에 넣는다

```

## 2-1 숫자형
- 정수형(1,2,-2)
- 실수(1.24,-34.56)
- 컴퓨터식 지수 표현 방식(4.24e10,4.24e-10)
- 8진수 (0o37)
- 16진수 (0x7A)

```python
# - 정수 -
a = 1
print(a)
# -> 출력 : 1

print(type(a))
# -> 출력 : <class 'int'>

# - 실수 -
a = 1.24
print(type(a))
# -> 출력 : <class 'float'>
```

#### 연산
- 사칙연산이 가능하다. `+`,`-`,`/`,`*`,`%`


## 2-2문자열
- 문자열 자료형 만드는 4가지 방법
```python
"Hello world"
'python is fun'
"""Python grammer study"""
'''Python grammer study'''
```

- 문자열에 따옴표 포함시키기
```python
food = 'Python\' favorite food is perl'
say = "\"Python is very eash.\" he says."
```

- 실습
```python

a = "Hello world"
print(type(a))

#-> 결과 : <class : 'str'>

# 만약 문법을 다르게 썼을 때는
# 예) -> a = 'python's favorite fod is perl'
# invalid syntax : 이런 문법은 python에 없어 라고 띄워준다.

# -문자열 더해서 연결하기(Concatenation)-
a = "Python"
b = "is fun!"
print(a+b)

#-> 결과 : Python is fun
```

**인덱싱(Indexing)**
- 긴 문자열이 있으면 각각이 숫자로 번호가 매겨진다.
```python
a = "Life is too short, You need Python"
print(a[0])
#-> 결과 : L
print(a[-1])
#-> 결과 : n
```

**슬라이싱(Slicing)**
```python
a = "Life is too short, You need Python"
print(a[0:4])
#-> 결과 : Life
# a[이상 : 미만 : 간격] 

a = "123456789
print(a[::2])
#-> 결과 : 13579
```

</br>
</br>

### 이스케이프 코드
![](https://mblogthumb-phinf.pstatic.net/MjAxNzA0MDRfMzkg/MDAxNDkxMjczNzg3MzY1.tRnt4bBYsqA0A0m5MSAzcmRTH5h0sWbVEPD327XNYzEg.6U0oj7-gpH8td7p2PfEWtVDXFCi9vTy5-ylPWtRO-Rsg.PNG.dd1587/%EC%B4%9D%EC%A0%95%EB%A6%AC%ED%91%9C.png?type=w800)

**format**
```python
"aaasdf {aga} adsfase {name} asdfasdf".format(name="Django",age="3")

name = "int"
a = f"나의 이름은 {name}입니다"

print(a)

#-> 나의 이름은 int입니다. 3.6버전 이상 부터
```

**문자열 개수 세기(count)**
```python
a = "hobby"
a.count('b')
#-> 결과 : 2
```

**문자열 위치 알력주기1(find)**
```python
a = "Python is best choice"
a.find('b')
# -> 결과 : 10
```

**문자열 위치 알려주기2(index)**
```python
a = "Life is too short"
a.index('t')
# -> 결과 : 8
```

**문자열 삽입(join)**
```python
a = ","
a.join('abcd')
# -> 결과 : 'a,b,c,d'
```

**소문자를 대문자로 바꾸기(upper)**
```python
a = "hi"
a.upper()
# -> 결과 : 'HI'
```

**대문자를 소문자로 바꾸기(lower)**
```python
a = "HI"
a.lower()
# -> 결과 : 'hi'
```

**양쪽 공백 지우기(strip)**
```python
a = " hi "
a.strip()
'hi'
```

**문자열 바꾸기(replace)**
```python
a = "Life is too short"
a.replace("Life","Your leg")
# -> 결과 : 'Your leg is too short
```

**문자열 나누기(split)**
```python
a = "Life is too short"
a.split()
# -> 결과 : ['Life','is','too','short']
```

## **2-3 리스트**
> 변수 여러 개를 관리하기가 힘들기 때문에  
> 서랍장처럼 1,2,3번을 하나의 변수에서 관리할 수  
> 있도록 만들기 위해서 리스트를 사용한다.

- 1,3,5,7,9라는 숫자 모음
```python
odd = [1,3,5,7,9]
```
</br>

- 리스트명 = [요소1,요소2,요소3, ...]
```python
a = []
b = [1,2,3]
c = ['Life','is','too','short']
e = [1,2,['Life','is']]
```
- 리스트형 자료형의 수정 방법들은 문자열과 비슷하다

**del 함수 사용해 리스트 요소 삭제하기**
```python
a
#-> 출력 : [1,'c',4]

del a[1]
a
#-> 출력 : [1,4]
```

**리스트에 요소 추가(apeend)**
```python
a = [1,2,3]
a.append(4)
a
#-> 결과 : [1,2,3,4]
```

**리스트 정렬(sort)**
```python
a = [1,4,3,2]
a.sort()
a
#-> 결과 : [1,2,3,4]
```

**리스트 뒤집기(reverse)**
```python
a = ['a','c','b']
a.reverse()
a
#-> 결과 : ['b','c','a']
```

**위치 반환(index)**
```python
a = [1,2,3]
a.index(3)
#-> 결과 : 2
```

**리스트에 요소 삽입(insert)**
```python
a = [1,2,3]
a.insert(0,4)
#-> 결과 : [4,1,2,3]
```

**리스트 요소 제거(remove)**
```python
a = [1,2,3,1,2,3]
a.remove(3)
#-> 결과 : [1,2,1,2,3]
```

**리스트 요소 끄집어내기(pop)**
```python
a = [1,2,3]
a.pop()
a
#-> 결과 : [1,2]
```

**리스트에 포함된 요소 x의 개수 세기(count)**
```python
a = [1,2,3,1]
a.count(1)
#-> 결과 : 2
```

**리스트 확장(extend)**
```python
a = [1,2,3]
a.extend([4,5])
a
#-> 결과 : [1,2,3,4,5]
```