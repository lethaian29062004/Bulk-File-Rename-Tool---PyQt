# -*- coding: utf-8 -*-

"""This module provides the Renamer class to rename multiple files."""

import time
from pathlib import Path

# QObject  to create custom subclasses with custom signals & functionalities
# pyqtSignal create custom signals to emit when a given event occurs
from PyQt5.QtCore import QObject, pyqtSignal


class Renamer(QObject): # subclasses 'Renamer'
    # returns an integer representing the number of currently renamed file, this number is used to update the progress bar
    progressed = pyqtSignal(int) 
    # return the path to the renamed file to update the list of renamed files
    renamedFile = pyqtSignal(Path)
    finished = pyqtSignal()

    def __init__(self, files, prefix):
        super().__init__()
        self._files = files
        self._prefix = prefix
    # prefix - the name you want (optional)    
        
    # Building of the new file name (new_name + number + file extension)
    # enumerate - generate a file number as the loop goes
    def renameFiles(self):
        for fileNumber, file in enumerate(self._files, 1):
            newFile = file.parent.joinpath(
                f"{self._prefix}{str(fileNumber)}{file.suffix}"
            )
            file.rename(newFile)
            time.sleep(0.1) 
            self.progressed.emit(fileNumber)
            self.renamedFile.emit(newFile)
        self.progressed.emit(0)  # Reset the progress bar to zero after finished
        self.finished.emit()