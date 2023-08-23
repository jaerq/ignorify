from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="ignorify",
    version="0.1.0",
    author="Jaer Quijivix-Sweeney",
    author_email="jaer.q@protonmail.com",
    description="A Python library for filtering files and directories based on patterns.",
    license="GPL-3.0",
    license_files=("LICENSE"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaerq/ignorify",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
