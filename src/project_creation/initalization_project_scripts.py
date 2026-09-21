"""Author: Manjeet Kumar
Date: 2024-06-20
Description: This script initializes a new Python project with a standard structure, virtual environment, and basic configurations.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, cwd=None):
    """Run a shell command and handle errors."""
    try:
        subprocess.check_call(command, shell=True, cwd=cwd)
        print(f"✅ Command succeeded: {command}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {command}")
        print(f"Reason: {e}")
        sys.exit(1)


def create_project_structure(root, project_name):
    project_root = Path(root) / project_name
    project_root.mkdir(parents=True, exist_ok=True)

    # Basic folders
    (project_root / "src").mkdir(exist_ok=True)
    (project_root / "tests").mkdir(exist_ok=True)

    # __init__.py inside src
    (project_root / "src" / "__init__.py").touch()

    print(f"📂 Project structure created at {project_root.resolve()}")
    return project_root


def create_virtualenv(project_root):
    venv_path = project_root / ".venv"
    run_command(f"{sys.executable} -m venv {venv_path}")
    print(f"🌀 Virtual environment created at {venv_path}")
    return venv_path


def create_requirements(project_root):
    requirements = ["requests", "numpy", "pandas"]
    req_file = project_root / "requirements.txt"
    req_file.write_text("\n".join(requirements))
    print(f"📄 requirements.txt created with default packages")
    return req_file


def install_packages(venv_path, req_file):
    pip_path = (
        venv_path / "Scripts" / "pip" if os.name == "nt" else venv_path / "bin" / "pip"
    )
    run_command(f"{pip_path} install -r {req_file}")
    print("📦 Packages installed successfully")


def create_gitignore(project_root):
    gitignore_content = """
# Virtual environment
.venv/
venv/
env/

# Python cache
__pycache__/
*.pyc

# OS files
.DS_Store
Thumbs.db
    """
    (project_root / ".gitignore").write_text(gitignore_content.strip())
    print("📝 .gitignore file created")


def initialize_git(project_root):
    run_command("git init", cwd=project_root)
    run_command("git add .", cwd=project_root)
    run_command('git commit -m "Initial project setup"', cwd=project_root)
    print("🌱 Git repository initialized with first commit")


def main():
    if len(sys.argv) < 3:
        print("Usage: python setup_project.py <path> <project_name>")
        sys.exit(1)

    root = sys.argv[1]
    project_name = sys.argv[2]
    print(f"🚀 Setting up project '{project_name}' at '{root}'...")
    project_root = create_project_structure(root, project_name)
    venv_path = create_virtualenv(project_root)
    req_file = create_requirements(project_root)
    install_packages(venv_path, req_file)
    create_gitignore(project_root)
    initialize_git(project_root)

    print("🎉 Project setup complete!")


if __name__ == "__main__":
    print("Starting project initialization script...")
    main()
