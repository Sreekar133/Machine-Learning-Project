from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Sreekar"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:

    """
    Description : This function is going to return list of requirement mention in requirement.txt file

    return this function is going to return a list which contaon names of libraries mentionned in requirements
    """
    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description="This is the first FSDS Nov Batch Machine learning Project",
packages=find_packages(),
install_requires=get_requirements_list()
)


if __name__ =="__main__":
    print(get_requirements_list())