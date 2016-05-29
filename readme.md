Basic chatbot boiler-plate
==========================

This boiler plate code has a basic bot developed using aiml with out of the box rest api support

Setup development environment
-----------------------------
1) install python (version 2.7.10).

    note:
    i) Versions 3.* do not go well with aiml package
    ii) make sure "pip" is also installed with python
    
2) install virtualenv using pip. This makes sure this project's dependencies are created locally

    pip install virtualenv
    
3) install git
4) clone this repo in a folder of your local system

    git clone <repo url>

5) activate the virtual environment

    cd cal
    source ENV/bin/activate
   
note: to deactivate the virtual environment

    (ENV)<user>$ deactivate

Running the code:
-----------------
Below are the command line parameters supported for main.py
   
    main.py	-r		:reload bot brain
            -o		:run in offline mode


#### With API
This mode runs the bot with a rest api at localhost

    (ENV)<user>$ python main.py

set the msg parameter either at
query string: *http://127.0.0.1:8080/bot/talk?msg=hi*
or body: *msg=hi*
    
#### Without API (offline mode)

offline mode doesn't spawn the rest api. Useful when debugging only the bot

in offline mode below commands are supported by the bot. these commands can be given to the bot as runtime input
    
    "quit" : exit
    "reload aiml": reloads the aiml into bot's 
    "save" :


    