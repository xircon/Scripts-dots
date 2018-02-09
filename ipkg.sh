#!/bin/bash

head1="TAB key to (un)select. ENTER key to remove. ESC to quit."
prompt1="Enter string to filter list > "

outfile="/tmp/pacui-packages-group"

expac -Q "%-33n\t%d" > $outfile 

pkg=$( sort -k1,1 -u $outfile | fzf-tmux -m +x -e +s -i -1 --query="$1" --cycle --reverse \
	--margin=4%,1%,1%,2% --inline-info --preview '
            if ( pacman -Qq {1} &>/dev/null )         # check, if selected line is a locally installed package
            then
                pacman -Qi {1} --color always
            else
                echo -e "\e[1m{1} group has the following members: \e[0m"
                pacman -Sgq {1}
            fi
            ' --preview-window=right:50%:wrap --header="$head1" --prompt='Enter string to filter list > ' | awk '{print $1}' )

echo "Input2= "$input2
yaourt -Rsn $pkg
echo $pkg