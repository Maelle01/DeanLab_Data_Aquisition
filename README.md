# DeanLab_Data_Acquisition

Python code to interface with instruments (write and read) throug a GUI for transport measurements and more!
Written by Maëlle Kapfer and Jordan Pack.

# Pre requisite

You will need to have python installed as well as diverse packages.
1. Install python through Anaconda https://www.anaconda.com.

2. Install libraries needed to run the program:
  PyQt5
  pyqtgraph
  
3. Download QCodes 

# List of files

1. Load_instruments.py: Establishes a connection with instruments, give instrument a name and select channels to record. Those information get recorded in the file Instruments.txt

2. Measurement_Instruments.py: Contains the function to communicate with instruments, such as changing output value and read measured value

3. Save.py: Formats the saved data into a .dat file with tabulation as delimitation. 

4. GUI_functions.py: Builds the GUI and contains sub-GUIs for specific instruments

5. Main.py: File to run to start the GUI

# Run the program

First you'll need to establish a connection to the desired instruments by running Load_Instruments.py.

Then run Main.py which will open a GUI to program and plot the measurement. The GUI is composed of:
1. A save tab. Tick the save box to save the measurement. Choose and filename and a folder to save the file in.
2. A note tab. The note will be added in the saved file before the header.
3. Real time data display. Tick the box to plot the desired data in the graphic part, change the color and get the real time output of selected instrument. To change the x-axis choose an output in the "X to plot" dropdown menu.
4. An Intruments tab: allows to control insutruments outside of loops (set an output on for example)
5. A Loop tab where measurement loops can be programmed
  
  
Note: the code is still being updated and new capabilities added.
