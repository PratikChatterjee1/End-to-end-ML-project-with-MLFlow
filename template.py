import os
from pathlib import Path
import logging  # We need to see the logs in our terminal

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s') #information level logging with error message and time stamp


project_name = "mlProject"  
# we can name any as our choice. First a src folder will be created and inside that the mlproject will be creating all the components

#__init__ files are the constructor files, these are going to be my local package and everytime 
# I need the constructor file to make the folder as my local package, 
# because everytime I want to import something from these folder, hence we need to keep the constructor files ready.

list_of_files = [

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",   
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "template/index.html"
]

# line 43 ==in windows \ slash does not work and we need \ slash, hence we need to change it. We use this Path to make the isses resolve.
# line 43# we are seperating the folders and files
for filepath in list_of_files:
    filepath = Path(filepath)  
    filedir, filename = os.path.split(filepath)  

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")