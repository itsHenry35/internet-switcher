import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

# Function to execute the disable command
def disable_internet():
    result = subprocess.run(["netsh", "interface", "ip", "set", "address", "name=本地连接", "source=dhcp"], capture_output=True, text=True)
    disable_result = result.stdout

    result = subprocess.run(["netsh", "interface", "ip", "set", "dns", "name=本地连接", "source=dhcp"], capture_output=True, text=True)
    disable_result += "\n" + result.stdout

    messagebox.showinfo("Disable Result", disable_result)

# Function to execute the enable command
def enable_internet():
    def verify_password():
        password = password_entry.get()
        if password == "@Angqwer1":
            password_window.destroy()

            result = subprocess.run(["netsh", "interface", "ip", "set", "address", "name=本地连接", "source=static", "addr=10.121.145.234", "mask=255.255.255.0", "gateway=10.121.144.1", "gwmetric=1"], capture_output=True, text=True)
            enable_result = result.stdout

            result = subprocess.run(["netsh", "interface", "ip", "set", "dns", "name=本地连接", "source=static", "addr=114.114.114.114"], capture_output=True, text=True)
            enable_result += "\n" + result.stdout

            result = subprocess.run(["netsh", "interface", "ip", "add", "dnsservers", "name=本地连接", "address=10.121.145.1", "index=2"], capture_output=True, text=True)
            enable_result += "\n" + result.stdout

            messagebox.showinfo("Enable Result", enable_result)
        else:
            messagebox.showerror("Error", "Invalid password")

    # Create the password verification window
    password_window = tk.Toplevel(window)
    password_window.title("Password Verification")

    # Create the password label and entry in the verification window
    password_label = ttk.Label(password_window, text="Password:")
    password_label.pack()
    password_entry = ttk.Entry(password_window, show="*")
    password_entry.pack()

    # Create the verify button in the verification window
    verify_button = ttk.Button(password_window, text="Verify", command=verify_password)
    verify_button.pack()

# Create the main window
window = tk.Tk()
window.title("Internet Switcher")

# Create the disable button
disable_button = ttk.Button(window, text="Disable", command=disable_internet)
disable_button.pack()

# Create the enable button
enable_button = ttk.Button(window, text="Enable", command=enable_internet)
enable_button.pack()

# Start the Tkinter event loop
window.mainloop()
