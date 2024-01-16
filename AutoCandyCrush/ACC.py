import os
import subprocess
import win32com.shell.shell as shell
from time import sleep

enable = 'netsh interface set interface "Ethernet" enabled'
disable = 'netsh interface set interface "Ethernet" disabled'


def main():
    openCandy()
    # press play
    closeCandy()
    # copy stuff to folder
    Ethernet(disable)
    sleep(1)
    openCandy()
    # press play
    # enter level
    # use the special bombs till win
    # press next or ok or whatever
    closeCandy()
    Ethernet(enable)
    openCandy()
    # press play
    closeCandy()


# enable\disable Ethernet
def Ethernet(command=enable):
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+command)


# Open Candy Crush Saga
def openCandy():
    os.system('start CandyCrushSaga:')


# Close Candy Crush Saga
def closeCandy():
    subprocess.call(["taskkill", "/F", "/IM", "candycrushsaga.exe"])



