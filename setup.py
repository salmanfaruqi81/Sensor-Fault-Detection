from webbrowser import get
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:

    """
    This Function will return List of Requirements
    """
    
    requirement_list:List[str] = []

    return requirement_list


setup(

    name = "Sensor",
    version = "0.1",
    author = "Salman Faruqi",
    author_email = "salmanfaruqui@hotmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)



