# BASH COLORS
RED='\033[1;31m'
CYAN='\033[0;36m'
NC='\033[0m'
#

isupdate=`pacman -Qu | grep -v 'ignored' | wc -l`
 
if [ $isupdate -ne 0 ]; then
    echo  -e " ${CYAN} ** Update is avavible. ** "
else
   echo -e "${RED} ** No update avavible. ** "
   exit -1
fi  
 
#PACMAN MIRRORS.
if [ -d /etc/pacman.d ]; then
    echo -e "${CYAN} ** Do you want to check pacman-mirrors? Y/n ** "
    read MIRRORS_CHECK
fi 
 
if [ $MIRRORS_CHECK  == "Y" ] || [ $MIRRORS_CHECK  == "y" ]; then          
    sudo pacman-mirrors -g  
else
:
 
fi
   
sudo pacman -Syuw
 
if [ $? -eq 0 ]; then
    sudo pacman -Su  
else
    echo -e "${RED} ** Installation failed. ** "
fi
 
echo -e "${CYAN} ** Optimize pacman? **  (DO NOT USE OND SSD DISK) Y/n"
read PACMAN_OPTIMIZE
 
if [ $PACMAN_OPTIMIZE == "Y" ] || [ $PACMAN_OPTIMIZE == "y" ]; then
    echo -e "${CYAN}  ** Optimizing ... **"
    sudo pacman-optimize && sync
    echo -e "${CYAN}  **Everything is done. **"
else
    echo -e "${CYAN}  **Everything is done **" 
fi