sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print('Error, Please enter numeric input')
    quit()
print(fh, fr)
if fh > 40:
    reg = fh * fr
    otp = (fh - 40.0) * (fr * .5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:",xp)