
import os
import sys
import subprocess

def launch_ultron():
    print("=" * 40)
    print("       ULTRON AI LAUNCHER")
    print("=" * 40)

    print("Checking Python environment...")

    if sys.version_info < (3, 10):
        print("Please use Python 3.10 or newer.")
        return

    print("Starting ULTRON CORE...")

    subprocess.run(
        [sys.executable, "ultron_core.py"],
        check=False
    )

if __name__ == "__main__":
    launch_ultron()
