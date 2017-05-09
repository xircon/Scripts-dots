import QtQuick 2.5
import QtQuick.Controls 1.4

ApplicationWindow {

    width: 300
    height: 500
    title: "Shortcut Keys"

    Text {
    
        text: "Left Shift  - Escape\n Right Shift - Mute"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        font.pointSize: 24; font.bold: true
        color: "white"
    }
}