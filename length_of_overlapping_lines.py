
def solution(lines):
    #lines = [[0, 5], [3, 9], [1, 10]]
    starts = [min(a) for a in lines]  #index[0]자리만 뽑기  #[0,3,1]
    ends = [max(a) for a in lines]  #index[1]자리만 뽑기  #[5,9,10]
    starts.sort() #정렬[0,1,3]
    ends.sort() #정렬[5,9,10]
    answer = 0  #answer정의
    answer += max(0, ends[0] - starts[1])      #max(0, 5-1) -> 4 반환
    answer += max(0, ends[1] - starts[2])      #max(0, 9-3) -> 6 반환
    answer -= max(0, ends[0] - starts[2])      #max(0, 5-3) -> 2 반환
    print(answer) #8반환

