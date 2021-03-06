# a = 60, b = 13 일때,
# a = 0011 1100
# b = 0000 1101
# a & b = 0000 1100
# a | b = 0011 1101
# a ^ b = 0011 0001
# ~a = 1100 0011
# a << 2 = 240 -> 1111 0000
# a >> 2 = 15 ->  0000 1111

# 적용 문제풀기 
# 더해서 합이 0 이 되는 부분 집합 갯수 구하기

L = [-7, -3, -2, 5, 8]
n = len(L)
ret = 0
for i in range(1,1 << n): # 전체 부분집합 loop
    SUM = 0 
    for j in range(n):
        # i의 j 번째 비트가 1이면 j번째 원소 출력
        if i & (1 << j): 
            SUM += L[j]
    if SUM == 0:
        ret = 1
        break
print(ret)