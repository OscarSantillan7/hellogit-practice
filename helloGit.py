import os
import json
import sys

class HelloGit:

    def __init__(self,userName, userPassword):

        self.userName = userName
        self.userPassword = userPassword
    
    def helloUser(self):

        return f"Hello {self.userName}"

def userPassword():

    while True:

        try:

            userPassword = int(input("Enter a numerical password: "))

            if (len(str(userPassword))) != 6:

                print("Invalid password, try again")
            
            else:

                print("Valid Password")
                break
            
        except ValueError:
            
            print(f"{userPassword}is not valid")
        
        return userPassword
    
password = userPassword()


if __name__ == "__main__":

    hiG = HelloGit("Oscar",password)
    hiG.helloUser()

