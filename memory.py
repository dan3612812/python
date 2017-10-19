#!python2
from ctypes import *
from ctypes.wintypes import *
OpenProcess = windll.kernel32.OpenProcess
ReadProcessMemory = windll.kernel32.ReadProcessMemory
CloseHandle = windll.kernel32.CloseHandle

PROCESS_ALL_ACCESS = 0x1F0FFF
pid = 6224
address = 0x00E97074

buffer = c_char_p("The data goes here")
bufferSize = len(buffer.value)
bytesRead = c_ulong(0)

processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)

if ReadProcessMemory(processHandle, address, buffer, bufferSize, byref(bytesRead)):
    print("Success:", buffer)
else:
    print(buffer)
    print("Failed.")


CloseHandle(processHandle)
