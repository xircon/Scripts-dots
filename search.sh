#!/bin/dash
# A fuzzy file-finder and opener based on dmenu 
# Requires: dmenu, xdg-utils 
if [ -z "$@" ]; then
	find ~/ -not -path '*/\.*' 2> /dev/null | sed "s+$HOME+~+g" | sort -f
else
	case "$(echo $@ | cut -d " " -f 1)" in
		a)
			exec $BROWSER https://wiki.archlinux.org/index.php/"$(echo $@ | cut -d " " -f2-)" &> /dev/null &
			;;
		w)
			exec $BROWSER https://en.wikipedia.org/wiki/"$(echo $@ | cut -d " " -f2-)" &> /dev/null &
			;;
		s)
			exec $BROWSER https://startpage.com/do/search?query="$(echo $@ | cut -d " " -f2-)"&cat=web&pl=chrome&language=english &> /dev/null &
			;;
		*)
			exec xdg-open "$(echo $@ | sed 's/^...//')" &> /dev/null &
			;;
	esac
fi
