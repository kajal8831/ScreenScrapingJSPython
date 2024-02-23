--1) First install python and pip

To install Python and pip, you can follow these steps:

Installing Python:
Download Python:
Visit the official Python website at https://www.python.org/downloads/ and download the latest version of Python for your operating system (Windows, macOS, or Linux).

Run the Installer:
Run the downloaded installer. During installation, make sure to check the box that says "Add Python to PATH" (this is important for accessing Python from the command line).

Install Python:
Follow the installation wizard's instructions to complete the installation. Once it's finished, Python should be installed on your system.

Verify Installation:
Open a command prompt (Windows) or terminal (macOS/Linux) and type the following command to verify that Python has been installed successfully:

bash
Copy code
python --version
You should see the installed Python version.

Installing pip:
Download get-pip.py:
Open your web browser and go to https://bootstrap.pypa.io/get-pip.py. Right-click on the page and select "Save As" to download the file. Save it in a location you can easily access.

Run the Script:
Open a command prompt (Windows) or terminal (macOS/Linux), navigate to the directory where you saved get-pip.py, and run the following command:

bash
Copy code
python get-pip.py
This will install pip.

Verify Installation:
To check if pip has been installed, run the following command:

bash
Copy code
pip --version
You should see information about the installed pip version.

Now you have Python and pip installed on your system, and you can use them to manage packages and run Python scripts.


--2) Install Flash and selenium

bash
Copy code
pip install Flask selenium

--3) Download chrome driver for your chrome version 

visit url https://chromedriver.chromium.org/downloads

https://googlechromelabs.github.io/chrome-for-testing/

I downloaded this zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.69/win64/chromedriver-win64.zip

After this extract the folder, it must have chromedriver.exe

Make sure chrome and chrome driver versions are compatible with each other and selenium is also upgraded

--4) Run your code on cmd

Navigate to your directory using cmd and fire command

python app.py