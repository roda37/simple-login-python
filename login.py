import json
count = 0
jsonF = 'userdata.json'
try:
    with open(jsonF) as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}
query = str(input("Do you have an account?"))
if query == "y" or query == "Y":
    while count < 3:
        username = str(input("Enter your username"))
        password = str(input("Enter your password"))
        with open('userdata.json') as json_file:
            data = json.load(json_file)
            if data[str(username)] == password:
                print("Welcome, " + username)
                break
            else:
                print("The username and password do not match, try again")
                count += 1
else:
    print("Let's create a new account")
    new_username = str(input("Enter your new username"))
    new_password = str(input("Enter your new password"))
    data[new_username] = new_password
    with open('userdata.json', 'w') as fp:
        json.dump(data, fp, indent=2)
