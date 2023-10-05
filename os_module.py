import os

def observe_system_info():
    print(f"CPU Cores: {os.cpu_count()}")
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"Logged-in User: {os.getlogin()}")

observe_system_info()
