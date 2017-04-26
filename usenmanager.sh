#!/bin/bash
sudo systemctl stop connman.service
sudo systemctl disable connman.service
sudo systemctl enable NetworkManager.service
sudo systemctl start NetworkManager.service