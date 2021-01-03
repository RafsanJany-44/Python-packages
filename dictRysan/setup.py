import setuptools

with open("ReadMe.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="dictRysan",
 
    #version of the module
    version="1.1.0",
 
    #Name of Author
    author="Rafsan Jany",
 
    #Email address
    author_email="rafsanjany1213@gmail.com",
 
    #Small Description about module
    description="dictionary : searching,sorting,reading and writting json file",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/RafsanJany-44/Python-packages/tree/master/dictRysan/",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

