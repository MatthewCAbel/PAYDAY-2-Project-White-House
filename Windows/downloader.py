import os
import subprocess
import shutil
import zipfile
from tkinter import Tk, filedialog, simpledialog, messagebox
from pathlib import Path
import sys
import venv

def ensure_requests_installed():
    try:
        import requests
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
    return requests

requests = ensure_requests_installed()

def create_virtual_env():
    venv_dir = Path("venv")
    venv.create(venv_dir, with_pip=True)

def download_depot_downloader():
    url = "https://github.com/SteamRE/DepotDownloader/releases/latest/download/DepotDownloader-windows-x64.zip"
    zip_name = "DepotDownloader-windows-x64.zip"
    extract_dir = Path("DepotDownloader")

    print("Downloading Depot Downloader...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(zip_name, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        print("Download complete.")

        extract_dir.mkdir(exist_ok=True)
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print("Depot Downloader extracted to:", extract_dir)

        os.remove(zip_name)
        print("Zip file removed.")
    else:
        raise Exception("Failed to download Depot Downloader.")

    return extract_dir

def get_installation_folder():
    Tk().withdraw() 
    folder = filedialog.askdirectory(title="Select installation folder")
    if not folder:
        raise Exception("No folder selected.")
    project_folder = os.path.join(folder, "PAYDAY 2 Project White House")
    os.makedirs(project_folder, exist_ok=True)
    print(f"Project folder created: {project_folder}")
    return project_folder

def get_steam_credentials():
    Tk().withdraw() 
    username = simpledialog.askstring("Steam Username", "Enter your Steam username:")
    if not username:
        raise Exception("No username entered.")
    password = simpledialog.askstring("Steam Password", "Enter your Steam password:", show='*')
    if not password:
        raise Exception("No password entered.")
    return username, password

def run_depot_downloader(depot_downloader_path, project_folder, username, password):
    if not depot_downloader_path.exists():
        raise Exception("Depot Downloader is not extracted correctly.")

    command = [
        str(depot_downloader_path / "DepotDownloader.exe"),
        "-app", "218620",
        "-depot", "218621",
        "-manifest", "8140332499591716770",
        "-username", username,
        "-password", password,
        "-dir", project_folder
    ]

    print("Running Depot Downloader...")
    process = subprocess.Popen(command, stdin=subprocess.PIPE, text=True)
    process.communicate(input="\n")
    process.wait()
    if process.returncode != 0:
        raise Exception("Depot Downloader encountered an error.")
    print("Depot Downloader complete.")

def clone_and_copy_repo(project_folder):
    repo_url = "https://github.com/MatthewCAbel/Project-White-House-Mods.git"
    clone_path = Path("PWH Mods")

    print("Cloning GitHub repository...")
    subprocess.run(["git", "clone", "--branch", "wolfhud", repo_url, str(clone_path)], check=True)

    items_to_copy = ["WSOCK32.dll", "mods", "assets"]
    for item_name in items_to_copy:
        item_path = clone_path / item_name
        if item_path.exists():
            dest = Path(project_folder) / item_name
            if item_path.is_dir():
                shutil.copytree(item_path, dest, dirs_exist_ok=True)
            else:
                shutil.copy2(item_path, dest)
            print(f"Copied {item_name} to the project folder.")
        else:
            print(f"{item_name} not found in the repository.")

def main():
    print("Welcome to Project White House!\n\n"
          "This script will download version 197.2 of PAYDAY 2 and then install our modpack automatically "
          "into your game folder.\n\n"
          "You will need to enter your Steam credentials in order to download the game files from Depot Downloader. "
          "This information will ONLY be sent to Steam's servers. Please see the Depot Downloader GitHub page for more information.\n\n"
          "You will need to respond to two Steam Guard prompts during the install process.")

    create_virtual_env()

    depot_downloader_path = download_depot_downloader()

    project_folder = get_installation_folder()
    
    username, password = get_steam_credentials()
    
    run_depot_downloader(depot_downloader_path, project_folder, username, password)
    run_depot_downloader(depot_downloader_path, project_folder, username, password)

    clone_and_copy_repo(project_folder)

    messagebox.showinfo("Done!", "Done! Please add the Project White House EXE file as a non-Steam game to play and rename it on steam to play.\n"
                                 "Thank you for playing Project White House!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        print(f"Error: {e}")
