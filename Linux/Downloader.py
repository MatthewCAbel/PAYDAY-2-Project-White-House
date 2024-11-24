import os
import subprocess
import zipfile
import shutil  
import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import sys
import venv



def show_welcome_message():
    welcome_message = (
        "Welcome to Project White House!\n\n"
        "This script will download version 197.2 of PAYDAY 2 and then install our modpack automatically "
        "into your game folder.\n\n"
        "You will need to enter your Steam credentials in order to download the game files from Depot Downloader. "
        "This information will ONLY be sent to Steam's servers. Please see the Depot Downloader GitHub page for more information.\n\n"
        "You will need to respond to two Steam Guard prompts during the install process."
    )
    messagebox.showinfo("Welcome to Project White House!", welcome_message)



def create_virtualenv():
    env_dir = "env"
    if not os.path.exists(env_dir):
        print("Creating virtual environment...")
        venv.create(env_dir, with_pip=True)
    else:
        print("Virtual environment already exists.")
    install_dependencies(env_dir)



def install_dependencies(env_dir):
    pip_path = os.path.join(env_dir, "bin", "pip") if sys.platform != "win32" else os.path.join(env_dir, "Scripts", "pip.exe")
    print("Installing dependencies...")
    subprocess.check_call([pip_path, "install", "wget"])



def download_depotdownloader(env_dir):
    url = "https://github.com/SteamRE/DepotDownloader/releases/latest/download/DepotDownloader-linux-x64.zip"
    print("Downloading DepotDownloader...")

    python_path = os.path.join(env_dir, "bin", "python") if sys.platform != "win32" else os.path.join(env_dir, "Scripts", "python.exe")
    download_script = f"""
import wget
wget.download("{url}", "DepotDownloader-linux-x64.zip")
"""
    subprocess.check_call([python_path, "-c", download_script])
    print("\nDownload complete.")



def extract_zip():
    zip_file = "DepotDownloader-linux-x64.zip"
    print("Extracting DepotDownloader zip...")
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall("DepotDownloader")
    print("Extraction complete.")
    try:
        os.remove(zip_file)
        print(f"Deleted zip file: {zip_file}")
    except OSError as e:
        print(f"Error: Could not delete {zip_file}. {e}")



def get_steam_credentials():
    root = tk.Tk()
    root.withdraw() 

  
    SteamUsername = simpledialog.askstring("Steam Username", "Enter your Steam username:")
    if not SteamUsername:
        messagebox.showerror("Error", "Username is required.")
        exit()

    SteamPassword = simpledialog.askstring("Steam Password", "Enter your Steam password:", show="*")
    if not SteamPassword:
        messagebox.showerror("Error", "Password is required.")
        exit()

  
    SteamUsername = SteamUsername.replace('"', r'\"')
    SteamPassword = SteamPassword.replace('"', r'\"')

    return SteamUsername, SteamPassword



def select_directory():
    root = tk.Tk()
    root.withdraw()  
    selected_directory = filedialog.askdirectory(title="Select the directory to save the download")
    if not selected_directory:
        messagebox.showerror("Error", "Directory selection is required.")
        exit()
    return selected_directory


def ensure_depotdownloader_executable():
    depotdownloader_path = "./DepotDownloader/DepotDownloader"

    if sys.platform != "win32":
        subprocess.check_call(["chmod", "+x", depotdownloader_path])
        print("DepotDownloader is now executable.")
    return depotdownloader_path



def run_depotdownloader(SteamUsername, SteamPassword, FILE):
    payday2_dir = os.path.join(FILE, "PAYDAY 2 Project White House")
    if not os.path.exists(payday2_dir):
        os.makedirs(payday2_dir)
        print(f"Created directory: {payday2_dir}")

    
    depotdownloader_path = ensure_depotdownloader_executable()

    
    command = [
        depotdownloader_path,
        "-app", "218620",
        "-depot", "218621",
        "-manifest", "8140332499591716770",
        "-username", SteamUsername,
        "-password", SteamPassword,
        "-dir", payday2_dir,
        "-remember"
    ]

    
    print(f"Running command: {command}")

    
    subprocess.run(command)



def clone_and_copy_mods(FILE):
    repo_url = "https://github.com/MatthewCAbel/Project-White-House-Mods"
    clone_dir = "Project-White-House-Mods"

   
    print(f"Cloning repository: {repo_url}")
    subprocess.check_call(["git", "clone", repo_url, clone_dir])

    
    payday2_dir = os.path.join(FILE, "PAYDAY 2 Project White House")

  
    if not os.path.exists(payday2_dir):
        os.makedirs(payday2_dir)
        print(f"Created directory: {payday2_dir}")

    
    print(f"Copying contents from {clone_dir} to {payday2_dir}...")
    for item in os.listdir(clone_dir):
        s = os.path.join(clone_dir, item)
        d = os.path.join(payday2_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print("Cloning and copying complete.")

    
    print(f"Deleting the cloned repository folder: {clone_dir}")
    shutil.rmtree(clone_dir)
    print(f"Deleted folder: {clone_dir}")



def show_final_message():
    final_message = (
        "Done! Please add the Project White House EXE file as a non-Steam game and add the launch option from the SuperBLT website to load the mods correctly.You will also need to use the same proton version as you use in vanilla. Thank you for playing Project White House!"
    )
    messagebox.showinfo("Project White House - Installation Complete", final_message)



def main():

    show_welcome_message()

    env_dir = "env"

  
    create_virtualenv()

    
    download_depotdownloader(env_dir)

    
    extract_zip()


    FILE = select_directory()


    SteamUsername, SteamPassword = get_steam_credentials()

   
    run_depotdownloader(SteamUsername, SteamPassword, FILE)

   
    print("\nRe-running DepotDownloader to validate the downloaded files...")
    run_depotdownloader(SteamUsername, SteamPassword, FILE)

  
    clone_and_copy_mods(FILE)

   
    show_final_message()


if __name__ == "__main__":
    main()
