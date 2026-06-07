#asking username and password
#conditions: password to not contain username and username to be "Trident111"
user_name=input("enter user name: ")
password=input("enter password: ")
if password=="Trident111" and user_name not in password:
        print("proceeding....")
else:
        print("enter another password!")
