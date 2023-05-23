![alt text](https://github.com/vasil-lyubenov/serve_and_protect/blob/main/logo.png?raw=true)

Serve And Protect
This Python script detects a specific sequence of key presses (A-Z-I-S by default) and displays a desktop notification when the sequence is detected and lock your workplace so they can't continue with further shit.

- Requirements
This script requires Python 3 and the following Python packages:

pynput: for detecting key presses
plyer: for displaying desktop notifications

- Installing Python and pip
Before you can run this script, you need to have Python and pip (the Python package installer) installed on your system.

Python

Python can be downloaded from the official website. Download the latest version and run the installer. Make sure to check the box that says "Add Python to PATH" during the installation.

pip

pip is included as standard with Python versions 3.4 and later, so if you've installed Python from the official website, you should already have pip. You can check by opening a command prompt and typing:

```
pip --version
```

If pip is installed, this will display the version number. If not, you will need to install pip manually.

Installing Required Packages
Once you have Python and pip installed, you can install the required packages using pip.

Open a command prompt and type the following commands:

```
pip install pynput
pip install plyer
```

Running the Script
With the necessary packages installed, you can run the script by navigating to the directory where the script is located and running the following command:

```
python serveAndProtect.py
```

Replace serveAndProtect.py with the actual name of the script file.

Customizing the Script
The key sequence that the script looks for is defined in the sequence list. You can change the sequence to any sequence of keys you like.

Please replace the script name and sequence of keys according to your needs.