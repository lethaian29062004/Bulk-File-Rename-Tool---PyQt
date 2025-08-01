**rprenamer.py** - provides an entry-point script to run the application.



**rprename/ directory**

**__init__.py** - enables rprename/ as a Python package.
**app.py** - provides the PyQt skeleton application.
**rename.py** - provides the file renaming functionalities.
**views.py** - provides the application’s GUI and related functionalities.


**ui/ subdirectory**
Storing of GUI-related code
**__init__.py** - enables ui/ as a Python package.
**window.py** - contains the Python code for the application’s main window. 
(Generated using pyuic5)
**window.ui** - holds a Qt Designer file that contains the code for the application’s main window in XML format.

**Check If the Number in the required Files match with the encoding number





**HOW TO RUN**

```sh
python -m venv ./venv
.\venv\Scripts\Activate
pip install PyQT5
python rprenamer.py







-----------------------------------------------------------------------------------
**Steps to Build**
1 - Build the GUI manually using Qt Designer

2 - Using pyuic5 to translate .ui files to .py files.
 
3 - Create the PyQT Skeleton Application - the root folder

./rprename_project/
│
├── rprename/
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── window.py
│   │   └── window.ui
│   │
│   ├── __init__.py
│   ├── app.py
│   ├── rename.py
│   └── views.py
│
├── README.md
├── requirements.txt
└── rprenamer.py






4 - Add content to - rprename/_int_.py

5 - Add content to - rprename/views.py

6 - Add content to - rprename/app.py

7 - Add content to - rprenamer.py



8 -
'pathlib' - Manage file system path & rename files
