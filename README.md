# MarioPuppeteer
### A Flask based web-app to play Mario remotely.

To run the program, you must have the NES emulator FCEUX installed on your machine, 
with a playable ROM of Super Mario Bros, and a python version of 3.6 or later.  

You can download the Windows version of the emulator [from here](https://fceux.com/web/home.html), or using your Linux package manager. While this project does work on the Linux version of the emulator, only the Windows version provides the RAM debugger.

While the game is running, run the Lua script `read.lua` through the emulator. 
Then, navigate to the `app` directory on the command line and run the python program itself with the command: 

    flask run

Make sure you have your `FLASK_APP` environment variable set correctly.  
You can do that by using the command:  

    export FLASK_APP=routes.py


Open any browser on the same network and type `localhost:` followed by the port number provided by the program.  

For example:

    localhost:5000
