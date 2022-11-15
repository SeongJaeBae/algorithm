
def main():
    s = [int(input()) for i in range(10)]
    answer = []
    for i in s:
        if i % 42 not in answer:
            answer.append(i % 42)
    print(len(answer))

        
if __name__ == "__main__":
    main()

