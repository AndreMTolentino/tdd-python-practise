# TDD-ON-PRACTISE

The objective of this project was to create an object that allows adding fractions following the steps of Fundamentals of High-Discipline TDD Course (https://online-training.jbrains.ca/courses/wbitdd-01/lectures/34779823).

The course was originally built in Java Language, so this is an adaption for those who wants to follow the steps of Test-First-Programming using Python Language.


## Course Organization

The course is divided in 5 lectures, each one with nearly 30 min of time. On this git, there is a commit related to each class.

* First Lecture: https://online-training.jbrains.ca/courses/wbitdd-01/lectures/133490
* Second Lecture: https://online-training.jbrains.ca/courses/wbitdd-01/lectures/133486
* Third Lecture: https://online-training.jbrains.ca/courses/wbitdd-01/lectures/133487
* Fourth Lecture: https://online-training.jbrains.ca/courses/wbitdd-01/lectures/133488
* Fifth Lecture: https://online-training.jbrains.ca/courses/wbitdd-01/lectures/133489


## Pre-requisites

The version of python used to build this code was 3.10, however I think any version of python > 3 will run.

You can install pystest library to run all the tests.
```bash
pip install pytest
```


## Run Tests

To see the test running, open the terminal, and write:
```bash
pytest
```

To specify a file, just write the path after the command. Example:
```bash
pytest scripts/tests/test_unit.py 
```
