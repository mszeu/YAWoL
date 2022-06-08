# WoL
Wake-on-Lan magic packet generator

**wakeup** is a simple python script that generates and sends a Wake-on-Lan magic packet to the specified MAC address

The script is given **AS IS** and it is under the **AGPL Aferro license 3.0**.

For more information about the license terms please refer tot the **LICENSE** file distributed with the project.
## Usage

**wakeup.py** **MACAddress** [**--port** port]
- **MACAddress**: is the MAC address of the appliance to wake up (e.g.: *0011223344AF*)
- **--port**: the destination of the magic packet. If is not specified the default is 7 

## Example

**wakeup.py** 0011223344AF **--port** 9
