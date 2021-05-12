#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
getrequests = 0 # counter for GET
postrequests = 0 # counter for POST

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            print(f"User IP: {line.split()[-1]} failed to login")
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        if "GET" in line:
            getrequests += 1
        if "POST" in line:
            postrequests += 1
print("The number of failed log in attempts is", loginfail)

print("The number of GET requests are", getrequests)

print("The number of POST requests are", postrequests)
