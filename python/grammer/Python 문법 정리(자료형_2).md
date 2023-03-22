# Python 문법 정리
> 기본적인 python 문법에 관해서 정리하였습니다  
> 튜플~자료형의 값을 저장하는 공간,변수

### 2-4 튜플 자료형
- 리스트와의 차의점은 리스트는 [대괄호] 튜플은(소괄호)
- 리스트는 계속해서 추가(append)할 수 있지만 튜플은 그런게 불가능하다

### 2-5 딕셔너리
- 사전적 정의 `사전`
- 단어를 키로 해서 어떤 값이 있는 자료구조라고 할 수 있다.
- API에 자주 활용됨

**딕셔너리 자료형**
- 연관 배열(Associative array) 또는 해시(Hash)
- 단어 그대로 해석하면 사전이라는 뜻
- Key를 통해 Value를 얻는다.
```python
dic = {'name':'pey','phone':'0119993323','birth':'1118'}
```

**딕셔너리 요소 쌍 추가하기**
```python
a = {1 : 'a'}
a[2] = 'b'
a
#-> 결과 : {2 : 'b', 1: 'a'}
```

**딕셔너리 요소 삭제하기**
```python
del a[1]
a
#-> 결과 : {'name': 'pey', 3: [1, 2, 3], 2: 'b'}
```

**딕셔너리에서 Key 사용해 Value 얻기**
```python
grade = {'pey' : 10,'julliet' : 99}
grade['pey']
#-> 결과 : 10
```

**딕셔너리 만들 때 주의할 사항**
```python
a = {1 : 'a',1:'b'}
a
#-> 결과 : {1:'b'}
```

**Key 리스트 만들기(keys)**
```python
a = {'name': 'pey', 'phone': '0119993323', 'birth':
'1118'} 
a.keys()
#->결과 : dict_keys(['name', 'phone', 'birth'])
```

**Value 리스트 만들기(values)**
```python
a.values()
#-> 결과 : dict_values(['pey', '0119993323', '1118'])
```

**Key,Value 쌍 얻기(items)**
```python
a = {'name': 'pey', 'phone': '0119993323', 'birth':
'1118'}
a.items()
#-> 결과 : dict_items([('name', 'pey'), ('phone', '0119993323'),('birth', '1118')])
```

**Key:Value 쌍 모두 지우기(clear)**
```python
a.clear()
a
#-> 결과 : {}
```

**Key로 Value얻기(get)**
```python
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a.get('name')
#-> 결과 : 'pey'
```

**해당 Key가 딕셔너리 안에 있는지 조사하기(in)**
```python
 a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
'name' in a
#-> 결과 : True
```

</br>
</br>

### 2-6 집합 자료형
- 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형중복을 허용하지 않는다.
- 순서가 없다(Unordered).

**집합 자료형**
```python
s1 = set([1,2,3])
s1
#-> 결과 : {1,2,3}

#순서가 없고 중복이 허용되지 않는다.
s2 = set("Hello")
s2
#-> 결과 : {'e', 'l', 'o', 'H'}
```

**교집합**
```python
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s1 & s2
#-> 결과 : {4,5,6}

or

s1.intersection(s2)
#-> 결과 : {4,5,6}
```

**합집합**
```python
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4,5,6,7,8,9])
s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}

or

s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
```

**차집합**
```python
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4,5,6,7,8,9])
s1 - s2
#-> 결과 : {1,2,3}

s2 - s1
#-> 결과 : {8,9,7}

or

s1.difference(s2)
#-> 결과 : {1,2,3}
s2.difference(s1)
#-> 결과 : {8,9,7}
```

**값 1개 추가하기(add)**
```python
s1 - set([1,2,3])
s1.add(4)
s1
#-> 결과 : {1,2,3,4}
```

**값 여러 개 추가힉(update)**
```python
s1 = set([1,2,3])
s1.update([4,5,6])
s1
#-> 결과 : {1,2,3,4,5,6}
```

**특정 값 제거하기(remove)**
```python
s1 = set([1,2,3])
s1.remove(2)
s1
#-> 결과 : {1,3}
```
