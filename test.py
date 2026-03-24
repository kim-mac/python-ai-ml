

def main():
    l= 3
    r = 9 
    oddNumbers(l, r)

def oddNumbers(l, r):
    for i in range(l, r+1):
        if i % 2 != 0:

           print(i)

if __name__ == "__main__":    main()