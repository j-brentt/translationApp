                          ______                      __      __  _                ___              
                         /_  __/________ _____  _____/ /___ _/ /_(_)___  ____     /   |  ____  ____ 
                          / / / ___/ __ `/ __ \/ ___/ / __ `/ __/ / __ \/ __ \   / /| | / __ \/ __ \
                         / / / /  / /_/ / / / (__  ) / /_/ / /_/ / /_/ / / / /  / ___ |/ /_/ / /_/ /
                        /_/ /_/   \__,_/_/ /_/____/_/\__,_/\__/_/\____/_/ /_/  /_/  |_/ .___/ .___/ 
                                                                                     /_/   /_/      
Author: Jordan Brent

Welcome to my Translation App!

# Intro
This application that I created utilizes Microsoft's translate API for translating from English to a variety of languages.

## Built with
- Python
- PyQt6
- Microsoft Azure
- Microsoft Translate API

### Warning
The API key included in the initial commits of this repository is **expired** and no longer functional. To run this project, you need to set up your own API key and configure it as an environment variable (`TRANSLATOR_API_KEY`).

## Instructions on running 
1. First ensure that your machine has intalled the latest version of Python.
   [Here's a quick guide.](https://www.datacamp.com/blog/how-to-install-python)

2. Next, make sure that the PyQt6 module is also installed, which is key to run the app
     ```py
   pip install PyQt6
   ```
3. Upon cloning the respository from GitHub, ensure to create a `.env` file in your root directory containing your Translate API key.
   This can be done as so,
      ```py
   TRANSLATOR_API_KEY=<your-api-key-here>
   ```
4. Next, run the translationApp.py file to bring up the UI and happy translating!     

   
### Contact Information
Email     - jabrent@icloud.com\
Repo Link - https://github.com/j-brentt/translationApp.git
