def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return
    

    finally:
        print(" Hey i am inside an finally")

main()