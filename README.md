# DeanLab_Data_Aquisition

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

4. 
# Run the program

First you'll need to establish a connection to the desired instruments by running Load_Instruments.py.

Then run Main.py
  
  
