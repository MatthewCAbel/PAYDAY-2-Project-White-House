# PAYDAY-2-Project-White-House
A Steam Depot Downloader and mod pack download script for version 197.2 of PAYDAY 2. This also backports many weapon buffs from modern PAYDAY.

This script will download update 197.2 of PAYDAY 2 and install all of the mods in this repository automatically. You MUST own the game on your steam account for this to function.

It will ask for your Steam login credentials. This is needed for Depot Downloader to function. Please see here if you want to learn more: https://github.com/SteamRE/DepotDownloader

The mods repository can be found here: https://github.com/MatthewCAbel/Project-White-House-Mods

# Planned Features
Options for different HUDs during Installation

Backporting new weapons as custom ones

# Installation
Make sure you have Python3 (https://www.python.org/downloads/) and git (https://git-scm.com/downloads/win) installed on Windows. Please make sure you select the options to add them to your path when you install them (an option on the first page in the python installed, this should be the default for git). For Linux users, just install these through whatever means you use on your distro.

![392516163-5698294c-f2d5-47ba-a07d-25af37da5095](https://github.com/user-attachments/assets/a3f59a36-c670-4148-a9f0-2d199c293c81)
![image](https://github.com/user-attachments/assets/0f9d4337-ad63-4b80-9375-cb6b77c04c2e)

Download the script for your operating system from the releases page. Then run it through CMD (py downloader.py) for Windows (make sure you are in the same directory as the script) or your terminal (python Downloader.py) for Linux. (For the unaware, CMD can be opened in a folder on windows by "cd"ing to the folder address, typing "cmd" in the address bar in file explorer, or by holding shift and clicking the blank space in a folder then clicking "Open Command Prompt Here")

The script will ask you where to install the game, it will create a folder in the chosen location. It will then ask for your steam username and password. This info will ONLY go to Steam's servers, you can read it yourself if you're unsure about it. It will also ask for a steam guard authentication.

Once you login successfully, it will download the game. Once it downloads a first time, it will run depot downloader again to ensure there are no errors. It will ask for another steam guard authentication when it does this.

After this, it will download the mods from our GitHub repo and extract them to your game folder.

Once the install script is done, please add Project White House to steam as a non steam game and change the name. Once you've done this, you're ready to play.

# Credits
MatthewCAbel - General Project Manager, Install Script Coding, Balancing

icecowsun/Lettuce - Assistance with GitHub Page and Install Script

SteamRE - Depot Downloader - https://github.com/SteamRE/DepotDownloader

# Mod Credits

SuperBLT - SuperBLT Team - https://superblt.znix.xyz

Alphasort Mods - TdlQ - BLT - https://pd2mods.z77.fr/alphasort_mods.html

AutoDiscardParachute - octo - https://modworkshop.net/mod/45902

Automatically Equip ICTV Armor - Dr_Newbie - https://modworkshop.net/mod/35944

Basic Movement Undeploys Bipod - DeadmansChest - https://modworkshop.net/mod/19561

BeardLib - Simon, Luffy, Hoppip, Cpone - https://modworkshop.net/mod/14924

Buzzsaw 42 Belt Fix - Hinaomi - https://modworkshop.net/mod/31499

Celer - TdlQ - https://pd2mods.z77.fr/celer.html

Check for Wallbangs - vojin154 - https://modworkshop.net/mod/47414

Clear Texture Cache - TdlQ - https://pd2mods.z77.fr/clear_texture_cache.html

Clientsided Uppers - Powware - https://modworkshop.net/mod/29645

Custom FOV - Appii - https://modworkshop.net/mod/33680

Custom Preferred Masks - easternunit100 - https://modworkshop.net/mod/24888

Drag and Drop Inventory = TdlQ - https://pd2mods.z77.fr/drag_and_drop_inventory.html

Enable Restart on Crime Spree - Dr_Newbie - https://modworkshop.net/mod/31266

Enhanced Hitmarkers - TdlQ - https://pd2mods.z77.fr/enhanced_hitmarkers.html

Extra Profiles and Skill Sets - fragtrane - https://modworkshop.net/mod/26702

Grace doesn't kill civils - Dr_Newbie - https://modworkshop.net/mod/22987

Heist Specific Music in Crime Spree - Ludor Experiens - https://modworkshop.net/mod/23418

High Crime Spree Pack - sunny_bunny - https://modworkshop.net/mod/35789

Improved Offline Functionality - fragtrane - https://modworkshop.net/mod/25511

KSP 58 Belt Fix - Hinaomi, Krimzin - https://modworkshop.net/mod/27074

Less Aliasing - fugsystem - https://modworkshop.net/mod/37442

Less Inaccurate Weapon Laser - TdlQ - https://pd2mods.z77.fr/less_inaccurate_weapon_laser.html

Load Steam Inventory Once - Sora - https://modworkshop.net/mod/24008

Lobby Player Info -TdlQ - https://pd2mods.z77.fr/lobby_player_info.html

Mod List Lite - BangL - https://pdmods-arc.berigora.net/paydaymods.com/mods/551/mll.html

More Dozers (+2) - andole - https://modworkshop.net/mod/23776

More Weapon Stats - https://pd2mods.z77.fr/more_weapon_stats.html

No ADS Recoil Animations - Zdann - https://modworkshop.net/mod/25619

No Flashlight Glow - Offyerrocker - https://modworkshop.net/mod/22410 

No More Menu Filter - Cpone - https://modworkshop.net/mod/23119

No Screen Shake (Only on Shooting) - sydch, Mooshino - https://modworkshop.net/mod/22471

Perfect Viewmodel - Luffy - https://modworkshop.net/mod/17618

Refresh Rate Checker - TdlQ - https://pd2mods.z77.fr/refresh_rate_checker.html

Repeater Sights Tweak Updated - Dorpenka - https://modworkshop.net/mod/40958

Save My EXP! - Hoppip - https://modworkshop.net/mod/32685

Sensitivity Fixer - James L33 - https://modworkshop.net/mod/12823

Simple Seperate Save - naii_ - https://modworkshop.net/mod/37258

Snh20's Inverted Flashbang Glare - test1 - https://modworkshop.net/mod/27337

Steam over FBI - Literally the Crash - https://modworkshop.net/mod/20204

Stop crime spree crash on join - ◥◣Avocado◢◤ - https://modworkshop.net/mod/33165

The Fixes - Dom, andole - https://modworkshop.net/mod/23732

Vanilla More Heist Crime Spree Extended - SenpaiKillerFire - https://modworkshop.net/mod/27632

WolfHUD - Kamikaze94 - https://github.com/Kamikaze94/WolfHUD

# Mod Override Credits
Better Flashlight Texture - mut5r https://modworkshop.net/mod/31473

Chunky armor hitsounds mod - Fennikk - https://modworkshop.net/mod/25327

Enhanced Glass Cutting - Thesnowgato - https://modworkshop.net/mod/33593

HD NPC Weapon Model Replacements - Jarey_ - https://modworkshop.net/mod/34740

No Dirt Cameras - Kitsune Jimmy - https://modworkshop.net/mod/833

Original Bipods - >:3 - https://modworkshop.net/mod/28543

Reduced Sicaro Smoke - Jarey_ - https://modworkshop.net/mod/22674

Reinforcements Armor Regeneration Sound - Fennikk - https://modworkshop.net/mod/25337

Slightly Exaggerated Weapon Tracers - fugsystem - https://modworkshop.net/mod/25476

Visible power boxes - Kell S. - https://modworkshop.net/mod/27187

