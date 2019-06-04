from manimlib.imports import *
import numpy as np

class checkRotation(Scene):
    def construct(self):
        line = Line(
            3*UP + 4*LEFT,
            3*UP + 4*LEFT + 4*DOWN,
            color = WHITE
        )
        line.rotate(
            np.pi/6,
            about_point = line.get_start()
        )
        self.play(ShowCreation(line))
        self.play(Rotate(line, -2*np.pi/6, about_point = 3*UP + 4*LEFT))
        self.wait(3)
