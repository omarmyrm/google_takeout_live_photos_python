# google_takeout_live_photos_python
Many of us come to a problem when doing a 'takeout' from our Google Photos account if we have taken 'live photos' with our Apple devices.
By default, Google exports our live photos as a photo and a short (3 seconds) .MP4 file. As this may be annoying and takes extra space, this program fixes it by deleting those videos.
The way this program works is by deleting any .MP4 video that is shorter than 4 seconds (live photos clip is 3 seconds). Therefore, please, make sure to back up in another directory any .MP4 video that is shorter than 4 seconds and you want to keep.

#Operation:
1) Download the script
2) Place the script in the directory in which you want to delete all the live photos additional clips.
3) Run the script from the command line [cd to the chosen directory] and then [python borrar_mp4.py].
4) Wait for the process to end without interacting with the chosen directory,

#Disclaimer:
The modification or wrong operation of this program could lead to permanent loss of data. You take it to your own risk.
