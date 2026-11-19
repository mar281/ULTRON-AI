
import platform
import sys

def show_system_info():
    print("=" * 40)
    print("       ULTRON SYSTEM INFORMATION")
    print("=" * 40)

    print("Operating System:", platform.system())
    print("OS Version:", platform.version())
    print("Machine:", platform.machine())
    print("Python Version:", sys.version)
    print("Architecture:", platform.architecture()[0])

    print("=" * 40)

if __name__ == "__main__":
    show_system_info()
