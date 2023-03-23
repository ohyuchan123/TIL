# 카운터(Counter)
카운터(Counter)는 Python에서 제공하는 데이터 구조 중 하나로,  
요소들의 개수를 셀 때 사용된다.

Counter은 Python 표준 라이브러리 중 collections 모듈에 속한 클래스이다.

```python
from collections import Counter

numbers = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
counter = Counter(numbers)

print(counter)
```

위 코드에서는 collections 모듈에서 Counter 클래스를 import하고,   
리스트 numbers의 요소들을 카운팅하여 Counter 객체인 counter를 생성합니다.

출력은 다음과 같다.

```yaml
Counter({1: 4, 2: 3, 3: 2, 4: 1})
```

저는 이 라이브러리를 프로그래머스 최빈값에 활용하였습니다.

```python
from collections import Counter
def solution(array):
    c = Counter(array).most_common()
    print(c)
    if len(c) > 1 and c[0][1] == c[1][1]:
        return -1
    
    return c[0][0]
```