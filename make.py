# coding=UTF8

# Make into the build folder database scripts. Parameters:
# - config profile from the config file

# TODO: more customized: config module profiles 

import config, codecs, sys
reload(config)
from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("src", encoding="utf-8"))

# Config parameters
con = config.__getattribute__(sys.argv[1])

# Create build folder
buildFolder = con["buildfolderprefix"]+"-"+sys.argv[1]
if not os.path.exists(buildFolder):
    os.makedirs(buildFolder)

# Recreate folder structure
for root, dirs, files in os.walk("src"):
    for d in dirs:
        if not os.path.exists(buildFolder+'/'+d):
            os.makedirs(buildFolder+'/'+d)

# Create additional folders
if "createfolders" in con:
    for folder in con["createfolders"]:
        folderPath = buildFolder+"/"+folder
    
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)

# Build from sources        
for root, dirs, files in os.walk("src"):
    destRoot = buildFolder+root.lstrip("src")
    for f in files:
        template = env.get_template(root.lstrip("src")+"/"+f)
        fout = codecs.open(destRoot+"/"+f, "w", "utf-8")
        fout.write(template.render(c=con))
        fout.close()


# # TODO: Handle Jinja2 exceptions properly: jinja2.exceptions.TemplateNotFound
