import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WebScrapingForAll", 
    version="0.0.1",
    author="Mauricio Arango",
    author_email="arangoi2@illinois.edu",
    description="A simple set of tools to make web scarping easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marangoisa/WebScrapingForAll",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
