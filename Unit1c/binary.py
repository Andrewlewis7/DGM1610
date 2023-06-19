def binary_search_guess():
    low = 1
    high = 100

    while low <= high:
        mid = (low + high) // 2
        print("Is the number equal to, higher or lower than", mid, "?")
        response = input("Enter 'e' for equal, 'h' for higher, or 'l' for lower: ")

        if response == 'e':
            print("Great! The number is", mid)
            break
        elif response == 'h':
            low = mid + 1
        elif response == 'l':
            high = mid - 1
        else:
            print("Invalid input. Please try again.")

    if low > high:
        print("Oops! It seems that the number you're thinking of is not between 1 and 100.")

binary_search_guess()

# C:\Users\andre\OneDrive\Documents\GitHub\DGM1610\Unit1c\binary.py