

def main():
    x = int(input())
    if x >= 90:
        print("expert")
    elif 70 <= x and x < 90:
        print(90 - x)
    elif 40 <= x and x < 70:
        print(70 - x)
    else:
        print(40 - x)

if __name__ == "__main__":
    main()
