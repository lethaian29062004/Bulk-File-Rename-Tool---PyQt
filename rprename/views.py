# -*- coding: utf-8 -*-

"""This module provides the RP Renamer main window."""

from collections import deque # deque = a double-ended queue
# deque 
# support append & pop operation from either side of the deque
# In this case, use a deque to store the paths of the files you need to rename.

from pathlib import Path
# Manage file system path & rename files



from PyQt5.QtCore import QThread
# Offload the file renaming process from the application's main thread.
# Prevent possible freezing GUI issues when selecting a big number of files to rename.


from PyQt5.QtWidgets import QFileDialog, QWidget
# QFileDiaglog - used to select files from the file system using predefined dialog



from .rename import Renamer # Renamer class from rename.py
from .ui.window import Ui_Window



FILTERS = ";;".join(
    
    (
        "PNG Files (*.png)",
        "JPEG Files (*.jpeg)",
        "JPG Files (*.jpg)",
        "GIF Files (*.gif)",
        "Text Files (*.txt)",
        "Python Files (*.py)",
    )
)




class Window(QWidget, Ui_Window):
    



    def __init__(self):
        super().__init__()
        self._files = deque() # ._files as a deque object - store the paths to the file you want to rename
        self._filesCount = len(self._files) # ._filesCount to store the number of files to rename
        self._setupUI()
        self._connectSignalsSlots() # call ._connectSignalsSlots().
        



    def _setupUI(self):
        self.setupUi(self)
        self._updateStateWhenNoFiles()
        
        
                
                
                
                
    # Handle the case - No files are loaded     
    # Also, for the case - the renaming process is done
    def _updateStateWhenNoFiles(self):
        self._filesCount = len(self._files)
        self.loadFilesButton.setEnabled(True)
        self.loadFilesButton.setFocus(True)
        
        # Disable the Rename Files button and clear the prefix edit field
        self.renameFilesButton.setEnabled(False)
        self.prefixEdit.clear()
        self.prefixEdit.setEnabled(False)
        






    def _connectSignalsSlots(self): 
        # This method will collect several signal and slot connections in a single place. 
        # Up to this point, the method connects the Load Files button’s .clicked() signal with the .loadFiles() slot. 
        # This makes it possible to trigger .loadFiles() every time the user clicks the button.
        self.loadFilesButton.clicked.connect(self.loadFiles)
        
        self.renameFilesButton.clicked.connect(self.renameFiles)
        
        
        self.prefixEdit.textChanged.connect(self._updateStateWhenReady)







    # When the line edit is empty, the button gets disabled, and otherwise it’s enabled. 
    def _updateStateWhenReady(self):
        if self.prefixEdit.text():
            self.renameFilesButton.setEnabled(True)
        else:
            self.renameFilesButton.setEnabled(False)
    
    
    
    
    
    
    
    
    
    def loadFiles(self):
        self.dstFileList.clear() # clears the .dstFileList list widget every time the user clicks Load Files.
        
        # A conditional statement checks if the Last Source Direectory is currently displaying any directory path 
        # If so, then the if code block sets the initial directory, initDir, to hold that path.
        # Otherwise, the initial directory is set to Path.home(), which returns the path to the current user’s home folder.
        if self.dirEdit.text(): 
            initDir = self.dirEdit.text()
        else:
            initDir = str(Path.home())
        
        
        # This method creates a dialog to allow user to select one or more files
        files, filter = QFileDialog.getOpenFileNames( #
            self, "Choose Files to Rename", initDir, filter=FILTERS
        )
        
        # A conditional statement that runs a bunch of statements if the user selects at least one file from the QFileDialog.
        if len(files) > 0: 
            fileExtension = filter[filter.index("*") : -1] # Slices the current filter string to extract the file extension.
            self.extensionLabel.setText(fileExtension) # Sets the text of the .extensionLabel object to the file extension extracted on previous line
            
            # Retrieves the paths to the directory containing the selected files, by creating a Path object using the path to the first file in the list of selected files.
            srcDirName = str(Path(files[0]).parent)
            self.dirEdit.setText(srcDirName) # sets the texts of the .dirEdit line edit to the directory path 
            
            # A 'for' loop iterates over the list of selected files
            # Creates a Path object for each file and appends it to the ._files 
            # Adds each file to the .srcFileList list widget.
            for file in files: 
                self._files.append(Path(file))
                self.srcFileList.addItem(file)
            self._filesCount = len(self._files) 
            self._updateStateWhenFilesLoaded()
            
    
    
    
    
    
    
    def _updateStateWhenFilesLoaded(self):
        self.prefixEdit.setEnabled(True)
        self.prefixEdit.setFocus(True)        
    
    
    
    
    
          
    def renameFiles(self):
        self._runRenamerThread()
        self._updateStateWhileRenaming()
        
    
    
    
    
    
    
     # This method disables the Load Files and Rename Files buttons while the renaming process is running.
    def _updateStateWhileRenaming(self):
        self.loadFilesButton.setEnabled(False)
        self.renameFilesButton.setEnabled(False)    
      
      
      
      
      
      
        
   
    def _runRenamerThread(self):
        prefix = self.prefixEdit.text()
        self._thread = QThread()
        self._renamer = Renamer(
            files=tuple(self._files),
            prefix=prefix,
        )
        self._renamer.moveToThread(self._thread)
        
        # Rename
        self._thread.started.connect(self._renamer.renameFiles)
        
        # Update state
        self._renamer.renamedFile.connect(self._updateStateWhenFileRenamed)
        self._renamer.progressed.connect(self._updateProgressBar)
        self._renamer.finished.connect(self._updateStateWhenNoFiles)
        
        # Clean up
        self._renamer.finished.connect(self._thread.quit)
        self._renamer.finished.connect(self._renamer.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        
        # Run the thread
        self._thread.start()







    
    def _updateStateWhenFileRenamed(self, newFile):
        
        # When a file is renamed, this method removes the file from the list of files to be renamed   
        self._files.popleft()
        # Updates the list of Files to Rename
        self.srcFileList.takeItem(0)
        # Updates the list of Renamed Files
        self.dstFileList.addItem(str(newFile))    
    
    
    
    
    
    
    
    
     # Compute the progress bar value - the current file number divided by the total number of files to rename
    def _updateProgressBar(self, fileNumber):
        progressPercent = int(fileNumber / self._filesCount * 100)
        self.progressBar.setValue(progressPercent)    




    