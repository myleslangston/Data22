import os

working_directory = os.getcwd()  # current worker directory


def return_user_id():
    print(os.getuid())


def operating_system_information():
    print(os.uname())  # returns details about the operating system


