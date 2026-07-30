from angel_login import login

try:
    smart, session = login()
    print("Angel One Login Successful")
    print(session)
except Exception as e:
    print("Login Failed")
    print(e)
