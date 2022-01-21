# from setuptools import setup, find_packages
import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='miniparser',
    version = '0.0.6',
    author = 'wbwqq',
    description= 'A simple and easy to use python command line argument parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/wbwqq/miniparser',
    project_urls = {
        "Bug Tracker" : 'https://github.com/wbwqq/miniparser/issues',
    },
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'':'miniparser'},
    py_modules=['miniparser'],
    python_requires=">=3.6",
)