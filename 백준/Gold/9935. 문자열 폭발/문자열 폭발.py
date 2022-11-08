
def main():
    
    
    s = list(str(input()))
    bomb = list(str(input()))
    answer = []
    ## 큐& 재귀를 활용해서 O(n)으로 끝내야 될듯
    
    i=0
    #첫글자가 나오면 재귀돌려서 체크-> 재귀 돌리다가 다했는데도 틀림 -> 끝글자로 해야 될듯 
    for i in s:
        answer.append(i)
        
        if i == bomb[len(bomb)-1]:
            #print(answer[-len(bomb):])
            #print(answer)
            if answer[-len(bomb):] == bomb:
                for i in bomb:
                    answer.pop()

    if len(answer) == 0:
        print("FRULA")
    else:
        print("".join(answer))
"""
    old = new = s1
    while(len(new) <= len(old)):
        old = new
        #replace O(n) 반복문 n * n -> n^2 로 터짐
        new = old.replace(bomb,"")
        if new == "":
            return print("FRULA")
        if new == old:
            return print(new)
            break
   """

if __name__ == "__main__":
    main()


