import collections
def main():
    n = int(input())
    m = int(input())
    n_list = list(map(int,input().split(" ")))

    q = collections.deque()


    for i in n_list:
        for j in n_list:
            if i + j == m:
                q.append([i,j])

    print(int(len(q)/2))

if __name__ == "__main__":
    main()


