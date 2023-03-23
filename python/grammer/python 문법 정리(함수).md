# 기본적으로 자주 사용하는 내장 함수들을 정리하였습니다
- 공부하면서 중요하다고 생각한 함수를 앞으로 추가해 나갈 생각입니다.

### 리스트 내 원소 갯수,크기 반환 : len()
```python
A = [1,2,3,4,5]
print(len(A))
#-> 결과 : 5
```

### 자료형 확인 : type()
```python
A = 'bskyvision`
print("A의 자료형:",type(A))

B = 1988
print("B의 자료형 :",type(B))

#-> 결과 : A의 자료형 : <class 'str'>
#-> 결과 : B의 자료형 : <class 'int'>
```

### 문자형 변환
```python
A = '10'
print(type(A))
#-> 결과 :  <class 'str'>

B = int(A)
print(type(B))
#-> 결과 : <class 'int'>

C = str(B)
print(type(C))
#-> 결과 : <class 'str'>
```

### 반올림 : round()
```python
a  = 167.4868
print(round(a))
print(round(a,1))
print(round(a,2))
print(round(a,-1))
print(round(a,-2))

#-> 결과 : 
# 167
# 167.49
# 170.0
# 200.0
```

### 절대값 : abs()
```python
a = -1.6
print(abs(a))

b = 2.5
print(abs(b))

#-> 결과 :
# 1.6
# 2.5
```

### 최대값,최소값 : max(),min()
```python
a = [10,12,5,4,-3,0,19,2,8]
print(max(a))
print(min(a))

# -> 결과 :
# 19
# -3
```

### 크기 순으로 정렬 : sorted()
```python
a = [10,12,5,4,-3,0,19,2,8]
print(sorted(a)) # 오름차순 정렬
print(sorted(a,reverse=True)) #내림차순 정렬
```

### 리스트 원소의 합 : sum()
```python
a = [1,2,3,4,5,6,7,8,9,10]
print(sum(a))
# -> 결과 :
# 55
```

### for문에 자주 사용되는 range()
```python
for i in range(10):
    print(i)

for i in range(0,10):
    print(i)

for i in range(0,10,2): # 2씩 증가
    print(i)
```

### enumrate => 열거하다
```python
for i, name in enumerate(['body', 'foo', 'bar']):
print(i, name)

# 결과 :
# 0 body
# 1 foo
# 2 bar
```

