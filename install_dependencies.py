import subprocess
import sys
import os

def run(cmd, desc):
    print(f"🔧 {desc}...")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Failed: {desc}")
        sys.exit(1)
    else:
        print(f"Success: {desc}")

def main():
    print("Starting Raspberry Pi setup for garage-control project...\n")

    # 1. Update & install APT packages
    run("sudo apt update", "Updating package lists")
    run("sudo apt install -y python3 python3-pip python3-gpiozero python3-flask", "Installing Python packages via APT")

    # 2. Optional: Install RPi.GPIO (legacy fallback for gpiozero backends)
    run("sudo apt install -y python3-rpi.gpio", "Installing RPi.GPIO (for gpiozero)")

    # 3. Python packages via pip (in system environment)
    run("pip3 install flask --break-system-packages", "Installing Flask via pip")
    run("pip3 install --upgrade setuptools", "Upgrading setuptools")

    # 4. Enable SPI/PWM/etc. if needed (for future WS2812/ESP use)
    print("\nNOTE: If you're using PWM or SPI devices, run 'sudo raspi-config' → Interface Options → Enable as needed.")

    print("\nAll dependencies installed. You can now run:")
    print("    python3 app.py")
    print("\nVisit http://<pi-ip>:5000 in your browser.\n")

if __name__ == "__main__":
    main()

