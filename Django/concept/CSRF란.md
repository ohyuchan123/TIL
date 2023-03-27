# CSRF란?
CSRF(cross site request forgery)는 **웹 사이트 취약점 공격을 방지를 위해 사용하는 기술이다.** 장고가 CSRF 토큰 값을 세션을 통해 발행하고 웹 페이지에서는 폼 전송시에 해당 토큰을 함께 전송하여 실제 웹 페이지에서 작성된 데이터가 전달되는지를 검증하는 기술이다.
</br>

csrf_token 사용을 위해서는 CsrfViewMiddleware 미들웨어가 필요한데 이 미들웨어는 settings.py의 MIDDLEWARE 항목에 디폴트로 추가되어 있으므로 별도의 설정은 필요 없다.

```python
(... 생략 ...)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
(... 생략 ...)
```
만약 crf_token 기능을 사용하고 싶지 않다면 주석 처리된 부분처럼 주석 처리 하면 된다.