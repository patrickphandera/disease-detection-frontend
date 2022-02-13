from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
import time
class CameraClick(BoxLayout):
    def __init__(self):
        super(CameraClick,self).__init__()
        camera= Camera(id= 'camera', play= False, resolution= (100,100))
    
        self.add_widget(Button(text= 'Play', on_press= (camera.play = not camera.play),size_hint_y= None,height= 48dp))
        self.add_widget(Button(text= 'Capture',size_hint_y= None,height= 48dp,on_press= root.capture()))
class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()
