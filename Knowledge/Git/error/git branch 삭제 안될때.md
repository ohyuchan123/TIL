# git 브랜치 삭제 안될 때

깃 브랜치를 삭제하려고 할 때
```
git branch -d dev
```

아래와 같은 오류가 뜨면서 삭제가 안될 때가 있다.
```
error: Cannot delete branch 'dev' checked out at 'C:/Users/dev'
```

이는 현재 브랜치가 삭제하고자 하는 브랜치 이기 때문이며  
아래와 같이 브랜치를 전환한 후에 삭제하면 된다.

```
git checkout master

git branch -d dev
```