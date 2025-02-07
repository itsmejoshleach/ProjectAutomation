# Project Creation Automation Script

This Python script automates the process of creating a new project with essential files, initializing a Git repository, and pushing it to GitHub. It supports multiple programming languages, including Python, Bash Shell, Flutter, and HTML/CSS/JS. The script also integrates GitHub authentication for easy repository creation.

## Features

- **Creates a Project Folder**: Generates a project folder with the provided name.
- **Generates Key Files**:
  - `README.md`: Project description.
  - `LICENSE`: MIT License by default.
  - `.gitignore`: Language-specific `.gitignore` rules (Python, Bash, Flutter, HTML/CSS/JS).
  - For Python projects:
    - `requirements.txt`: Template for Python dependencies.
    - `.env`: For environment variables like GitHub token.
    - `venv/`: Virtual environment folder.
- **Git Operations**:
  - Initializes a Git repository.
  - Creates an empty commit with the message `Root Commit`.
  - Adds and commits `README.md`, `LICENSE`, and `.gitignore` files with the message `Initial Setup`.
  - Creates and pushes a repository to GitHub automatically.
- **GitHub Authentication**: Uses a GitHub personal access token stored in a `.env` file for automatic authentication. If not present, the script prompts for login using the `gh` CLI.

## Prerequisites

Before using this script, ensure you have the following installed:

- **Python** (>=3.x): [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **GitHub CLI (`gh`)**: [Download GitHub CLI](https://cli.github.com/)

Additionally, you need to set up the GitHub CLI and authenticate with a personal access token (PAT). You can use the following command to log in:

gh auth login --with-token

Ensure you also install the python-dotenv package to load environment variables:
```pip install python-dotenv```

## Setup
Clone or download the script to your local machine.

Create a .env file in the same directory as the script with your GitHub token:

```GITHUB_TOKEN=your_github_personal_access_token```
Note: You can generate a personal access token from your GitHub account here.

Optionally, you can edit the .env file to configure defaults for your project creation, like the default language.

## Usage
To run the script, use the following command:

```python create_project.py <project_name> <description> <language>```

## Parameters:
- project_name: Name of the project (e.g., My New Project)
- description: A short description of the project (e.g., This is a Python project)
- language: The programming language to use for the project. The available options are:
- Python (default)
- Bash
- Flutter
- HTML & CSS & JS
Examples:
- Create a Python Project (default):
```python create_project.py "My Python Project" "A simple Python project"```
- Create a Flutter Project:
```python create_project.py "My Flutter App" "A mobile app using Flutter" Flutter```
- Create a Bash Project:
```python create_project.py "My Bash Scripts" "A collection of useful bash scripts" Bash```
- Create an HTML/CSS/JS Project:
```python create_project.py "My Web Project" "A website built with HTML, CSS, and JS" "HTML & CSS & JS"```

## What Happens When You Run the Script
The script creates a project folder with the provided name.
It generates the following files inside the project folder:
- README.md
- LICENSE (MIT license by default)
- .gitignore (configured for the selected language)

For Python projects, it also creates:
- requirements.txt (for dependencies)
- .env (to store environment variables like GitHub token)
- venv/ (virtual environment)

Initializes a Git repository.
Creates an empty commit with the message Root Commit.
Creates a GitHub repository (if you’re authenticated with GitHub) and pushes the project to GitHub.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting
GitHub Authentication: If the script fails to authenticate with GitHub, ensure that you have the correct personal access token in your .env file or that you're logged in using the GitHub CLI (gh auth login).
Dependencies: If you encounter missing dependencies, run pip install -r requirements.txt to install them.