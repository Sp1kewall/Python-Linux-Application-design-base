'''Данный файл нуджен для установки базовых переменных
Этот файл очень важен!'''


import yaml

with open('../about.yaml', 'r') as about0:
	about = yaml.load(about0, Loader=yaml.FullLoader)


version = about.get("version")

appname = about.get("appname")

update = about.get("update")