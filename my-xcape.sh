#!/bin/bash
xcape -e 'Super_L=Alt_L|Tab'
xcape -e 'Super_R=Control_L|Alt_L|m'
xcape -e 'Control_L=Super_L|1'
xcape -e 'Alt_L=Super_L|2'
xcape -e 'Shift_L=x'
xcape -e 'Shift_R=Super_L|F2'
xcape -e 'Control_R=Control_R|Return' 