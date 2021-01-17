import setuptools
 
with open("ReadMe.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="dictRysan",
 
    #version of the module
    version="1.4.6",
 
    #Name of Author
    author="Rafsan Jany",
 
    #Email address
    author_email="rafsanjany1213@gmail.com",
 
    #Small Description about module
    description="dictionary",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    
    url="https://github.com/RafsanJany-44/Python-packages/tree/master/dictRysan/",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)