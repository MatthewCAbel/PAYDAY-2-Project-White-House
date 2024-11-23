echo Please enter your steam username. This will download it through DepotDownloader

read SteamUsername

./DepotDownloader -app 218620 -depot 218621 -manifest 8140332499591716770 -username $SteamUsername
