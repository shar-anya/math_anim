# Animation of representation of a differential equation in matrix form
# FILEID: AS2
from manimlib.imports import *

class WriteDE(Scene):
    def construct(self):
        FirstText = TextMobject("Consider a system of Linear Differential Equations")
        FirstText.set_color_by_tex_to_color_map({"system": YELLOW_D, "Linear":GREEN,})
        FirstText.scale(0.8)
        FirstText.to_edge(TOP)

        self.play(ShowCreation(FirstText))
        self.wait(2)
