
build: 
	npm run build --prefix "./src/"
watch: 
	npm run watch --prefix "./src/"
compile:
	pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" -n "IRacingDirector" app.py