# Bulk File Rename Tool 


## Description

Have you ever faced the hassle of renaming dozens — or even hundreds — of files manually ?
It’s time-consuming, boring, and prone to human error. This is where **Bulk File Rename Tool** comes to the rescue !

**Bulk File Rename Tool** is a simple yet powerful desktop application built with **Python + PyQt** that helps you rename multiple files in a folder **in seconds**. Whether you’re organizing personal photos, Python scripts, or any type of file — this tool can save you hours of work.



## Key Features
**Smart Renaming:** Rename files using a custom prefix + automatic numbering.

**File Filtering:** Works great with images, Python files, or any extension you want.

**Responsive UI:** Powered by PyQt threads to avoid GUI freezing during renaming.

**Built with Qt Designer:** Clean and intuitive interface for maximum productivity.

**Pathlib Integration:** Handles files and folders in a clean, cross-platform way.



## Project Structure
```
 ./rprename_project/
│
├── rprename/
│   │
│   ├── ui/
│   │   ├── __init__.py      # enables ui/ as a Python package.
│   │   ├── window.py        # contains the Python code for the application’s main window. ( generated using pyuic5 )
│   │   └── window.ui        # holds a Qt Designer file that contains the code for the application’s main window in XML format.
│   │
│   ├── __init__.py          # enables rprename/ as a Python package.
│   ├── app.py               # enables rprename/ as a Python package.
│   ├── rename.py            # provides the file renaming functionalities.
│   └── views.py             # provides the application’s GUI and related functionalities.

│
├── README.md
├── requirements.txt
└── rprenamer.py             # provides an entry-point script to run the application.


```





## Steps to Build The Application

**1** - Build the GUI manually using **Qt Designer**.

**2** - Using pyuic5 to **translate .ui files to .py files**.
 
**3** - Create the PyQT **Skeleton Application** - the root folder.

**4** - Modify these files to make the application functions as desire : **rprename/_int_.py, rprename/views.py, rprename/app.py, rprenamer.py**.




## How to Run

**1** - Clone the source code into your PC.

**2** - Open you preferred IDE (**Visual Studio Code recommended**).

**3** - Open the project folder, then open the terminal .

**4** - Create a virtual environment :
<pre lang="markdown"> 
 bash python -m venv ./venv 
 source venv/bin/activate # **On macOS/Linux** 
 venv\Scripts\activate # **On Windows** </pre>


**5** - Install required dependencies :
`pip install requirements.txt`    
[If you got an error, try `pip install PyQt5 `] 


**6** - Run the application :
`python rprenamer.py`










