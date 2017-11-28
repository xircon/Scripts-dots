#!/bin/bash

head1="TAB key to (un)select. ENTER key to remove. ESC to quit."
prompt1="Enter string to filter list > "

outfile="/tmp/pacui-packages-group"

find /usr/share/icons -iname "*" -type f > $outfile 

pkg=$( sort -k1,1 -u $outfile | fzf -m -e +s -i -1 --query="$1" --cycle --reverse \
	--margin=4%,1%,1%,2% --inline-info --preview '
	Curr={} 
    if [ ! -f {} ]; then
        echo "File not found!"
    else
        echo $Curr
    fi

	' \
	--preview-window=right:50%:wrap --header="$head1" --prompt='Enter string to filter list > ' | awk '{print $1}' )

echo {1}
echo "Input2= "$input2
echo $pkg
feh $pkg