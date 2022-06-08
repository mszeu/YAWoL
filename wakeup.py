# Minimal and Simple Wake-on-Lan utility by Marco S. Zuppone - msz@msz.eu
# This utility is released under AGPL 3.0 license
# please refer to the LICENSE file for more information about licensing
# and to README.md file for more information about the usage of it

import argparse
import socket


def wol(lunaMacAddress: bytes, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    magic = b'\xff' * 6 + lunaMacAddress * 16
    s.sendto(magic, ('<broadcast>', port))
    print("packet sent to:", lunaMacAddress.hex(), "port:",port)
    print("Magic packet:", magic.hex())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Sends the WoL magic packet to the specified MAC address",
        epilog="For any questions, feedback, suggestions, send money (yes...it's a dream I know) you can contact the "
               "author at msz@msz.eu")
    parser.add_argument("MACAddress", type=str,
                        help="The MAC Address of the Ethernet device to wake. Example: 0011223344AA")
    parser.add_argument("--port", type=int, default=7, help="The port where to send the magic packet")
    args = parser.parse_args()
    chars = set('0123456789abcdedABCDEF')
    if len(args.MACAddress) != 12 and not (all((c in chars) for c in args.MACAddress)):
        print("the MAC Address needs to be hexadecimal without spaces or signs between one byte and the other and the "
              "bytes need to be 6")
        exit()
    # pass to wol the mac address of the ethernet port of the appliance to wakeup
    wol(bytearray.fromhex(args.MACAddress), args.port)
    # bytearray.fromhex('')
