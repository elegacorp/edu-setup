# Project Edu Setup

### How to Use

Form a project file in .txt format that contains a board name on the first line, followed by modules and clips formatted like the below.

``` 
Board Name: [Course Name] Fundamentals

1 - Introduction
Overview
Clip One
Clip Two
Clip Three
Conclusion

2 - Another Module
Yet Another Clip
Getting One More Clip
This is a Test Clip
Demo: What If There Was a Demo?
Conclusion 
```

In the root of the project, update the .env file to include the full file path to the course outline .txt file.

Example: `PROJECT_PATH="c:\mydir\course_outline.txt"`

On the command line, execute the command for the script from the main folder directory.

` python scripts/project_setup.py `

### About

This project is used for initialization of a Trello board when beginning work on a new Pluralsight course. project_setup.py generates all of the default work card names needed for the course to be managed in Trello.

(c) Copyright 2018-2023 Elega Corporation. This project is licensed under the MIT License and is therefore able to be used for personal or commercial use - see LICENSE.txt for full licensing verbiage.