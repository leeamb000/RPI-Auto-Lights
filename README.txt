For information on all hardware and how to set it up for the project to function properly, see Report. Two PIR sensors attached to GPIO 14 and 15, and 1 Smart Plug, are required for the code to run with minimum modifications. The IP address of the Smart Plug will need to be changed to the IP address of the user's Smart Plug in lines 45 and 74 of the code. 

The following command will install the python-kasa library:
pip install python-kasa==0.4.0.dev0

If the RPI.GPIO library is not already installed, the following command will install it:
sudo apt-get install RPi.GPIO