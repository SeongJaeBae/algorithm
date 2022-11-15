
def main():
    a ,b = input().split(" ")
    
    if int(a)>int(b):
        print(">")
    elif int(a)== int(b):
        print("==")
    elif int(a) < int(b):
        print("<")


if __name__ == "__main__":
    main()

