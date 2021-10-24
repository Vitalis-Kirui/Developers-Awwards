# Developers' Awwards.

## Author

[**Kipyegon Kirui Vitalis**](https://github.com/Vitalis-Kirui)

## Description

A Django application that allows users to share their projects and recieve ratings from other users. Links to the live projects are provided and one can the live app/site.

## Live Link

[View Site](https://vitalis-awwards.herokuapp.com/)

## User Story

* User can signup & signin to the application
* User can post projects they have worked on
* Current user is able to view their profile page with the projects they posted
* User is able to view other users posted projects and rate them
* When user clicks on a single project it navigates to another page where user is able to view the details of the project and rate it
* User is able to search for different projects

## API Endpoints

* [Profiles Endpoints](https://vitalis-awwards.herokuapp.com/api/v1/profile)
* [Projects Endpoints](https://vitalis-awwards.herokuapp.com/api/v1/projects)

## Prerequisites

You need the following to start working on this project: On your local system; 

1. Python3.8
2. Django
3. Pip
4. Virtual Environment(virtualenv)
5. A text editor

## Development Installation

To get the code..

1. Clone the repository:
 `git clone  https://github.com/Vitalis-Kirui/Developers-Awwards.git`

2. Move to the folder and install requirements
 ` cd Developers Awwards-`

3. In the projects root directory, install the virtualenv library using pip and create a virtual environment. Run the following commands respectively:
    - **`pip install virtualenv`**
    - **`virtualenv venv`**
    - **`. venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
4. Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
5. Launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    - To upload photos as admin, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.
6. Run tests by running the command **`python3.8 manage.py test awwards`**

## Technology used

* [Python3.8](https://www.python.org/)
* [Django](https://docs.djangoproject.com)
* [Heroku](https://heroku.com)
* Git
* Bootstrap 4.3.1

## Known Bugs

* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [vitaliskirui1@gmail.com]

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright © 2021  [Kipyegon Kirui Vitalis](https://github.com/jLuseno161)