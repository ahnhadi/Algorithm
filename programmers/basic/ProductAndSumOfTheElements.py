# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    a = 1
    b = 0
    c = 0
    for i in range(0,len(num_list)):
        a *= num_list[i]
        b += num_list[i]
        c = b**2
    if a < c:
        return 1
    if a > c:
        return 0