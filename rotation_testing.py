from manimlib.imports import *
import numpy as np

class checkRotation(Scene):
    def construct(self):
        # line1 = Line(color= BLUE_A)
        # line2 = Line(color= GOLD_D)
        # line2.scale(2)
        # line2.shift(1*DOWN)
        # line2.set_angle(45*DEGREES)
        # self.play(ShowCreation(line1), ShowCreation(line2))
        # self.wait(1)
        # self.play(ApplyMethod(triangle1.rotate,3))
        # self.play(ApplyMethod(
        # line1.rotate(45*DEGREES, about_point = ORIGIN)
        # self.play(ApplyMethod(line2.rotate, about_point = 2*RIGHT+DOWN))
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
