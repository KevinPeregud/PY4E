largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    #print(num)
        
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
        
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
   
print('Maximum is', largest)
print('Minimum is', smallest)


#Want to fine max and min
#Invalid input
#Maximum is 10
#Minimum is 2