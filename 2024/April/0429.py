#Q1

gap = 2541 - 1998
y = int(input())
if 1000 <= y <= 3000:
    print(y - gap)
#Q2

S = input()
i = int(input())
print(S[i-1])

#Q3

year = int(input())

if (year%4==0 and year %100 !=0) or year% 400==0:
    print(1)
else:
    print(0)

#Q4

score = int(input())
if 90<=score<=100:
    print("A")
elif 80<=score<90:
    print("B")
elif 70<=score<80:
    print("C")
elif 60<=score<70:
    print("D")
else:
    print("F")

#Q5

def solution(quiz):
    answer = []
    for q in quiz:
        X,operand,Y,equal,Z = q.split(' ')
        X = int(X)
        Y = int(Y)
        Z = int(Z)
        result = None
        if operand == '+':
            result = X + Y
        elif operand == '-':
            result = X - Y
        if result is not None and result == Z:
            answer.append("O")
        else:
            answer.append("X")
    return answer

