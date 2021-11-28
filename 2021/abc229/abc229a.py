

def main():
    s1 = input() 
    s2 = input() 
    #a, b = map(int,input().split())
    #n = int(input())
    ans = True
    if (s1 == ".#" and s2 == "#.") or (s1 == "#." and s2 == ".#"):
        ans = False
    
    if ans:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
