# kivy
learn kivy python
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: "Layout"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'LayoutScreen'
        Button:
            text: "Widget"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'WidgetScreen'
<LayoutScreen>:
    BoxLayout:
        orientation: 'vertical'
        rows:3
        BoxLayout:
            Button:
                text: "Back"
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'MenuScreen'
            Label:
                text: "Menu"
                font_size: "20dp"
                color: 1,0,0,1
                font_name: "Font/ds_digital/DS-DIGII.TTF"
        BoxLayout:
            Button:
                    text: "BoxLayout"
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'MenuScreen'
            Button:
                    text: "AnchorLayout"
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'MenuScreen'
            Button:
                    text: "GridLayout"
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'MenuScreen'
        BoxLayout:
<WidgetScreen>:
    BoxLayout:
        orientation: 'vertical'
        GridLayout:
            cols: 2
            Button:
                text: "Back"
                size_hint: 0.1,0.1
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'MenuScreen'
            Label:
                text: "Menu"
                font_size: "20dp"
                color: 1,0,0,1
                font_name: "Font/ds_digital/DS-DIGII.TTF"
        GridLayout:
            cols: 3
            ToggleButton:
                text: "OFF"
                on_state: root.on_toggle_button_click(self)
                size_hint: None,1
                width: "100dp"
            Button:
                text: "Count"
                on_press: root.on_button_click()
                disabled: not root.isEnable
            Label:
                text: root.text
                font_size: "70dp"
                color: 1,0,0,1
                font_name: "Font/ds_digital/DS-DIGII.TTF"
            Switch:
                id: isSliderDisable
                on_active: root.on_switch_active(self)
                size_hint: None,1
                width: "100dp"
            Slider:
                id: sliderValue
                min: 0
                max: 100
                value: 50
                disabled: not isSliderDisable.active
            Label:
                text: str(int(sliderValue.value))
                font_size: "70dp"
                color: 1,0,0,1
                font_name: "Font/ds_digital/DS-DIGII.TTF"
            TextInput:
                size_hint: None,1
                width: "100dp"


