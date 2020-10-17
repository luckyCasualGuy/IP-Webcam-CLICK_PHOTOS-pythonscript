# IP-Webcam-CLICK_PHOTOS-script
To store photos from your IP Webcam mobile feed on your PC: Used for collecting datasets good quality image datasets from your phone camera

# Make sure your mobile is connected to same router as your PC

### Install requirements.txt:  
`pip install -r requirement.txt`  

### Download IP Webcam app on your mobile phone:
Set the app settings and start the server from mobile app
![MOBILE HOME PAGE](https://raw.githubusercontent.com/luckyCasualGuy/IP-Webcam-CLICK_PHOTOS-pythonscript/main/imgs/startserver.jpg)

### Start the python script:  
`python camera.py -d Save`
Keep this script running in background

### Go to the link specified in your IP Webcam mobile app after starting the server there: 
#### This is where you will find link:
![Where](https://raw.githubusercontent.com/luckyCasualGuy/IP-Webcam-CLICK_PHOTOS-pythonscript/main/imgs/IPWhere.jpg)

#### Open it in your browser.
![HOME PAGE](https://raw.githubusercontent.com/luckyCasualGuy/IP-Webcam-CLICK_PHOTOS-pythonscript/main/imgs/IPWebcamHome.jpg)

select any of the video modes and then fullscreen to view the camera feed.

### Press SPACE to take photos:
Photos will be saved in the foler specified after `-d`

### Press EXC to quite the script:
