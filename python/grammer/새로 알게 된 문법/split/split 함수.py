# split 함수 사용 예제

s = "a b c d e f g"
print(f's : {s}')

r = s.split()
print(f's.split() : {r}')

# split 함수 예제2
s = "aa.bb.cc.dd.ee.ff.gg"
print(f's                : {s}')
 
r0 = s.split()
r1 = s.split('.')
r2 = s.split(sep='.')
print(f"s.split()        : {r0}")
print(f"s.split('.')     : {r1}")
print(f"s.split(sep='.') : {r2}")

# 공원 산책
# -> E 2 분리
routes = ["E 2","S 2","W 1"]

for route in routes:
        dir, move = route.split(' ')
        move = int(move)