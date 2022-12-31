import struct, socket

def BuildMagicPacket(hwa: bytes) -> bytes:
    '''
    Build magic packet
    '''
    return b'\xff' * 6 + hwa * 16

def SendMagicPacket(msg: bytes, broadcast, wol_port: int) -> None:
    '''
    Send packet to broadcast address
    '''
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    for i in broadcast:
        soc.sendto(msg, (i, wol_port))
    soc.close()

def WakeOnLan(ethernet_address: str, broadcast: list[str], wol_port: int = 9) -> None:
    # Construct 6 byte hardware address
    add_oct = ethernet_address.split(':')
    
    if len(add_oct) != 6:
        raise Exception('\n*** Illegal MAC address\nMAC should be written as 00:11:22:33:44:55\n')
    
    hwa = struct.pack('BBBBBB', int(add_oct[0],16),
        int(add_oct[1],16),
        int(add_oct[2],16),
        int(add_oct[3],16),
        int(add_oct[4],16),
        int(add_oct[5],16))

    msg = BuildMagicPacket(hwa)

    SendMagicPacket(msg, broadcast, wol_port)

def main() -> None:
    broadcast = ['192.168.1.255']
    
    WakeOnLan('F4:B5:20:45:01:2A', broadcast)

if __name__ == '__main__':
    main()

