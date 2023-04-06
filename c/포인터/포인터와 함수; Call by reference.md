# 포인터와 함수; Call by Reference
```c
int add(int *x, int *y){
    *x += *y;
    return *x;
}
int main(){
    int a = 5, b = 5;
    printf("%d %d", add(a, b), a);
}
```

위 코드처럼 하면 매개변수가 포인터 변수가 되면수 함수가 작동 할 때 a,b의 실인수 값이 바뀝니다. 그래서 출력문은 10,10이 된다.