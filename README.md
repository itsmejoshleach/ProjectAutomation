# Project Creation Automation Script

This Python script automates the process of setting up a new software project. It helps you quickly create a project with essential files, initialize a Git repository, and push it to GitHub. It supports multiple languages, including Python, Bash Shell, Flutter, and HTML/CSS/JS.

## Features

- Creates a project folder with the given name
- Generates a `README.md` file with the project name and description
- Adds a `LICENSE` file with MIT License content
- Creates a `.gitignore` file tailored to the selected programming language
- For Python projects:
  - Creates a virtual environment (`venv`)
  - Generates a `requirements.txt` file
  - Generates a `.env` file for environment variables
- Initializes a Git repository
- Creates an empty Git commit with the message `Root Commit`
- Creates an `Initial Setup` commit with the `README.md`, `LICENSE`, and `.gitignore` files
- Creates a GitHub repository and pushes the project to it

## Prerequisites

- Python 3.x
- Git
- GitHub CLI (`gh`)

Ensure you have the necessary tools installed:

- **Python**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **GitHub CLI**: [Download GitHub CLI](https://cli.github.com/)

You must also authenticate the GitHub CLI with your GitHub account. You can do this by running:
``` gh auth login```


## Installation
Clone this repository or download the script.

Install the required Python libraries (if any):

```pip install -r requirements.txt```

## Usage
Run the script with the following syntax:
``` python create_project.py <project_name> <description> <language>```

## Parameters:
project_name: Name of the project (e.g., My New Project)
description: Short description of the project
language: The programming language for the project. Valid options are:
Python
Bash
Flutter
HTML & CSS & JS
Example:
```python create_project.py "My Python Project" "This is a Python project" Python```
This will create a new Python project with the following structure:

README.md
LICENSE
.gitignore (with Python-specific rules)
requirements.txt
.env
venv/ (virtual environment)
A Git repository initialized
GitHub repository created and pushed