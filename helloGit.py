import os
import json
import sys

class HelloGit:

    def __init__(self,userName):

        self.userName = userName
    
    def helloUser(self):

        return f"Hello {self.userName}"

if __name__ == "__main__":

    hiG = HelloGit("Oscar")
    hiG.helloUser()

