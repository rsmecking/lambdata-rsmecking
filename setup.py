

# setup.py

from setuptools import find_packages, setup

from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rsmecking-lambdata",
    version="2.55",
    author="Ryan Mecking",
    author_email="rsmecking@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/rsmecking/lambdata-rsmecking",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)