data=[]
print('\033[41m',"<<< WELCOME TO CRUD >>>",'\033[0m')
print("First You Creat your Account")
while True:
    print("1.Creat your acount\n2.Read Data\n3.Update your data\n4.deleate data\n5.Exit>")
    a=input("seleat your option:- ")
    if a=="1":
        print("Creat Acount") 
        name=input("Enter your name:- ")
        data.append(name)
        while True:
            
         num=(input("Enter your no:- "))
         if len(num)==10 and num.isdigit():
                data.append(num)
                break            
         else:
                print("your mobile number digits are worng")
        while True:        
         gmail=input("Enter your Gmail:- ")
         if "@gmail.com" in gmail:
                data.append(gmail)
                break
         else:
                print("Your gmail is wrong")
        while True:        
         password=input("Creat Your Password:- ")   
         if len(password)>=8 and len(password)<=12:
             if "A" in password or "a" in password or "B" in password or "b" in password or "C" in password or "c" in password or "E" in password or "e" in password or "F" in password or "f" in password or "G" in password or "g" in password or "H" in password or "h" in password or "I" in password or "i" in password or "J" in password or "j" in password or "K" in password or "k" in password or "L" in password or "l" in password or "M" in password or "m" in password or "N" in password or "n" in password or "O" in password or "o" in password or "P" in password or "p" in password or "Q" in password or "q" in password or "R" in password or "r" in password or "S" in password or "s" in password or "T" in password or "t" in password or "U" in password or "u" in password or "V" in password or "v" in password or "W" in password or "w" in password or "X" in password or "x" in password or "Y" in password or "y" in password or "Z" in password or "z" in password:
                if "@" in password or "#" in password or "$" in password or "&" in password:
                    if "0" in password or "1" in password or "2" in password or "4"  in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
                        data.append(password)    
                        print('\033[42m',"Your Account Creat Seccesfull>>",'\033[0m')
                        break                
         else:
            print("Your password is wrong")              

    elif a=="2":
        if not  data:
            print("Data Not Found ")
        else:
            while True:
                pass1=input("Enter your password: ")
                if pass1==data[3]:
                    print("Full Name:-",data[0])
                    print("Mobile Number:-",data[1])
                    print("Gmail ID:-",data[2])
                    print("Password:-",data[3])
                    break
                else:
                    print("Your Password Is Wrong Try Again")    
                  
    elif a=="3":
         if  not  data:
            print("Data Not Found")
            break
         print("1.Name\n2.Mobile Number\n3.Email ID\n4.Password")
         update=input("Which you want to Update:-")
         if update=="1":
            print("Update Your Name:- ")
            while True:
             pass2=input("Enter the Password:- ") 
             if pass2==data[3]:
                 name2=input("Enter Your New Name")
                 data[0]=name2
                 print(data)       
                 break
             else:
                 print("Your Password Is Wrong")
         elif update=="2":
            print("Update Your Mobile No>>")
            while True:
                pass3=input("Enter Your Password:- ")
                if pass3==data[3]:                    
                     number=input("Enter Your New Mobile Number:-")
                     if len(number)==10:
                       data[1]=number
                       print(data)
                       break
                     else:
                         print("Plese enter 10 digit Mobile Number")
                   
                else:
                    print("Your Password Wave is Wrong")
         elif update=="3":
            print("Update Your Email ID")
            while True:
                pass4=input("Enter Your Password:-")
                if pass4==data[3]:
                    email=input("Enter Your New Email ID:-")
                    if "@gmail.com" in email:
                     data[2]=email
                     print(data)
                     break
                    else:
                        print("Your Email ID is wrong wave")
                else:
                    print("Your Password is wrong")     
         elif update=="4":
            print("Update your Password")  
            while True:
                pass5=input("Enter Your Old Password:-")
                if pass5==data[3]:
                    newpass=input("Enter Your New Password:")
                    if len(password)>=8 and len(password)<=12:
                       if "A" in password or "a" in password or "B" in password or "b" in password or "C" in password or "c" in password or "E" in password or "e" in password or "F" in password or "f" in password or "G" in password or "g" in password or "H" in password or "h" in password or "I" in password or "i" in password or "J" in password or "j" in password or "K" in password or "k" in password or "L" in password or "l" in password or "M" in password or "m" in password or "N" in password or "n" in password or "O" in password or "o" in password or "P" in password or "p" in password or "Q" in password or "q" in password or "R" in password or "r" in password or "S" in password or "s" in password or "T" in password or "t" in password or "U" in password or "u" in password or "V" in password or "v" in password or "W" in password or "w" in password or "X" in password or "x" in password or "Y" in password or "y" in password or "Z" in password or "z" in password:
                         if "@" in password or "#" in password or "$" in password or "&" in password:
                            if "0" in password or "1" in password or "2" in password or "4"  in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
                                data[3]=newpass
                                print(data)
                                break
                    else:
                        print("Your New Password is Not Valied")            
                else:
                    print("Wrong PassWord ")
    elif a == "4":
        while True:
         if not data:
            print("Not Data Found")
            break
         while True:
            pass6 = input("Enter your password to delete your account: ")
            if pass6 == data[3]:
                data.clear()
                print("Your account has been deleted.")
                break
            else:
                print("Your Password is wrong. Try Again.")
    elif a=="5":
        print("EXIT TO CRUD >>")
        print("Thank you To Visit")
        break            
    else:
        print("You Must Select 1 to 5 options")
        print("Not use anthore Number")
        
                
