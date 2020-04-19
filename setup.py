import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piapy",
    version="0.1.2",
    author="Javier Garcia",
    author_email="javier.garcia.d@gmail.com",
    description="Python wrapper for PIA VPN desktop client command line interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bskapital/piapy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
