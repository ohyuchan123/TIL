# 직렬 변환기(serializers)

Django 직렬 변환기는 Django 모델과 같은 복잡한 데이터 유형을 웹 API 또는 다른 시스템에서 쉽게 사용할 수 있는 JSON, XML 또는 기타 콘텐츠 유형으로 변환하는 강력한 도구입니다.
직렬 변환기는 직렬화(데이터를 다른 형식으로 변환) 및 역직렬화(다른 형식의 데이터를 PYthon 객체로 변환)하는 데 사용할 수 있습니다.
</br>

Django에서 직렬 변환기는 일반적으로 내장 serializers.Serializer 클래스에서 상속되는 클래스를 정의됩니다. 직렬 변환기 클래스 내에서 필요한 사용자 지정 또는 유효성 검사 노리와 함께 직렬화된 표현에 포함할 필드를 정의합니다.
</br>

Django에서 직렬 변환기 사용의 주요 이점 중 하나는 기본 데이터 모델에 관계없이 응용 프로그램에 대해 일관된 API를 정의하는 방법을 제공한다는 것입니다. 이를 통해 클라이언트 측 코드를 단순화하고 시간이 지남에 따라 API를 보다 쉽게 유지 관리하고 발전시킬 수 있습니다.


**rest framework tutorial code**
```python
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
```