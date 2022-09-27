import math
from collections import defaultdict

def solution(fees, records):
    answer = []

    dict = {}
    total = defaultdict(int)
    # 주차한 시간
    for record in records :
        time, number, state = record.split() # 시간, 차량 번호, 상태(In or Out)
        hour, minutes = time.split(":")
        time = int(hour) * 60 + int(minutes)
        if number in dict : # 이미 입차되어 있다면
            total[number] += time - dict[number]
            del dict[number]
        else : # 입차할 경우
            dict[number] = time

    # 출차를 안 한 경우
    max_time = (23 * 60) + 59
    for num, t in dict.items():
        total[num] += max_time - t

    # 요금 계산
    basic_minutes, basic_fee, split_minutes, split_fee = fees
    for num, t in total.items() :
        cost = basic_fee
        if t > basic_minutes : # 추가 요금 발생
            cost += math.ceil((t - basic_minutes) / split_minutes) * split_fee # 올림 처리
        answer.append((num, cost))

    # 차량 번호 오름차순
    answer.sort()
    return [value[1] for value in answer]