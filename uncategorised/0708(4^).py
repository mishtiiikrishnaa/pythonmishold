#asking username and password
#conditions: password to not contain username and username to be "Trident111"
user_name=input("enter user name: ")
password=input("enter password: ")
if password!="Trident111" and user_name in password:
        print("enter another password!")
else:
        print("proceeding.....")
