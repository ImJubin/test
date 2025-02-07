#평균 = 총합 / 리스트 길이
#       >sum, len 없이 총합, 길이를 구하려면? 반복문을 돌아야해(구조)
#       >그 총합(sum_list)과 길이(lengh)는 변수가 필요하겠군(data)
#최소, 최대
#       >min max 없이 최소 치대 구하려면? 반복문을 돌아야 해 (구조)
#       >최소, 최대 변수가 필요하겠군(data)

#  아 그럼 반복문은 한 번만 돌아도 그 안에서 다 구할 수 있겠군

def analyze_likes(weekly_like_list):
    sum_list = 0
    size_list = 0
    min_list = max_list = weekly_like_list[0]

    for number in weekly_like_list:
        size_list += 1
        sum_list += number

        if number < min_list:
                min_list = number
        
        if number > max_list:
                max_list = number
    
    return (sum_list/size_list, max_list-min_list)

