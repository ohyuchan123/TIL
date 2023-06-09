# git commit 내용 수정하기

## **1. 아직 커밋이 local에 있을 때**
> 아직 로컬에서 commit을 하고 push는 하지 않아 remote에 올라가지 않은 상태일 경우  
다음과 같이 하면 된다.

### 1.1 가장 최근의 commit 수정
```
git commit --amend
```
위와 같이 `amend`를 이용하면 가장 마지막에 commit한 내용을 수정할 수 있습니다.  
`git commit --amend`를 사용하고 커밋을 수정할 수 있는 창이 뜨면, 수정을 완료한 후 `esc`->`:wq`(저장 + 창 닫기)를 해주면 됩니다.

### 1.2 더 오래된 commit 수정 or 한 번에 여러 commit 수정
커맨드 라인에 `git log`를 작성 해보면  

로그에서 여태 자신이 한 커밋을 쭉 확인 후 어던 커밋을 수정할 것인지 알려준다. -> ㄷㄷ

만일 위에서부터 세 번째 커밋을 수정해야 한다면
`git revase -i HEAD~3`

위 커맨드를 사용하면 현재 작업중인 브랜치의 가장 최근 commit 3개를 보여주게 됩니다.

(3이 들어간 자리에 체크하길 원하는 commit의 갯수를 집어넣으면 된다.)

수정하고 싶은 커밋 옆의 `pick` 이라는 문구를 reword로 바꿔 주면 된다.

## **2. 이미 커밋을 push해 remote에 올린 상황일 때**
커밋이 이미 remote에 적용된 상황이라면, `force`를 통해 서정된 커밋을 강제로 `push` 해주어야 합니다.

github 공식 문서에 따르면 force pushing을 **최대한 사용하지 않아야 한다**고 해서 push 된 커밋의 로그를 갖고 있던 다른 팀원들이 **로그를 수동으로 수정해줘야 하기 때문**이라고 한다.

로컬에서 commit을 할 때도 중요하지만 remote에 push 하기 전에는 정말 두 번 세 번 다시 확인하자!!

방법 자체는 간단하다 loacl에서 commit 메세지를 수정한 후, 아래 커맨드를 실행하면 된다.

```
git push --force 브랜치이름
```