# Animation of representation of a differential equation in matrix form
# FILEID: AS2
from manimlib.imports import *

class WriteDE(Scene):
    def construct(self):
        self.show_text1()
        self.wait(2)

    def show_text1(self):
        self.text = [
        TextMobject(r"Consider a system of Linear Differential Equations",
        tex_to_color_map={"system": YELLOW_D, "Linear": GREEN_C}),
        TexMobject("{\\frac{dx}{dt}} = 5x+ 1y}"),
        TexMobject("{\\frac{dy}{dt}} = 3x+ 3y}"),
        ]
        # tex_to_color_map={"x": BLUE_C, "y": MAROON_C}),
        text = self.text
        self.text[0].shift(2*UP)
        self.text[0].scale(0.7)
        self.play(ShowCreation(self.text[0]))

        text[2].shift(1.5*DOWN)
        self.play(Write(text[1]))
        self.play(Write(text[2]))
