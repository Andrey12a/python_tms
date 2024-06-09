def check_dataa(email, password, users):
    for user in users:
        if user['email'] == email:
            if user['password'] == password:
                return True
