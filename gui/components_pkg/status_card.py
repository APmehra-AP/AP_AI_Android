# Created by : Amarchand Meghwal

from kivymd.uix.card import MDCard


class StatusCard(MDCard):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.radius = [20]
        self.padding = 20
        self.size_hint_y = None
        self.height = "160dp"
        self.elevation = 3
