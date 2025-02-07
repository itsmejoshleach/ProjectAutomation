import os
import sys
import subprocess
import shutil

def create_project(project_name, description, language):
    # Step 1: Create project folder
    os.makedirs(project_name, exist_ok=True)
    print(f"Created project folder: {project_name}")
    
    # Step 2: Create README.md file
    with open(os.path.join(project_name, 'README.md'), 'w') as readme:
        readme.write(f"# {project_name}\n\n{description}")
    print("Created README.md file")

    # Step 3: Create LICENSE file with MIT license
    with open(os.path.join(project_name, 'LICENSE'), 'w') as license_file:
        license_file.write("MIT License\n\nCopyright (c) 2025\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the 'Software'), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nauthors or copyright holders be liable for any claim, damages or other\nliability, whether in an action of contract, tort or otherwise, arising from,\nout of or in connection with the software or the use or other dealings in the\nSoftware.")
    print("Created LICENSE file")

    # Step 4: Create .gitignore file
    gitignore_content = ""
    if language == "Python":
        gitignore_content = "*.pyc\n__pycache__/\nvenv/\n.env\n"
    elif language == "Bash":
        gitignore_content = "*.sh~\n*.swp\n"
    elif language == "Flutter":
        gitignore_content = ".dart_tool/\nbin/\nbuild/\n*.iml\n"
    elif language == "HTML & CSS & JS":
        gitignore_content = "node_modules/\n*.log\n"
    with open(os.path.join(project_name, '.gitignore'), 'w') as gitignore:
        gitignore.write(gitignore_content)
    print("Created .gitignore file")

    # Step 5: Create language-specific files (Python)
    if language == "Python":
        # Create virtual environment
        subprocess.run(['python3', '-m', 'venv', os.path.join(project_name, 'venv')])
        print("Created virtual environment (venv)")
        
        # Create requirements.txt
        with open(os.path.join(project_name, 'requirements.txt'), 'w') as req_file:
            req_file.write("# Add dependencies here\n")
        print("Created requirements.txt")

        # Create .env file
        with open(os.path.join(project_name, '.env'), 'w') as env_file:
            env_file.write("# Add environment variables here\n")
        print("Created .env file")

    # Step 6: Initialize Git repo
    os.chdir(project_name)
    subprocess.run(['git', 'init'])
    print("Initialized git repository")

    # Step 7: Create empty commit ("Root Commit")
    subprocess.run(['git', 'commit', '--allow-empty', '-m', 'Root Commit'])
    print("Created empty commit: Root Commit")

    # Step 8: Create GitHub repository (Assuming authentication is done)
    repo_name = project_name.lower().replace(" ", "-")
    subprocess.run(['gh', 'repo', 'create', repo_name, '--private', '--remote', 'origin'])
    print(f"Created GitHub repository: {repo_name}")

    # Step 9: Create "Initial Setup" commit
    subprocess.run(['git', 'add', '--all'])
    subprocess.run(['git', 'commit', '-m', 'Initial Setup'])
    print("Created commit: Initial Setup")

    # Done
    print(f"Project {project_name} created and pushed to GitHub.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python create_project.py <project_name> <description> <language>")
        sys.exit(1)

    project_name = sys.argv[1]
    description = sys.argv[2]
    language = sys.argv[3]

    if language not in ["Python", "Bash", "Flutter", "HTML & CSS & JS"]:
        print("Invalid language. Choose from 'Python', 'Bash', 'Flutter', or 'HTML & CSS & JS'.")
        sys.exit(1)

    create_project(project_name, description, language)
