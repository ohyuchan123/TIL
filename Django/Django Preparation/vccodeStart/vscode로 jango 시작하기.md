# VSCode로 Django 시작하기
`cmd(명령 프롬프트)`에서 프로젝트 경로를 정한다.
```python
cd .. #	이전 폴더로(뒤로가기)
cd 폴더명	# 해당 폴더로
mkdir 폴더명 #폴더 생성

해당 폴더 위치에서 code . # vscode 실행
```

**vscode에서**
ctrl + `를 눌러 터미널을 연다.</br>
다음과 같이 입력한다.</br>
`python -m  venv jangovenv`</br>
jangovenv는 생성할 가상환경 폴더명이다.

**django 설치 및 서버 실행**
f1을 누르고 Select Interpreter을 누르고 생성했던 가상환경 폴더와 같은 이름이 있는 항목을 선택한다.
</br>

`python -m pip install django`
`django-admin startproject config .`
`cd firstPj`
`python manage.py runserver`