from urllib.request import urlopen
from numpy import array, uint8
from cv2 import imdecode, IMREAD_UNCHANGED , imwrite, resize, INTER_AREA
from numpy.core.fromnumeric import reshape
from pynput.keyboard import Key, Listener
from time import time
from pathlib import Path
from argparse import ArgumentParser



class Camera():
    url='http://192.168.0.100:8080/shot.jpg'
    counter = 0
    breakPlease = False

    def __init__(self, dir: str, reshape = (640, 480)):
        self.setReshape(reshape)
        self.setDir(dir)
        self.setKeyListner()

    def setKeyListner(self):
        self.keyListner = Listener(
            on_press=self.keyPressed, 
            on_release=self.keyReleased
        )

    def keyPressed(self, key):
        if key == Key.esc:
            self.breakPlease = True 

        if key == Key.space:
            image = self.image
            reshaped = resize(image, self.reshape, INTER_AREA)

            save = f"{self.dir}/{int(time())}.jpg"
            imwrite(save, reshaped)
            print(save)
            

    def keyReleased(self, key):
        pass

    def startCamera(self):
        print('''
        IP Webcam camera save !!
        esc: - Exit
        space: - Take photo   
        ''')
        
        self.keyListner.start()

        while True:
    
            if self.breakPlease:
                break

            imgResp=urlopen(self.url)
            imgNp=array(bytearray(imgResp.read()),dtype=uint8)
            self.image=imdecode(imgNp, IMREAD_UNCHANGED)

        self.keyListner.stop()
        print('''
        Exiting !!!
        ''')

    def setDir(self, dir):
        Path(dir).mkdir(exist_ok=True)
        self.dir = dir

    def setReshape(self, reshape):
        if len(reshape) != 2:
            raise AttributeError("reshape shold be of len 2")
        self.reshape = reshape

if __name__ == '__main__':
    parser = ArgumentParser("IP Webcam mobile camera capture photos")

    parser.add_argument('-d', '--savedir', type=str, required=True,
        help="specify diectory path to save")
    parser.add_argument('-r', '--reshape', type=tuple, default=(640, 480),
        help="specify size to reshape images")

    args = parser.parse_args()
    
    Camera(args.savedir, args.reshape).startCamera()