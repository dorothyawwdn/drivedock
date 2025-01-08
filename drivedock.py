import os
import subprocess
import platform

class DriveDock:
    def __init__(self):
        if platform.system() != "Windows":
            raise EnvironmentError("DriveDock is only compatible with Windows operating systems.")
        
    def list_drives(self):
        """Lists all drives on the system."""
        drives = [f"{d}:\\" for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f"{d}:\\")]
        return drives

    def optimize_drive(self, drive_letter):
        """Optimizes the specified drive."""
        try:
            subprocess.run(["defrag", drive_letter, "/O"], check=True)
            print(f"Drive {drive_letter} optimized successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to optimize drive {drive_letter}. Error: {e}")

    def check_drive_errors(self, drive_letter):
        """Checks the specified drive for errors."""
        try:
            subprocess.run(["chkdsk", drive_letter, "/F"], check=True)
            print(f"Drive {drive_letter} checked for errors successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to check drive {drive_letter} for errors. Error: {e}")

    def get_drive_info(self, drive_letter):
        """Retrieves information about the specified drive."""
        try:
            output = subprocess.check_output(["fsutil", "volume", "diskfree", drive_letter], text=True)
            print(f"Drive {drive_letter} information:\n{output}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to retrieve drive {drive_letter} information. Error: {e}")

if __name__ == "__main__":
    dock = DriveDock()
    drives = dock.list_drives()
    print("Available Drives:", drives)
    
    # Example usage
    if drives:
        dock.optimize_drive(drives[0])
        dock.check_drive_errors(drives[0])
        dock.get_drive_info(drives[0])