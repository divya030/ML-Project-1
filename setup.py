from setuptools import setup 
from typing import List

# Declaring variables for the setup function 

Project_Name = "Housing Predictor"
Version = "0.0.1"
Author = "Aparna"
Description = "First ML Project"
Packages=["housing"]
Requirement_file_name = "requirements.txt"


def get_requirements_list()->List[str]:  ## returns a list in str datatype as mentioned.
    """ 
    Description : This function returns the list of requirement 
    mentined in requirements.txt file (libraries mentiones in it)

    """
    with open (Requirement_file_name) as requirement_file:
        return requirement_file.readlines()


setup(
name = Project_Name,
version = Version,
author = Author,
description = Description,
packages = Packages,
install_requires = get_requirements_list()


)