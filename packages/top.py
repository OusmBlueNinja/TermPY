# ["top", "packages.top", ["top"]]
# Made By OusmBlueNinja
import psutil

def top(command: list):
    if len(command) != 0:
        print("Usage: top")
        return

    try:
        print("Top Processes:")
        print("{:<8} {:<20} {:<10}".format("PID", "Name", "CPU (%)"))
        for process in get_top_processes():
            print("{:<8} {:<20} {:<10.2f}".format(process.pid, process.name(), process.cpu_percent(interval=1)))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def get_top_processes():
    # Get a list of processes sorted by CPU usage
    processes = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        processes.append(process)

    processes.sort(key=lambda x: x.cpu_percent(interval=1), reverse=True)
    return processes[:10]  # Display the top 10 processes by CPU usage

