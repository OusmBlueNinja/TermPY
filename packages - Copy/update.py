#["upd", "packages.update", ["upd"]]
# Made By Blurple
import os, sys, requests, threading

fileList = [
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/builtin.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/echo.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/nano.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/netget.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/pip.py",
    "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/upd.py"
]

def download_and_save(url):
    r = requests.get(url)
    if 'Requests:' in r.text:
        print(r.text)
        print(r.headers['Content-Type'])
        fileInstallingCreator = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.basename(url))
        with open(fileInstallingCreator, "w") as newFile:
            newFile.write(r.text)

def upd(command):
    input(f"Settings: {fileList}, {os.path.dirname(os.path.realpath(__file__))}\nPress enter to continue")

    threads = []
    for url in fileList:
        thread = threading.Thread(target=download_and_save, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()