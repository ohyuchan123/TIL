# for문을 활용한 다양한 *찍기를 작성합니다.
# python의 별찍기는 다른 언어의 별찍기와는 다르게 작성되서 따로 작성하였습니다.

#*
#**
#*** 

#1번 코드

#format
for i in range(5):
    print(':<5'.format('*'*(i+1)))

#일반 코드
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print("")


#*** 
#**
#*

# 2번 코드

#format
for i in range(6,0,-1):
    print('{:<5}'.format('*'*(i-1)))

# 일반 코드
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print('')

# 나머지 코드는 위 두 코드를 활용할 수 있으면 만들 수 있다고 생각해서
# 생략 하겠습니다.