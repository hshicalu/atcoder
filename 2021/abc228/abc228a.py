

def main():
    
    s, t, x = map(int,input().split())

    if s < t:
        print("Yes" if s <= x and x < t else "No")
    else:
        print("Yes" if x < t or s <= x else "No")

if __name__ == "__main__":
    main()
