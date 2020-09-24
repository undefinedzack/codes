testCases = int(input())

for i in range(testCases):
    N = int(input())
    score_board = str(input())

    a,b = 0 , 0
    a_series,b_series = [] , []
    for knt in range(0,len(score_board),2):

        a += int(score_board[knt])
        a_series.append(score_board[knt])
        b += int(score_board[knt+1])
        b_series.append(score_board[knt+1])
        # print(a_series,b_series)

        if a > b:
            if b + (N-len(b_series)) > a:
                continue
            else:
                print(knt+2)
                break
        elif a == b:
            if N - len(a_series) == 0:
                print(knt+2)
            else:
                continue
        else:
            if a + (N-len(a_series)) > b:
                continue
            else:
                print(knt+2)
                break