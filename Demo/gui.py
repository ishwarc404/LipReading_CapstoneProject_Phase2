import wx
import streamer
import threading
import time
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import cv2

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Lip2Text Translator',size=(400, 300)) #width,height

        panel = wx.Panel(self)

        #start button
        start_button = wx.Button(panel, label='Start', pos=(150, 45))
        start_button.Bind(wx.EVT_BUTTON, self.on_start_press)

        #stop button
        stop_button = wx.Button(panel, label='Stop', pos=(150, 85))
        stop_button.Bind(wx.EVT_BUTTON, self.on_stop_press)

        #textlabel
        # CREATE STATICTEXT AT POINT (20, 20)
        self.outputLabel = wx.StaticText(panel, id = 1, label = "", pos =(150, 200),
                                size = wx.DefaultSize, style = 0, name ="statictext")

        self.SetMaxSize(wx.Size(400,300))
        self.SetMinSize(wx.Size(400,300))
        self.Centre() #centres it on the screen
        self.Show()
        self.stop = False

    def create_thread(self, target):
        thread = threading.Thread(target=target)
        self.started_thread = thread
        thread.daemon = True
        thread.start()

    def stop_thread(self):
        self.started_thread._stop()

    def on_start_press(self, event):
        print("Start clicked")
        self.create_thread(self.start_translating)
    
    def on_stop_press(self, event):
        print("Stop clicked")
        self.stop = True
        self.stop_translating()

    vs = WebcamVideoStream(src=0)
    fps = FPS()

    def start_translating(self):
        self.stop = False
        streamer.clean_pictures()
        print("[INFO] sampling THREADED frames from webcam...")
        self.vs.start()
        self.fps.start()
        record_index=1
        while self.fps._numFrames < 1000 and not(self.stop):
            frame = self.vs.read()
            print("frames: "+str(self.fps._numFrames)+" record_index: "+str(record_index))
            cv2.imwrite("pictures/"+str(record_index)+".jpg", frame)
            record_index=record_index+1

            key = 0xFF & cv2.waitKey(35)
            self.fps.update()
            self.fps.stop()


    def stop_translating(self):
        # do a bit of cleanup
        self.vs.stop()
        streamer.processImages()
        time.sleep(2)
        outputfile = open("result_lip/text.txt",'w')
        outputfile.write("Processing")
        outputfile.close()
        
        self.outputLabel.SetLabel("some sentence")




if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()