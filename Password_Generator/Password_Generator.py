import random
import string

#length of password
lengthOfPassword = int(input("Enter the length of Password: "))

#select the characters set
print(''' Select Characters you want to add in the Password form below (Can Select More then One) :
      1.Letters
      2.Special Characters
      3.Numbers
      4.Exit''')

characters = ""

#Adding character sets for our passwords
while (True):
    choice = int(input("Choose a number "))
    if(choice == 1):
        #adding Alphabets to our characterslist
        characters += string.ascii_letters

    elif(choice == 2):
        #adding Symbols to our characterslist
        characters += string.punctuation

    elif(choice == 3):
        #adding Numbers to our characterslist
        characters += string.digits
        
    elif(choice == 4):
        #Exiting the loop after selecting the character Set
        break
        
    else:
        print("Please pick a valid option!")
 
password = []

for i in range(lengthOfPassword):
    #picking random Characters
    randomchars=random.choice(characters)

    #Appending random characters to ur password
    password.append(randomchars)
    
#printing the password after join  all the random characters
print("Final Password is :" + "".join(password))
