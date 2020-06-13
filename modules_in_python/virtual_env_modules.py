# When we work with many projects we usually need the same packages in different versions.
# If we would install the same package globally with different version we will overwrite

# To have a specific packages for specific projects we have to use VIRTUAL ENVIRONMENT:
# https://docs.python.org/3/library/venv.html

# Type in terminal:
#   python3 -m venv NAME_OF_NEW_ENV_FOLDER__OR__PATH_TO_IT

# Next we have to activate this new environment by typing in a console (on Linux/Unix):
#   source env/bin/activate

# WINDOWS:
# VSCode asked me if I want to use this Env for a project. Runned file use this Env.
# But terminal didn't switched and packages are installed globally...
# We have to change Execution Policy to let Python run a script.
# In PowerShell type:
#   Set-ExecutionPolicy - ExecutionPolicy RemoteSigned - Scope CurrentUser
# Next run a file from a Virtual Env folder:
#   .\VirtualEnvProject\Scripts\Activate.ps1

# We should see in a PowerShell a name of an active Environment on the begining.
# Then, any package we will install will be installed on this Env (not globally)

# REQUIREMENTS.txt
# To save packages required to the project, in activated virtualEnv, type in PowerShell:
#   pip freeze > requirements.txt
# (name of this file is a common convention)

# if we won't be in vEnv this command will save our globally installed packages

# Other developers could install our project's packages by running in console:
#   pip install -r requirements.txt

# To leave virtualEnv we should type in PowerShell/terminal:
#   deactivate