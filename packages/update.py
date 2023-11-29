#["upd", "packages.update", ["upd"]]
# Made By Blurple
import os, sys, requests, threading, time

url = "https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/"
filenames = [
    "builtin.py",
    "calc.py",
    "filemanager.py",
    "filemanip.py",
    "hangman.py",
    "nano.py",
    "netget.py",
    "notebook.py",
    "pip.py",
    "randomquote.py",
    "reminder.py",
    "system_info.py",
    "test.py",
    "top.py",
    "update.py",
    "vault.py"
]

fileList = [f"{url}{filename}" for filename in filenames]

def download_and_save(url):
    r = requests.get(url)
    #print(r.text)
    fileInstallingCreator = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.basename(url))
    with open(fileInstallingCreator, "w") as newFile:
        newFile.write(r.text)
    print("\n")

def upd(command):
    print("Programs to download:")
    for prg in fileList:
        print(prg)
    print(f"To path: {os.path.dirname(os.path.realpath(__file__))}\nPress enter to continue")
    input()

    print("Downloading and saving files:")
    
    threads = []
    for url in fileList:
        thread = threading.Thread(target=download_and_save, args=(url,))
        threads.append(thread)
        thread.start()
    text = ""
    # Display loading animation
    while any(thread.is_alive() for thread in threads):
        for _ in range(len(threads)):
            text += "."
            print(text+"\r", end="", flush=True)
            time.sleep(0.5)
    
    print("\nAll files downloaded and saved!")
