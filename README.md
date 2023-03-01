# VisualizerWeb

A webapp for visualizing machine learning algorithms.

## Run with Docker

1. Install Docker
2. Run Docker: `docker-compose -f "docker-compose.yml" up -d --build`
3. Check localhost:4000


## Development environment

Read the readme.md in the frontend and backend folder.


### Development outside of docker - additional hints: port adjustment necessary!!

Backend:
starting development server with debugger:

	install python (python installer from python homepage)

	install requirements:
	$ cd [path to backend folder)
	$ pip install --no-cache-dir -r requirements.txt
	
	start dev server with reload on changes:
	$ flask --app backend.py run --debug

	--> change files inside algo folder and schema folder

	--> server is listening on port 5000 !!!
	--> production server is listening on port 4001 (when started from docker)
	
Frontend: 
	change destination port for communication with backend:
		open frontend folder
		open in editor the file quasar.config.js
		goto build: {
      	 	env: {
        	  		 BACKENDURL: 'http://localhost:4001'
		replace 4001 with 5000
		save the file
	
	when development finished change it back before running docker-compose!!!
------------
	node.js version <18 und >=14 necessary for running the app code!!

	on windows: use cmd, not powershell (restriction policies prevent running scripts!)
	on Linux/Mac: read instructions in frontend/readme

[cmd]	> cd [path to frontend folder]
	> npm -g @quasar/cli
	> quasar dev				#will start the dev server (reload on change)

in case of problems when running quasar dev try to build the project:
	> quasar build
	> quasar dev
	

