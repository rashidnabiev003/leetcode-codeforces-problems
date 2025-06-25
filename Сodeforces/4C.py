n = int(input())
email_dict = {}

def dict_checker(email: str):
    new_email = ""
    if email in email_dict.keys():
        new_email = email + str(email_dict.get(email) + 1)
        email_dict[new_email] = 0
        email_dict[email] = email_dict.get(email) + 1
        return new_email
    else:
        email_dict[email] = 0
        return "OK"

for i in range(n):
    email = input()
    print(dict_checker(email))


