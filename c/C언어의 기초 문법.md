# C언어의 기초 문법

```
목차

1. C언어의 기초
2. 입출력
3. 조건문
4. 반복문
5. 함수
6. 포인터
7. 구조체
```

이미 한번 정리한 곳이 있어 이곳에서는 제어문,함수,포인터,구조체만 정리하겠습니다.

**C언어의 기초**
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/C%EC%96%B8%EC%96%B4%EC%9D%98%20%EA%B8%B0%EC%B4%88/include%EC%99%80%20%ED%97%A4%EB%8D%94%ED%8C%8C%EC%9D%BC.md#include%EC%99%80-%ED%97%A4%EB%8D%94%ED%8C%8C%EC%9D%BC">include 와 헤더파일</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/C%EC%96%B8%EC%96%B4%EC%9D%98%20%EA%B8%B0%EC%B4%88/main%20%ED%95%A8%EC%88%98.md#main-%ED%95%A8%EC%88%98">main 함수</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/C%EC%96%B8%EC%96%B4%EC%9D%98%20%EA%B8%B0%EC%B4%88/%EB%B3%80%EC%88%98.md#%EB%B3%80%EC%88%98">변수</a>

**입출력**
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EC%9E%85%EC%B6%9C%EB%A0%A5/printf.md#printf">printf</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EC%9E%85%EC%B6%9C%EB%A0%A5/%EB%B3%80%ED%99%98%EB%AC%B8%EC%9E%90%EC%99%80%20%EA%B8%B0%ED%98%B8%EB%AC%B8%EC%9E%90.md#%EB%B3%80%ED%99%98%EB%AC%B8%EC%9E%90%EC%99%80-%EA%B8%B0%ED%98%B8%EB%AC%B8%EC%9E%90">변환문자와 기호문자</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EC%9E%85%EC%B6%9C%EB%A0%A5/scanf.md#scanf">scanf</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EC%9E%85%EC%B6%9C%EB%A0%A5/cast'%20%EC%97%B0%EC%82%B0%EC%9E%90.md#cast-%EC%97%B0%EC%82%B0%EC%9E%90">cast 연산자</a>

**조건문**
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EC%A1%B0%EA%B1%B4%EB%AC%B8/if%20%EB%AC%B8.md#if%EB%AC%B8">if문</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EC%A1%B0%EA%B1%B4%EB%AC%B8/Switch-Case.md#switch-case">Switch-Case</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EC%A1%B0%EA%B1%B4%EB%AC%B8/%EC%A1%B0%EA%B1%B4%EC%8B%9D.md#%EC%A1%B0%EA%B1%B4%EC%8B%9D">조건식</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EC%A1%B0%EA%B1%B4%EB%AC%B8/%EC%A1%B0%EA%B1%B4%20%EC%97%B0%EC%82%B0%EC%9E%90.md#%EC%A1%B0%EA%B1%B4-%EC%97%B0%EC%82%B0%EC%9E%90%EC%82%BC%ED%95%AD-%EC%97%B0%EC%82%B0%EC%9E%90">조건 연산자</a>

**함수**
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%95%A8%EC%88%98/%ED%95%A8%EC%88%98/%ED%95%A8%EC%88%98%EC%9D%98%20%EB%B0%98%ED%99%98%EA%B0%92.md#%ED%95%A8%EC%88%98%EC%9D%98-%EB%B0%98%ED%99%98return%EA%B0%92">함수의 반환(return)값</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%95%A8%EC%88%98/%ED%95%A8%EC%88%98/%EC%84%A0%EC%96%B8%EA%B3%BC%20%EC%A0%95%EC%9D%98.md#%EC%84%A0%EC%96%B8%EA%B3%BC-%EC%A0%95%EC%9D%98">선언과 정의</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%95%A8%EC%88%98/%ED%95%A8%EC%88%98/%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98.md#%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98">매개변수</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%95%A8%EC%88%98/%ED%95%A8%EC%88%98/%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98_2.md#%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%982">매개변수(2)</a>

**재귀함수**
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%95%A8%EC%88%98/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98%EC%9D%98%20%ED%8A%B9%EC%A7%95%EA%B3%BC%20%EC%84%A0%EC%96%B8%20%EB%B0%A9%EB%B2%95.md#%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98%EC%9D%98-%ED%8A%B9%EC%A7%95%EA%B3%BC-%EC%84%A0%EC%96%B8-%EB%B0%A9%EB%B2%95">재귀함수의 특징과 선언 방법</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%95%A8%EC%88%98/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98%EC%99%80%20%EB%B0%98%EB%B3%B5%EB%AC%B8%EC%9D%98%20%EA%B3%B5%ED%86%B5%EC%A0%90%EA%B3%BC%20%EC%B0%A8%EC%9D%B4%EC%A0%90.md#%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98%EC%99%80-%EB%B0%98%EB%B3%B5%EB%AC%B8%EC%9D%98-%EA%B3%B5%ED%86%B5%EC%A0%90%EA%B3%BC-%EC%B0%A8%EC%9D%B4%EC%A0%90">재귀함수와 반복문의 공통점과 차의점</a>

**재귀 함수의 활용**
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%95%A8%EC%88%98/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98%EC%9D%98%20%ED%99%9C%EC%9A%A9/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98%20%EC%88%98%EC%97%B4.md#%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98%EC%97%B4">피보나치 수열</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%95%A8%EC%88%98/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98%EC%9D%98%20%ED%99%9C%EC%9A%A9/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C%20%ED%98%B8%EC%A0%9C%EB%B2%95.md#%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95">유클리드 호제법</a>

**포인터**
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%8F%AC%EC%9D%B8%ED%84%B0/%ED%8F%AC%EC%9D%B8%ED%84%B0%20%EB%B3%80%EC%88%98%EC%99%80%20%EC%A3%BC%EC%86%8C%EA%B0%92%20%EC%B0%B8%EC%A1%B0%EC%99%80%20%EC%97%AD%EC%B0%B8%EC%A1%B0.md#%ED%8F%AC%EC%9D%B8%ED%84%B0-%EB%B3%80%EC%88%98%EC%99%80-%EC%A3%BC%EC%86%8C%EA%B0%92-%EC%B0%B8%EC%A1%B0%EC%99%80-%EC%97%AD%EC%B0%B8%EC%A1%B0">포인터 변수와 주소갑시 참조와 역참조</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%8F%AC%EC%9D%B8%ED%84%B0/%ED%8F%AC%EC%9D%B8%ED%84%B0%EC%99%80%20%ED%95%A8%EC%88%98%3B%20Call%20by%20reference.md#%ED%8F%AC%EC%9D%B8%ED%84%B0%EC%99%80-%ED%95%A8%EC%88%98-call-by-reference">포인터와 함수; Call by Reference</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%ED%8F%AC%EC%9D%B8%ED%84%B0/%EA%B5%AC%EC%A1%B0%EC%B2%B4%20%ED%8F%AC%EC%9D%B8%ED%84%B0%20%ED%8F%AC%EC%9D%B8%ED%84%B0%20%EC%97%B0%EC%82%B0%EC%9E%90.md#%EA%B5%AC%EC%A1%B0%EC%B2%B4-%ED%8F%AC%EC%9D%B8%ED%84%B0-%ED%8F%AC%EC%9D%B8%ED%84%B0-%EC%97%B0%EC%82%B0%EC%9E%90">구조체 포인터; 포인터 연산자</a>


**구조체**
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EA%B5%AC%EC%A1%B0%EC%B2%B4/%EA%B5%AC%EC%A1%B0%EC%B2%B4%EC%9D%98%20%EB%9C%BB%EA%B3%BC%20%EC%A2%85%EB%A5%98.md#%EA%B5%AC%EC%A1%B0%EC%B2%B4%EC%9D%98-%EB%9C%BB%EA%B3%BC-%EC%A2%85%EB%A5%98">구조체의 뜻과 종류; struct와 typedef struct</a>
- <a href="https://github.com/ohyuchan123/TIL/blob/main/c/%EA%B5%AC%EC%A1%B0%EC%B2%B4/%ED%8F%AC%EC%9D%B8%ED%84%B0%20%EA%B5%AC%EC%A1%B0%EC%B2%B4.md#%ED%8F%AC%EC%9D%B8%ED%84%B0-%EA%B5%AC%EC%A1%B0%EC%B2%B4">포인터 구조체</a>
