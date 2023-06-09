# Python 문법 정리
> 기본적인 python 문법에 관해서 정리하였습니다  
> 조건문~반복문

### 03-1 if문
- 돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.
```python
money = True
if money : 
    print("택시를 타고 가라")
else :
    print("걸어 가라")

#-> 결과 : 택시를 타고 가라
```

**비교 연산자**

![](data:image/png;base64,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)

</br>
</br>

**and,or,not**
```python
x or y : x 와 y 둘중에 하나만 참이면 참이다.
x and y : x 와 y 모두 참이어야 참이다.
not x : x가 거짓이면 참이다.
```

- 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라
```python
money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else :
    print("걸어가라")

#-> 결과 : 택시를 타고 가라
```

**다중 조건 판단 elif**

### 03-2 while 문
- while문의 기본 구조
```python
while <조건문> :
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
```

**열 번 찍어 안 넘어 가는 나무 없다.**
```python
treeHit = 0
while treeHit <10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다.",%treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# 나무를 1번 찍었습니다.
# 나무를 2번 찍었습니다.
# 나무를 3번 찍었습니다.
#...
#나무 넘어갑니다.
```

**break**
- 반복문을 멈추는 기능

**continue**
- 반복문을 하면서 조건이 주어졌을때 그 조건이 참일때 건너뛰기

### 03-3 for문
- for문의 기본 구조
```python
for 변수 in 리스트(또는 튜플,문자열):
    수행할 문장1
    수행할 문장2
    ...
```

**전형적인 for문**
```python
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#-> 결과 :
# one
# two
# three
```

**for와 함께 자주 사용하는 range함수**
```python
sum = 0
for i in range(1,11):
    sum = sum+i
print(sum)
#-> 결과 : 55
```

**리스트 내포(List comprehension)**
```python
result = [num * 3 for num in a]
print(result)
#-> 결과 : [3,6,9,12]
```