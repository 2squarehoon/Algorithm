year = int(input())
if not year % 4:
    if not year % 100:
        if not year % 400:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
