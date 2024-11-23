zenity --info --text "This script will automatically download PAYDAY 2 update 197.2 from Steam's servers then download all the mods from the Project White House Repo."

wget https://github.com/SteamRE/DepotDownloader/releases/latest/download/DepotDownloader-linux-x64.zip
unzip DepotDownloader-linux-x64.zip
rm DepotDownloader-linux-x64.zip

zenity --info --text "Please select where you would like to install Project White House"

FILE=`zenity --file-selection --directory --title="Select the install directory"`

zenity --info --text "$FILE Selected"

mkdir $FILE/"PAYDAY 2 Project White House"

SteamUsername=`zenity --forms  --add-entry="Username:" --text="Please enter your steam username"`

SteamPassword=`zenity --forms  --add-password="Username:" --text="Please enter your steam username. This information will only go to Steam's servers. Please check the Depot Downloader GitHub for more info."`

./DepotDownloader -app 218620 -depot 218621 -manifest 8140332499591716770 -username $SteamUsername -password $SteamPassword -dir $FILE/"PAYDAY 2 Project White House"

echo Depot Downloader will verify all the files are correct before proceeding!

./DepotDownloader -app 218620 -depot 218621 -manifest 8140332499591716770 -username $SteamUsername -password $SteamPassword -dir $FILE/"PAYDAY 2 Project White House"

cd $FILE/"PAYDAY 2 Project White House"

git clone https://github.com/MatthewCAbel/Project-White-House-Mods

cp -ar $FILE/"PAYDAY 2 Project White House"/Project-White-House-Mods/* $FILE/"PAYDAY 2 Project White House"

rm -rf $FILE/"PAYDAY 2 Project White House"/Project-White-House-Mods

zenity --info --text "Done! Thank you for playing Project White House! Please add the EXE file as a non steam game and select the same Proton version as your normal PAYDAY 2 install to play."



