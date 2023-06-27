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


#Enter a number: 6
#Enter a number: 2
#Enter a number: 9
#Enter a number: 3
#Enter a number: 5
#Enter a number: done
#Maximum: 9.0
#Minimum: 2.0