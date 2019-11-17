# Animation clip demonstrating change of graphs of norm in R^2
# FILEID: H7
from manimlib.imports import *
import numpy as np
from decimal import Decimal

class PlayNorm(MovingCameraScene, Axes):
    def construct(self):
        self.text = []
        text = self.text
        text.append(TexMobject(r"\text{The }", "{l_p}",
                    r"\text{ norm of a vector }",
                    r"{\vec{x}}", r"{ = }", r"{(x_1, x_2, ..., x_n)}", ",",
                    tex_to_color_map = {"l": PURPLE_C, r"\vec{x}": PURPLE_A, "_p": RED,
                                        "x_1, x_2, ..., x_n": PURPLE_A}))
        text.append(TexMobject(r"{\norm{x}_p}", "{=}",
                    r"{\biggl(\sum_{i=1}^n {|{x}_{i}|}^p\biggr)^{\frac{1}{p}}}",
                    tex_to_color_map = {r"\norm{x}": PURPLE_A, "{x}_{i}": PURPLE_A,
                    "^p":RED, "_p": RED, r"\frac{1}{p}": RED}
                    ))
        VGroup(*text).scale(0.7)
        text[0].add_background_rectangle(opacity = 0.8)
        text[1].add_background_rectangle(opacity = 0.8)
        text[0].to_edge(UP)
        text[1].next_to(text[0], DOWN, 1.2*SMALL_BUFF)
        # text[1].shift(DOWN)

        plane = NumberPlane(axis_config = {"stroke_color": LIGHT_GREY}, )
        axes = Axes()
        self.add(plane)
        self.wait(1)
        self.play(Write(text[0]))
        self.play(Write(text[1]))
        self.wait(1.5)
        
        # self.play(ApplyMethod(self.camera_frame.scale , 0.35))
        # curves = []
        # n = 11
        # colors = color_gradient([MAROON, YELLOW_C], n)
        #
        # for i in np.arange(1, 11):
        #     curves.append(self.drawcurve(i, colors[i]))
        #     self.play(ShowCreation(curves[-1]), run_time = 0.8)
        #     self.wait(0.3)
        # self.wait(3)

    def drawcurve(self, n, color):
        curve = []
        curve.append(ParametricFunction(
                    lambda t: np.array([
                    t,
                    np.power(1 - np.power(t,n),(1/n)),
                    0,
                    ]),
                    color=color,
                    stroke_width = 2,
                ))
        curve.append(ParametricFunction(
                    lambda t: np.array([
                    np.power(1 - np.power(t,n),(1/n)),
                    -t,
                    0,
                    ]),
                    color=color,
                    stroke_width = 2,
                ))
        curve.append(ParametricFunction(
                    lambda t: np.array([
                    -t,
                    -np.power(1 - np.power(t,n),(1/n)),
                    0,
                    ]),
                    color=color,
                    stroke_width = 2,
                ))
        curve.append(ParametricFunction(
                    lambda t: np.array([
                    -np.power(1 - np.power(t,n),(1/n)),
                    t,
                    0,
                    ]),
                    color=color,
                    stroke_width = 2,
                ))

        return VGroup(*curve)
