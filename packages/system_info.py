# ["system_info", "packages.system_info", ["os_info", "architecture_info", "memory_info"]]
# Made By OusmBlueNinja
import os
import platform
import psutil

def os_info(command: list):
    if len(command) != 0:
        print("Usage: os_info")
        return

    os_info = platform.system()
    print(f"Operating System: {os_info}")

def architecture_info(command: list):
    if len(command) != 0:
        print("Usage: architecture_info")
        return

    architecture_info = platform.architecture()
    print(f"System Architecture: {architecture_info[0]} {architecture_info[1]}")

def memory_info(command: list):
    if len(command) != 0:
        print("Usage: memory_info")
        return

    virtual_memory = psutil.virtual_memory()
    total_memory = virtual_memory.total / (1024 ** 3)  # Convert to GB
    used_memory = virtual_memory.used / (1024 ** 3)    # Convert to GB
    free_memory = virtual_memory.available / (1024 ** 3)  # Convert to GB

    print(f"Total Memory: {total_memory:.2f} GB")
    print(f"Used Memory: {used_memory:.2f} GB")
    print(f"Free Memory: {free_memory:.2f} GB")

# Example usage:
# os_info []
# architecture_info []
# memory_info []
