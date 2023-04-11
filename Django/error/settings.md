# template를 연결할 때 setting.py에서 에러가 발생헀다

아 이것때문에 꽤나 고생했다 실제로 별로 많은 작업이 필요가 없었지만  
내가 이해를 못해서 시간이 많이 소모가 되었다

django에 대한 개념은 꾸준히 공부하자!!!

일단 오류를 해결하기 위해서는 setting.py에 설정을 해줘야 한다.

아래 설정은 다 해줘야 연결이 된다. (사실 맞는지 잘 모르겠음....)  
이렇게 하더니 되버렸다.

```python
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
```

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

일단 위에서 `import os`에 대해서 설명하겠다

**python os란?**
일단 간단하게 설명하자면 운영체제에서 제공되는 여러 기능을 파이썬에서 수행시켜주는 파이썬 라이브러리(모듈)

**os의 필요성**
운영체제에서 자연스럽게 하던 작업들을 코드에서도 활용할 수 있게 해준다.

- 파일 복사, 폴더 생성, 폴더 내 파일 목록 구하기 등등

**os의 사용법**
```python
// os 라이브러리 불러오기
import os
// 현재 경로 가져오기
os.getcwd()  // '현재 경로'
// 폴더 변경하기
os.chdir('폴더 경로')
// 폴더에 존재하는 파일들 목록 가져오기
os.listdir('폴더 경로')  // ['파일1', '파일2' ... ]
// 목록 개수 확인
len(os.listdir('폴더 경로'))
```