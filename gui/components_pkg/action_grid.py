# Created by : Amarchand Meghwal

from kivymd.uix.gridlayout import MDGridLayout


class ActionGrid(MDGridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2
        self.spacing = "12dp"
        self.adaptive_height = True
