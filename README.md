# MarioPuppeteer
### A Flask based web-app to play Mario remotely.

To run the program, you must have the NES emulator FCEUX installed on your machine, 
with a playable ROM of Super Mario Bros, and a python version of 3.6 or later.  
  
While the game is running, run the lua script read.lua through the emulator. 
Then, navigate to the `app` directory on the command line and run the python program itself with the command: 

    flask run
    

Open any browser and type the ip-address of the computer that the program is running on and 
the port number provided by the program.  
  
For example:

    123.456.7.8:8000
    
- - -
