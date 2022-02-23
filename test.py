information = input().split()

number_of_comment = int(information[0])
observe_time = int(information[1])
judge_time = int(information[2])
judge_good = int(information[3])

all_list = [[0 for j in range(observe_time)] for i in range(number_of_comment)]

i = 0
j = 0

while(j != observe_time):
    information_comment = input().split()
    while(i != number_of_comment):
        all_list[i][j] = int(information_comment[i])
        i = i + 1
    i = 0
    j = j + 1

i = 0
j = 0
anser_buzz = 0
check_time = 0
repeat_num = judge_time

while(i != number_of_comment):
    while(j + judge_time != observe_time + 1):
        k = j
        while(k != repeat_num):
            anser_buzz = anser_buzz + all_list[i][k]
            if(anser_buzz >= judge_good):
                check_time = k + 1
                break
            k = k + 1
        anser_buzz = 0
        j = j + 1
        repeat_num = repeat_num + 1
        if(check_time != 0):
            break
    i = i + 1
    j = 0
    repeat_num = judge_time
    if(check_time != 0):
        anser_str = "yes" + str(check_time)
        print(anser_str)
    else:
        anser_str = "no" + str(0)
        print(anser_str)
    check_time = 0