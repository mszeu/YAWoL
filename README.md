# WoL - Wake-on-Lan
Wake-on-Lan magic packet generator

## PROGRAM NAME
 **wakeup**
## VERSION

**1.0**

## DESCRIPTION
**wakeup** is a simple python script that generates and sends a Wake-on-Lan magic packet to the specified MAC address

The script is given **AS IS** and it is under the **AGPL Aferro license 3.0**.

For more information about the license terms please refer tot the **LICENSE** file distributed with the project.
## USAGE

**wakeup.py** **MACAddress** [**--port** port]
- **MACAddress**: is the MAC address of the appliance to wake up (e.g.: *0011223344AF*)
- **--port**: the destination of the magic packet. If is not specified the default is 7 

## EXAMPLE

**wakeup.py** 0011223344AF **--port** 9

## REQUIREMENTS
The program requires **Python 3**. It was tested and developed under **Python 3.10**

#Special thanks
&nbsp;

<a href="https://www.jetbrains.com/?from=WoL"><img src=jetbrains-variant-3.png width=100></a>May thanks to <a href="https://www.jetbrains.com/?from=WoL">JetBrains</a> for giving us the <b>Open Source License</b> for free with the full access to their developer suite.

## COPYRIGHT & LICENSE
  Copyright(C) 2022  Marco S. Zuppone - msz@msz.eu - https://msz.eu

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, either version 3 of the
  License, or any later version.

  This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   GNU Affero General Public License for more details.
   
   All the details on the license are available online 
   here https://www.gnu.org/licenses/agpl-3.0.en.html or in the 
   file COPYING.TXT included in this distribution.
