# main 함수

C언어는 프로그램이 시작되면 무조건 main부터 찾게 됩니다.  

main 함수 안에 코딩을 짜야 명령어가 실행됩니다. main함수는 아래와 같이 작성합니다.

```c
#include <stdio.h>
#include <stdlib.h>
 
int main()
{
    /*coding...*/
}
```

위에 main을 쓰고, 중괄호 안에 명령어를 쓰면 그 명령어가 작동됩니다.

main 함수 안에 있는 int는 main의 반환값을 의미합니다.
반환값에 따라서 반환을 해야 하는 값이 다른데, 반환값을 정하지 않으면 무조건 0으로 반환됩니다. 이것을 바꿀면 "return"을 사용하면 된다.

```c
#include <stdio.h>
#include <stdlib.h>
 
int main()
{
    /*coding*/
    return 0;
}
```