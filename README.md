# UMS

Interact UMS programmatically using a simple Python Library.
Allows User to View User profile, Annoucement, Messages, Datesheet, grades, marks termwise etc.

Do fork and star ⭐ this repository if you like it.

## Contents

- [ Getting Started ](#getting-started)
- [ Methods / Functions ](#Methods)

  - [ User Profile ](#user-profile)
  - [ Announcements ](#announcements)
  - [ Messages ](#Messages)
  - [ Grades ](#Grades)
  - [ Marks ](#Marks)
  - [ Classes ](#Classes)
  - [ Datesheet ](#datesheet)

- [ Contribute ](#contribute)

---

## Getting Started

Install this package from pypi

```
$ pip install ums
$ python
>>> from ums import User
>>>
```

---

## Methods

## `See All User Methods/Functions`

### User Profile

- To get User detail
- function Name : `user_profile()`
- This function takes no argument
- This function return a `Dictionary` Object
  - `data` : user detail
    - `Name` : Name of the User ( dict object )
      - `Full Name` : Fullname of User
      - `First Name` : First name
      - `Middle Name` : Middle name ( if available )
      - `Last Name` : Last Name ( if available )
    - `RegNo` : Registration Number of user
    - `Rollno` : Roll Number of User
    - `Term` : Current Term
    - `Group` : Class Group
    - `Section` : Class section
    - `Programme` : User Programme Name
    - `Book Issued` : Number of Book user issued from University Library
  - `datetime` : timestamp when data is generated

#### Usage

```python
from ums import User

regno = < REGISTRATION NUMBER >
password = < PASSWORD >
user = User(registration=regno, password=password)

profile = user.user_profile()
print(profile)
```

---

### Announcements

- To get all recent annoucements
- Function name : `announcements()`
- This function takes no argument
- This function returns a `Dictionary` object
  - `data` : list of all announcement
    - `id` : Annoucement Id
    - `title` : Title of the announcement
    - `body` : Main body of the annoucement
    - `media` : list of media attached to the announcement ( if any )
  - `datatime` : timestamp when data is generated

#### Usage

```python
from ums import User

regno = < REGISTRATION NUMBER >
password = < PASSWORD >
user = User(registration=regno, password=password)

announcements = user.annoucements()
print(annoucements)
```

---

### Messages

- To get all the recent messages
- Function name : `messages()`
- This function takes no argument
- This function return a `Dictionary` object
  - `data` : list of all messages
    - `id` : Message Id
    - `subject` : Subject of message
    - `body` : Main body of the message
    - `date` : date of message when published
  - `datetime` : timestamp when data is generated

#### Usage

```python
from ums import User

regno = < REGISTRATION NUMBER >
password = < PASSWORD >
user = User(registration=regno, password=password)

messages = user.messages()
print(messages)
```

---

### Grades

- To get Termwise grade
- Function name : `grades()`
- This function takes no argument
- This function return a `Dictionary` Object
  - `data` : List of Different term
    - `term` : term / semester number
    - `tgpa` : term / semester tgpa
    - `grades` : List of grades of all subject of that term
      - `course` : Course name
      - `grade` : grade in that course
  - `datetime` : timestamp when data is generated

#### Usage

```python
from ums import User

regno = < REGISTRATION NUMBER >
password = < PASSWORD >
user = User(registration=regno, password=password)

grades = user.grades()
print(grades)
```

---

### Marks

- To get Termwise Marks
- Function name : `marks()`
- This function takes no argument
- This functiom return a `Dictionary` Object
  - `data` : List of different term
    - `termid` : term id
    - `courses` : list of diffeent courses of that term
      - `course` : Name of the course
      - `marks` : list of different marks of that course
        - t`ype : type of mark
        - `marks` : list of marks out of different scheme
  - `datetime` : timestamp when data is generated

#### Usage

```python
from ums import User

regno = < REGISTRATION NUMBER >
password = < PASSWORD >
user = User(registration=regno, password=password)

marks = user.marks()
print(marks)
```

---

### Classes

- To get all classes of current Day
- Function name : `classes()`
- This function takes no argument
- This function return a `Dictionary` Object
  - `data` : List of different Courses
    - `course` : Course name
    - `timing` : class timing
    - `platform` : Class platform
    - `status` : current class status of that course
  - `datetime` : timestamp when data is generated

#### Usage

```python
from ums import User

regno = < REGISTRATION NUMBER >
password = < PASSWORD >
user = User(registration=regno, password=password)

classes = user.classes()
print(classes)
```

---

### Datesheet

- To get Upcoming Exam Sheet ( if available )
- Function name : `datesheet()`
- This function takes no argument
- This function return a `Dictionary` Object
  - `data` : List of different courses
    - `id` : Id
    - `c_code` : Course Code
    - `course` : Course name
    - `report` : Reporting timing
    - `date` : Exam date
    - `timing` : Exam timing
  - `datetime` : timestamp when data is generated

#### Usage

```python
from ums import User

regno = < REGISTRATION NUMBER >
password = < PASSWORD >
user = User(registration=regno, password=password)

datesheet = user.datesheet()
print(datesheet)
```

---

## Contribute

- This Project is open for contibution, feel free to contibute new feature, requests and bug fixes
- To contibute fork this repository
- Bug fix / new feature / Optimization :
  - Create a new branch
  - Makes changes to that branch, create a new Pull request and describe your fixes or addition of new feature
- Feature request :
  - Create a new Issue with tag `new feature` and describe your feature you want in upcoming version

---

Made with 💜 in India
