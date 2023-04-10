# 코틀린 프로그래밍 언어 알아보기

**목차**
```
변수 선언
    유형 추론
    Null 안전
조건부
함수
    함수 선언 단순화
    익명 함수
    고차 함수
```

## 변수 선언
Kolin은 두 키원 (`val` 및 `var`)를 상ㅇ하여 변수를 선언합니다.
- 값이 변경되지 않는 변수에 `val`을 사용합니다. `val`을 사용하여 선언된 벼수에 값을 재할당할 수 없습니다.
- 값이 변경될 수 있는 변수에 `var`을 사용합니다.

아래 예에서 `count`는 `10`의 초기 값이 할당되는 `Int` 유형의 변수입니다.

```kotlin
var count : Int = 10
```

`Int`는 정수를 나타내는 유형이며 Kotlin에서 표현될 수 있는 많은 숫자 유형 중 하나입니다. 다른 언어와 마찬가지로 수치 데이터에 따라 `Byte`,`Short`,`Long`,`Float`,`Double`을 사용할 수도 있습니다.

`var` 키워드는 필요에 따라 `count`에 값을 재할당할 수 있음을 의미합니다. 예를 들어 `count` 값을 `10`에서 `15`로 변경할 수 있습니다.

```kotlin
var count : Int = 10
count = 15
```

하지만 일부 값을 변경되지 않습니다. `languageName`이라는 `String`을 고려합니다. `languageName`에서 'Kotlin'의 값이 현상 유지되도록 하려면 `val` 키워드를 사용하여 `languageName`을 선언합니다.

```kotlin
val languageName: String = "Kotlin"
```

**유형 추론**
---
