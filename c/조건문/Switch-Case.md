# Switch-Case
정렬 조건문

switch-case문은 정렬 조건문이라고 볼 수 있다.

```c
int a;
scanf("%d", &a);
switch(a){ // 변수 a를 조사한다
case 1:
    printf("1");
    break;
case 2:
    printf("2");
    break;
// ...(10까지 계속 쓴다)
default:
    printf("default");
}
```
이렇게 쓰면 a에 대한 조건식을 일일이 다 쓸 필요가 없습니다. switch(a)라고 하면 괄호 안 a라는 변수의 값을 조사한다는 뜻이 되고(굳이 변수가 아니여도 됩니다. 값을 가지고 있는 무엇이든 됩니다), case n: 은 '만약 a가 n일 때'와 같은 의미가 됩니다. 단, case문은 switch 문 안 중괄호의 들여쓰기를 무시합니다. 콜론: 다음 줄에는 명령어를 쓰고, 다 끝났으면 break;를 씁니다. break는 이 switch 문에서 나간다는 뜻이 됩니다. 만약 break를 쓰지 않는다면 계속 switch 문 안에서 끝까지 가게 됩니다.