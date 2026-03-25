import time
def length(password, leng):
    if len(password) >= 16:
        leng += 10
    elif len(password) < 16 and len(password) >=10:
        leng += 7
    elif len(password) >= 8:
        leng += 5
    else:
        leng +=3
        print("Password should have atleast 8 characters!")
    print(f"Score for length of password: {leng}/10")
    return leng

def digits(password, digit):
    count = 0
    for i in password:
        if i.isdigit():
            count+=1
    if count > 5:
        digit +=10
    elif count <=5 and count >=3:
        digit +=7
    elif count < 3 and count > 0:
        digit+=5
    else:
        digit = 0
        print("Password should contain atleast 1 digit!")
    print(f"Score for password containing digits: {digit}/10")
    return digit

def lowercase(password, lower):
    count = 0
    for i in password:
        if i.islower():
            count +=1
    if count > 6:
        lower +=10
    elif count <=6 and count >=4:
        lower +=7
    elif count < 4 and count >0:
        lower+=5
    else:
        lower = 0
        print("Password should contain lowercase characters!")
    print(f"Score for password containing lowercase characters: {lower}/10")
    return lower    

def uppercase(password, upper):
    count = 0
    for i in password:
        if i.isupper():
            count +=1
    if count > 3:
        upper +=10
    elif count <=3 and count >=2:
        upper +=7
    elif count <= 1 and count >0:
        upper+=5
    else:
        upper = 0
        print("Password should contain atleast 1 uppercase character!")
    print(f"Score for password containing uppercase characters: {upper}/10")
    return upper 

def special(password, special_char):
    count = 0
    special_chars = '''!@#$%^&*()_+-=[]{}|;:',.<>?/'''
    for i in password:
       if i in special_chars:
            count +=1
    if count > 2:
        special_char +=10
    elif count <=2 and count >=1:
        special_char +=7
    else:
        special_char = 0
        print("Password should contain atleast 1 special character!")
    print(f"Score for password containing special characters: {special_char}/10")
    return special_char 



password = input("Enter your password: ")
leng = upper = lower = special_char = digit = 0
score = 0.0 
le = length(password, leng)
time.sleep(1.5)
u = uppercase(password, upper)
time.sleep(1.5)
lo = lowercase(password, lower)
time.sleep(1.5)
sc = special(password, special_char)
time.sleep(1.5)
di = digits(password, digit)
time.sleep(1.5)
print("Calculating password strength", end = "")
for i in range(3):
    time.sleep(1)
    print(".", end = "")
time.sleep(1)
print()
score = (le + u + lo + sc +di)/5
print(f"Final password strength score: {score}/10")
if score >= 8:
    print("You are secure!!")
elif score > 5 and score <8:
    print("Could be better!")
else:
    print("Not safe!") 

