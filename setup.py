'''
Author: 饕餮
Date: 2021-12-23 21:23:03
version: 
LastEditors: 饕餮
LastEditTime: 2021-12-23 21:52:32
Description: setup
'''
from __future__ import print_function
from setuptools import setup,find_packages
import sys

setup(
    name="dongtai_sdk",
    version="0.0.2",
    author="spensercai",
    author_email="spensercai@gmail.com",
    description="DongTai SDK",
    long_description="DongTai SDK",
    license="MIT",
    url="https://github.com/HXSecurity/DongTai-SDK-Python",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[

    ],
    install_requires=[

    ],
    zip_safe=True,

)