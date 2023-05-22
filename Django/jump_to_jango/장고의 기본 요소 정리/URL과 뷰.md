## url과 view

---

**urls.py**

```python
from django.contrib import admin
from django.urls import path

from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', views.index),
]
```

`pybo/` url이 요청되면 `views.index`를 호출하라는 매핑을 urlpatterns에 추가하였다.  
views.index는 views.py 파일의 index 함수를 의미한다.

urlpatterns에서 실제 URL은 http://localhost:8000/pybo 이지만 호스트명과 포트가 생략된 pybo/로 매핑해야 한다.  
왜냐하면 호스트(예:localhost)와 포트(예:8000)는 서버가 어떤 환경에서 실행되는지에 따라 변하기 때문이다.

또 한가지 pybo/ 를 pybo라고 하지 않고 뒤에 슬래시(/)를 하나 더 붙여 주었다.  
이렇게 뒤에 슬래시를 붙여주면 브라우저 주소창에 http://localhost:8000/pybo 라고 입력해도 자동으로 http://localhost:8000/pybo/ 처럼 변환된다.  
이렇게 되는 이유는 URL을 정규화하는 장고의 기능 때문이다.  
특별한 경우가 아니라면 URL 매핑시 항상 끝에 슬래시를 붙여 주도록 하자.

**views.py**

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
```

HttpResponse는 요청에 대한 응답을 할 때 사용한다.  
여기서는 "안녕하세요 pybo에 오신것을 환영합니다" 라는 문자열을 브라우저에 출력하기 위해 사용되었다.  
index 함수의 매개변수 request는 HTTP 요청 객체이다.

이렇게 뷰 함수를 작성하고 다시 `http://localhost:8080/pybo`url을 요청하면 다음과 같은 결과를 확인할 수 있다.

![](https://wikidocs.net/images/page/70649/O_2-01_2.png)

## URL 분리

---

pybo 앱에 과련한 것들은 pybo 앱 디렉터리 하위에 위치해야 한다.  
하지만 위 내용 대로면 pybo와 관련된 url 매핑을 추가할 때마다 `config/urls.py`파일을 수정해야 한다.  
config의 urls.py 파일은 앱이 아닌 프로젝트 성격의 파일이므로 이곳에서는 프로젝트 성격의 url 매핑만 추가되어야 한다.  
따라서 pybo 앱에서만 사용하는 url 매핑을 `config/urls.py`파일에 계속 추가하는 것은 좋은 방법이 아니다.

```python
from django.contrib import admin
from django.urls import path, include
from pybo import views  # 더 이상 필요하지 않으므로 삭제

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
]
```

그렇다면 이제 pybo/urls.py 파일을 생성해야 한다. 파이참에서 pybo/urls.py 파일을 생성하기 위해 [pybo → 마우스 오른쪽 클릭 → New → File]을 한 다음 파일명으로 urls.py를 입력하자.

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]
```
