#Q1
R1, S = map(int, input().split())
R2= 2*S-R1
print(R2)
#Q2
def solution(babbling):
    answer = 0
    for word in babbling:
        temp = word.replace('aya', ' ').replace('ye', ' ').replace('woo', ' ').replace('ma', ' ').replace(' ','')
        if not temp:
            answer += 1
    return answer
