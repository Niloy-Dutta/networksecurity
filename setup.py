from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements

    '''
    requirements_lst: List[str]= []

    try:
        with open('requirements.txt',mode='r') as file_obj:
            #Read lines from the file 
            lines = file_obj.readlines()
            #process each lines
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)

    except FileNotFoundError: 
        print('requirements.txt file not found!')
    
    return requirements_lst



setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Niloy Dutta Anik",
    author_email="niloydutta2525@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)