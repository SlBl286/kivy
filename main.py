from kivy.app import App
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.widget import Widget;
from kivy.uix.button import Button;
from kivy.uix.boxlayout import BoxLayout;
from kivy.uix.gridlayout import GridLayout;

class LayoutExample(GridLayout):
    # pass;
    isEnable = BooleanProperty(False);
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

class MainWidget(Widget):
    pass;

class TheLabApp(App):
    pass;


TheLabApp().run();