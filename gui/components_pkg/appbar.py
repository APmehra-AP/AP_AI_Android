# Created by : Amarchand Meghwal

from kivymd.uix.toolbar import MDTopAppBar


class APAppBar(MDTopAppBar):

    def __init__(self, title="AP AI", **kwargs):
        super().__init__(**kwargs)

        self.title = title
        self.elevation = 0

        self.left_action_items = [
            ["robot-outline", lambda x: None]
        ]

        self.right_action_items = [
            ["cog", lambda x: None]
        ]
