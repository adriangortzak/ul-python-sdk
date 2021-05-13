from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2"]

setup(
    name="",
    version="0.1.0",
    author="Adddrian",
    author_email="addegor95@gmailcom",
    description="Unofficial client for the UL API",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MPL-2.0",
    url="https://github.com/Adddrian/ul-api-python-client",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
)
