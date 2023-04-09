# IoC(Inversion of Control)란?
IoC는 제어의 역전이라는 뜻으로 프로그램의 제어 흐름을 직접 제어하는 것이 아니라 외부에서 관리하는 것을 말한다.  
이전에는 개발자가 객체를 생성하고 관리하며 프로그램의 제어 흐름을 스스로 조종했다.  
하지만 Spring을 사용하면 스프링 컨테이너가 프로그램의 제어흐름을 제어하게 된다.

# DI(Dependency Injection)란?
DI는 의존관계 주입이라는 뜻으로 여기서 의존관계(Dependency)는 어떠한 객체와 같이 수행(work with)되는 다른 객체와의 관계를 뜻한다.

# 스프링 컨테이너(Spring Container)란?
스프링 컨테이너는 스프링의 빈(Bean)을 생성하고 관리한다. 스프링 컨테이너는 IoC Container 혹은 DI Container라고 불리는데,  
이는 스프링 컨테이너가 IoC 혹은 DI를 도맡아 진행하기 때문이다. 즉, 스프링 컨테이너는 스프링 Bean들을 생성하고, 이들의 의존 관계를 연결해주는 역할을 한다.
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb6SSct%2FbtrtoA0hR0q%2FIX3tnrZKLki7owa4qK5mxk%2Fimg.webp)

이러한 스프링 컨테이너는 BeanFactory와 ApplicationContext로 나뉘는데 둘의 내용은 다음과 같다.

**BeanFactory**
- 스프링 컨테이너의 최상위 인터페이스이다.
- 스프링 빈을 관리하고 조회하는 역할을 담당한다.

**ApplicationContext**
- BeanFactory 기능을 모두 상속받아서 제공한다.
- 다음과 같은 부가기능들을 제공한다.
    - 메시지 소스를 활용한 국제화 기능
    - 환경변수 - 로컨,개발,운영 등을 구분해서 처리
    - 애플리케이션 이벤트 관리
    - 편리한 리소스 조회


보통 스프링 컨테이너라고 하면 ApplicationContext를 뜻한다. BeanFactory의 모드 기능을 상속받는데다가 편리한 부가기능을 제공하기 때문에 BeanFactory 보다는 ApplicationContext를 사용하게 된다.

# 스프링 빈(Bean)이란?
스프링에서는, 스프링 IoC 컨테이너에 의해 관리되고 애플리케이션의 핵심을 이루는 객체들을 Bean이라고 부른다. Bean은 스프링 IoC 컨테이너에 의해 인스턴스화되어 조립되거나 관리되는 객체를 말한다.

즉, 스프링 빈은 스프링 컨테이너에 의해서 만들어지고 관리되는 객체라는 뜻이다. 