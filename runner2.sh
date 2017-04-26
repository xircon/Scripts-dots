#!/bin/bash
chce=`yad --form --field="ComboBox:CB" python\!root |cut -f1 -d\|`
case "$chce" in
    normal )
        featherpad ;;
    root )
        sudo featherpad ;;
esac

#gnome-terminal -x sh -c "medit; bash" 

