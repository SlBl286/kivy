from kivy.app import App
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.widget import Widget;
from kivy.uix.button import Button;
from kivy.uix.boxlayout import BoxLayout;
from kivy.uix.gridlayout import GridLayout;
from kivy.uix.screenmanager import ScreenManager,Screen

class LayoutScreen(Screen):
    isEnable = BooleanProperty(False);
    isSliderDisable = BooleanProperty(True);
    text = StringProperty("0");
    def on_button_click(self):
        if(self.isEnable):
            self.text = str(int(self.text)+1);
    def on_toggle_button_click(self,widget):
        if(widget.state == "normal"):
            widget.text = "OFF";
            self.isEnable = False;
        else:
            widget.text = "ON"
            self.isEnable = True;
    def on_switch_active(self,widget):
        if(widget.active == "OFF"):
            self.isSliderDisable = True
        else:
            self.isSliderDisable = False

class MenuScreen(Screen):
    pass;

class TheLabApp(App):
    def build(self):
        screenManager = ScreenManager();
        screenManager.add_widget(MenuScreen(name='menu'));
        screenManager.add_widget(LayoutScreen(name='LayoutScreen'));
        return screenManager;

if __name__ == '__main__':
    TheLabApp().run();