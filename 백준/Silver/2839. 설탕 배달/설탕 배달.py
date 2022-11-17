def main():
    s = int(input())
    #3 5 
    m_3 = int(s/3)
    l_3 = s%3
    m_5 = int(s/5)
    l_5 = s%5
    answer = 99999
    #
    if l_5 ==0:
        return print(m_5)
    else:

        for i in range(0,m_5+1):
            for j in range(0,m_3+1):
                if i*5 + j*3 > s:
                    break
                if i*5 + j*3 == s:
                    answer = min(answer, i+j)
        if answer == 99999:
            return print("-1")
        else:
            return print(answer)
if __name__ == "__main__":
    main()

