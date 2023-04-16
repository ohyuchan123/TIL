# MVT 패턴
장고 프레임워크에서는 View를 Template, Controller는 View라고 표현하며, MVC를 MVT 패턴이라고 한다.

모델은 데이터 베이스에 저장되는 데이터를 의미하는 것이고, 템플릿은 사용자에게 보여지는 UI부분을, 뷰는 실질적으로 프로그램 로직이 동작하여 데이터를 가져오고 적절하게 처리한 결과를 템플렛에 전달하는 역할을 수행한다.
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FpdQ3m%2FbtqwhTpC3gU%2FvXB2IGfXViX7cGFQgXjlR1%2Fimg.png)

웹 클라이언트의 요청을 받고, 장고에서 MVT 패턴에 따라 처리하는 과정을 요약하면 다음과 같다.

1. 클라이언트로부터 요청을 받으면 URLconf를 이용하여 URL을 분석한다.
2. URL 분석 결과를 통해 해당 URL에 대한 처리를 담당할 뷰를 결정한다.
3. 뷰는 자시의 로직을 실행하면서 만일 데이터 베이스 처리가 필요하면 모델을 통해 처리하고 그 결과를 반환받는다.
4. 뷰는 자신의 로직 처리가 끝나면 템플릿을 사용하여 클라이언트에 전송할 HTML 파일을 생성한다.
5. 뷰는 최종 결과로 HTML 파일을 클라이언트에게 보내 응답한다.