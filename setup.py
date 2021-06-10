'''
Author     : knight-byte ( Abunachar )
File       : setup.py
'''
# --------IMPORTS -------
import setuptools

# -------- SETUP ---------
with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="ums",
    packages=["ums"],
    version="0.1.0",
    description="LPU UMS api for exacting user data like Profile, annoucement, messages, Timetable, Grades etc.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/knight-byte/Ums",
    download_url="https://github.com/knight-byte/Ums/archive/v0.1.0.tar.gz",
    author="Abunachar Yeahhia",
    author_email="abunachar1236@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords=["lpu ums", "ums", "student",
              "university management system", "university", "lpu"],
    install_requires=["bs4", "requests", "lxml"],
)
