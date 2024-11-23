import os
import subprocess
import zipfile
import shutil  # To copy files from one directory to another
import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import sys
import venv


# Function to show the welcome message at the start
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


# Function to create and activate a virtual environment
def create_virtualenv():
    env_dir = "env"
    if not os.path.exists(env_dir):
        print("Creating virtual environment...")
        venv.create(env_dir, with_pip=True)
    else:
        print("Virtual environment already exists.")
    install_dependencies(env_dir)


# Function to install dependencies in the virtual environment
def install_dependencies(env_dir):
    pip_path = os.path.join(env_dir, "bin", "pip") if sys.platform != "win32" else os.path.join(env_dir, "Scripts", "pip.exe")
    print("Installing dependencies...")
    subprocess.check_call([pip_path, "install", "wget"])


# Function to download DepotDownloader
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


# Function to extract the downloaded zip file and delete it afterward
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


# Function to prompt for Steam credentials
def get_steam_credentials():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask for username and password
    SteamUsername = simpledialog.askstring("Steam Username", "Enter your Steam username:")
    if not SteamUsername:
        messagebox.showerror("Error", "Username is required.")
        exit()

    SteamPassword = simpledialog.askstring("Steam Password", "Enter your Steam password:", show="*")
    if not SteamPassword:
        messagebox.showerror("Error", "Password is required.")
        exit()

    # Escape double quotes in the username and password
    SteamUsername = SteamUsername.replace('"', r'\"')
    SteamPassword = SteamPassword.replace('"', r'\"')

    return SteamUsername, SteamPassword


# Function to select the directory where files will be downloaded
def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    selected_directory = filedialog.askdirectory(title="Select the directory to save the download")
    if not selected_directory:
        messagebox.showerror("Error", "Directory selection is required.")
        exit()
    return selected_directory


# Function to ensure DepotDownloader is executable before running
def ensure_depotdownloader_executable():
    depotdownloader_path = "./DepotDownloader/DepotDownloader"

    # Ensure the DepotDownloader binary is executable (on Unix-like systems)
    if sys.platform != "win32":
        subprocess.check_call(["chmod", "+x", depotdownloader_path])
        print("DepotDownloader is now executable.")
    return depotdownloader_path


# Function to run DepotDownloader
def run_depotdownloader(SteamUsername, SteamPassword, FILE):
    payday2_dir = os.path.join(FILE, "PAYDAY 2 Project White House")
    if not os.path.exists(payday2_dir):
        os.makedirs(payday2_dir)
        print(f"Created directory: {payday2_dir}")

    # Ensure DepotDownloader is executable
    depotdownloader_path = ensure_depotdownloader_executable()

    # Set the command to run DepotDownloader
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

    # Log the command for debugging purposes
    print(f"Running command: {command}")

    # Run the DepotDownloader command
    subprocess.run(command)


# Function to clone the GitHub repository and copy its contents
def clone_and_copy_mods():
    repo_url = "https://github.com/MatthewCAbel/Project-White-House-Mods"
    clone_dir = "Project-White-House-Mods"
    payday2_dir = os.path.join(os.getcwd(), "PAYDAY 2 Project White House")

    # Clone the repository using git
    print(f"Cloning repository: {repo_url}")
    subprocess.check_call(["git", "clone", repo_url, clone_dir])

    # Copy contents of the cloned repo to the PAYDAY 2 Project White House folder
    if not os.path.exists(payday2_dir):
        os.makedirs(payday2_dir)
        print(f"Created directory: {payday2_dir}")

    # Copy the contents of the cloned repo into the PAYDAY 2 directory
    print(f"Copying contents from {clone_dir} to {payday2_dir}...")
    for item in os.listdir(clone_dir):
        s = os.path.join(clone_dir, item)
        d = os.path.join(payday2_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print("Cloning and copying complete.")

    # Delete the cloned repository after copying the contents
    print(f"Deleting the cloned repository folder: {clone_dir}")
    shutil.rmtree(clone_dir)
    print(f"Deleted folder: {clone_dir}")


# Function to show the final message
def show_final_message():
    final_message = (
        "Done! Please add the Project White House EXE file as a non-Steam game and use the same Proton version you use in vanilla Payday 2. Thank you for playing Project White House!"
    )
    messagebox.showinfo("Project White House - Installation Complete", final_message)


# Main function to orchestrate the script
def main():
    # Show welcome message at the start
    show_welcome_message()

    env_dir = "env"

    # Create and activate virtual environment
    create_virtualenv()

    # Download DepotDownloader
    download_depotdownloader(env_dir)

    # Extract the zip file
    extract_zip()

    # Select download directory
    FILE = select_directory()

    # Get Steam credentials
    SteamUsername, SteamPassword = get_steam_credentials()

    # Run DepotDownloader for the first time
    run_depotdownloader(SteamUsername, SteamPassword, FILE)

    # Run DepotDownloader again to ensure files are valid
    print("\nRe-running DepotDownloader to validate the downloaded files...")
    run_depotdownloader(SteamUsername, SteamPassword, FILE)

    # Clone the repo and copy the contents to the PAYDAY 2 folder
    clone_and_copy_mods()

    # Show final message when the script is done
    show_final_message()


if __name__ == "__main__":
    main()
