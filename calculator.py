def main():
    x = int(input("Enter your number: "))
    print(f"the number {x} squared is", square(x))

def square(n):
    sqr = n * n
    return sqr

if __name__ == "__main__":
   main()