#!/bin/bash
chce=`yad --form --field="ComboBox:CB" normal\!root |cut -f1 -d\|`
case "$chce" in
    normal )
        featherpad ;;
    root )
        sudo featherpad ;;
esac