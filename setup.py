from setuptools import setup, find_packages

setup(
    name="global_macro_data",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
    ],
    author="Yangbo Wang",
    author_email="wangyangbo2003@gmail.com",
    description="Global Macro Data",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Yangbo-Wang/global_macro_data",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
