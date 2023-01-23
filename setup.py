from setuptools import setup, find_packages

setup(
    name='github_sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.24.0'
    ],
    author='Indra Nand Jha',
    author_email='indranandjha0@gmail.com',
    url='https://github.com/indranandjha1993/github_sdk',
    license='MIT',
    description='A Python SDK for interacting with the GitHub API',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
