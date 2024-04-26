'''This file is needed to set basic variables
This file is very important!'''


import yaml

with open('../about.yaml', 'r') as about0:
	about = yaml.load(about0, Loader=yaml.FullLoader)


version = about.get("version")
appname = about.get("appname")
