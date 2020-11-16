import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="appstore-reporter", # Replace with your own username
    version="1.0",
    author="Revanth Munirathinam",
    author_email="revanthm93@gmail.com",
    description="APPSTORE REPORTER helps to pull out sales and finance reports.",
    long_description="APPSTORE REPORTER helps to pull out sales and finance reports.",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/appstore-reporter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)