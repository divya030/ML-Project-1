from setuptools import setup , find_packages
from typing import List

# Declaring variables for the setup function 

Project_Name = "Housing Predictor"
Version = "0.0."
Author = "Aparna"
Description = "First ML Project"
Requirement_file_name = "requirements.txt"


def get_requirements_list()->List[str]:  ## returns a list in str datatype as mentioned.
    """ 
    Description : This function returns the list of requirement 
    mentined in requirements.txt file (libraripes mentiones in it)

    """
    with open (Requirement_file_name) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name = Project_Name,
version = Version,
author = Author,
description = Description,
packages = find_packages(),
install_requires = get_requirements_list()


)