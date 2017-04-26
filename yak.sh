#!/bin/sh 
# 
# yakuake_exec.sh by Barca (barca@linuxstorm.org) 
# Can be freely distributed under the GPL. Enjoy open source ;) 
# 
# Script to run command in Yakuake and set its tab's title. 

case $1 in 
    "") 
    echo -e "\n\E[34m:::\033[0m\E[31m yakuake_newtab.sh\033[0m \e[34m:::\033[0m" 
    echo "yakuake_exec.sh - script to run command in Yakuake and set its tab's title." 
    echo -e "by Barca (barca@linuxstorm.org\n" 
    echo -e "\E[31mUsage:\033[0m" 
    echo -e "$0 <tab title> <command> <options>\n" 
    echo -e "\E[31mOptions:\033[0m" 
    echo "--newtab           run command in new tab" 
    echo -e "\n\E[31mExample:\033[0m" 
    echo "$0 soundmixer alsamixer" 
    echo -e "opens new tab in Yakuake with title \"soundmixer\" and runs alsamixer binary in it\n" 
    exit 0 
    ;; 
*) 
        TAB_TITLE=$1 
        COMMAND=$2 
        OPTIONS=$3 
        if [[ "$OPTIONS" =~ "--newtab" ]]; then qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.addSession &>/dev/null; fi                                                      
        SESSION_ID=`qdbus org.kde.yakuake /yakuake/sessions org.kde.yakuake.activeSessionId`                                                                                            
        qdbus org.kde.yakuake /yakuake/tabs setTabTitle $SESSION_ID $TAB_TITLE &>/dev/null                                                                                              
        qdbus org.kde.yakuake /yakuake/sessions runCommandInTerminal $SESSION_ID "$COMMAND" &>/dev/null                                                                                  
        exit                                                                                                                                                                            
esac