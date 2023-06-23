
score = input("Enter Score: ")
try:
    sc = float(score)
except:
    print('Bad Score, Please enter numeric input between 0 and 1.0')
    quit()
if sc > 1.0:
    print('Bad Score, enter value between 0 and 1.0')
    quit()
elif sc == 1:
    print('Perfect Score')
elif sc >=.9:
    print('A')
elif sc >=.8:
    print('B')
elif sc >=.7:
    print('C')
elif sc >=.6:
    print('D')
else:
    print('F')

#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
# < 0.6     F
#Enter score: 0.95
#A
#Enter score: perfect
#Bad score
#Enter score: 10.0
#Bad score
#Enter score: 0.75
#C
#Enter score: 0.5