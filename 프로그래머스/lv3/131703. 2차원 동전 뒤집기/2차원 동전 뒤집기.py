def flipColumn(arr, col):
    n = len(arr)

    for i in range(n):
        if arr[i][col] == 1:
            arr[i][col] = 0
        else:
            arr[i][col] = 1


def solution(beginning, target):
    answer = float("inf")
    rows = len(beginning)
    cols = len(beginning[0])

    flipped = []
	# 미리 원본 배열을 flip시켜서 저장
    for i in range(rows):
        flipped.append([])
        for j in range(cols):
            if beginning[i][j]:
                flipped[i].append(0)
            else:
                flipped[i].append(1)

    # and시킬 bitmask를 돌면서
    for unit in range(1 << rows):
        rowFlipped = []
        flipCnt = 0
        for i in range(rows):
        	# 000, 010, 100... bitmask 생성
            comp = 1 << i

            # and한 값이 0이 아니면 해당 row 뒤집기
            if unit & comp:
                rowFlipped.append(flipped[i][:])
                flipCnt += 1
            # 해당 row 뒤집지 않기
            else:
                rowFlipped.append(beginning[i][:])
                
        # 열 뒤집기
        for j in range(cols):
            curCol = []
            targetCol = []

            for i in range(rows):
                curCol.append(rowFlipped[i][j])
                targetCol.append(target[i][j])
			
            # 현재 column과 target column이 다르면 뒤집기
            if curCol != targetCol:
                flipColumn(rowFlipped, j)
                flipCnt += 1

		# 결국 뒤집은 결과가 target과 같으면 뒤집은 횟수 갱신
        if rowFlipped == target:
            answer = min(answer, flipCnt)

    if answer == float("inf"):
        answer = -1

    return answer