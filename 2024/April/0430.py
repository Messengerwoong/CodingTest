#Q1:
def solution(age):
    answer = 2022-age+1
    return answer

#Q2:
x,y,w,h = map(int,input().split())
print(min(x,y,w-x,h-y))


#Q3:
def solution(my_string, s, e):
    str_list = list(my_string)
    str_list[s:e+1] = str_list[s:e+1][::-1]
    answer = ''.join(str_list)
    return answer

#Q4:
def solution(numbers):
    number_map = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, word in enumerate(number_map):
        numbers = numbers.replace(word, str(i))

    return int(numbers)
#Q5:
def solution(array):
    arr_list = {}
    for a in array:
        if a in arr_list:
            arr_list[a] += 1
        else:
            arr_list[a] = 1
    max_count = max(arr_list.values())
    mode = [key for key, value in arr_list.items() if value == max_count]
    if len(mode) > 1:
        return -1
    else:
        return mode[0]
