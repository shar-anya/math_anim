# Animation clip demonstrating change of graphs of norm in R^2
# FILEID: H7
from manimlib.imports import *
import numpy as np
from decimal import Decimal

class PlayNorm(MovingCameraScene, Axes):
    def construct(self):
        self.text = []
        text = self.text
        plane = NumberPlane(axis_config = {"stroke_color": LIGHT_GREY}, )
        axes = Axes()
        self.add(plane)
        self.write_stuff()
        self.wait(1)

        self.play(ApplyMethod(self.camera_frame.scale , 0.4))
        curves = []
        n = 11
        colors = color_gradient([MAROON, YELLOW_C], n+1) #12 values
        zoomtext = []
        runtimes = np.linspace(1.4, 0.2, n)
        extravar = None
        for i in np.arange(0, 10):
            weird = r"{\norm{x}_{"+str(i+1)+"}}"
            zoomtext.append(TexMobject(weird, "{=}", "{1}"))
            zoomtext[i].set_color(colors[i])
            zoomtext[i].scale(0.5)
            zoomtext[i].shift(UP+2*LEFT)
            zoomtext[i].add_background_rectangle()
            curves.append(self.drawcurve(i+1, colors[i]))
            if (i):
                self.play(Transform(curves[-2],curves[-1]), ReplacementTransform(zoomtext[i-1], zoomtext[i]), run_time = runtimes[i])
            else:
                self.play(ShowCreation(curves[0]), FadeIn(zoomtext[i]), run_time = runtimes[i])
                extravar = curves[0].copy()
                self.add(extravar)
            self.wait(0.1)

        weird = r"{\norm{x}_{"+str(50)+"}}"
        zoomtext.append(TexMobject(weird, "{=}", "{1}"))
        zoomtext[10].set_color(colors[10])
        zoomtext[10].scale(0.5)
        zoomtext[10].shift(UP+2*LEFT)
        zoomtext[10].add_background_rectangle()
        curves.append(self.drawcurve(11, colors[10]))
        self.play(ShowCreation(curves[-1]), ReplacementTransform(zoomtext[9], zoomtext[10]), run_time = runtimes[-1])
        self.wait(0.1)

        weird = r"{\norm{x}_{\infty}}"
        zoomtext.append(TexMobject(weird, "{=}", "{1}"))
        zoomtext[11].set_color(YELLOW_C)
        zoomtext[11].scale(0.5)
        zoomtext[11].shift(UP+2*LEFT)
        zoomtext[11].add_background_rectangle()
        norm_infty = Square(color = YELLOW_C, stroke_width = 3.5)
        self.play(ShowCreation(norm_infty), ReplacementTransform(zoomtext[10], zoomtext[11]), run_time = 1)
        self.wait(2)

        self.play(FadeOut(VGroup(*curves[1:], extravar, norm_infty)), ReplacementTransform(zoomtext[-1], zoomtext[0]), run_time = 1.5)
        self.wait(1.5)

        fraction_p_values =  np.arange(1.75, 0.25, -0.25)
        newcolors = color_gradient([MAROON, GREEN_C], len(fraction_p_values))
        newcurves = []
        newzoomtext = []
        for i in range(len(fraction_p_values)):
            weird = r"{\norm{x}_{"+str(fraction_p_values[i])+"}}"
            newzoomtext.append(TexMobject(weird, "{=}", "{1}"))
            newzoomtext[i].set_color(newcolors[i])
            newzoomtext[i].scale(0.5)
            newzoomtext[i].shift(UP+2*LEFT)
            newzoomtext[i].add_background_rectangle()
            newcurves.append(self.drawcurve(fraction_p_values[i], newcolors[i]))
            if (i):
                self.play(Transform(newcurves[-2], newcurves[-1]), ReplacementTransform(newzoomtext[i-1], newzoomtext[i]), run_time = runtimes[i])
            else:
                self.play(ShowCreation(newcurves[0]), FadeIn(newzoomtext[i]), run_time = runtimes[i])
                extravar = newcurves[0].copy()
                self.add(extravar)
                self.play(FadeOut(zoomtext[0]))
            self.wait(0.1)

        self.wait(2)

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

    def write_stuff(self):
        text = self.text
        text.append(TexMobject(r"\text{The }", "{l_p}",
                    r"\text{ norm of a vector }",
                    r"{\vec{x}}", r"{ = }", r"{(x_1, x_2, ..., x_n)}", ",",
                    tex_to_color_map = {"l": PURPLE_C, r"\vec{x}": PURPLE_A, "_p": RED,
                                        "(x_1, x_2, ..., x_n)": PURPLE_A}))
        text.append(TexMobject(r"{\norm{x}_p}", "{=}",
                    r"{\biggl(\sum_{i=1}^n {|{x}_{i}|}^p\biggr)^{\frac{1}{p}}}",
                    tex_to_color_map = {r"\norm{x}": PURPLE_A, "{x}_{i}": PURPLE_A,
                    "^p":RED, "_p": RED, r"\frac{1}{p}": RED}
                    ))

        text.append(TexMobject(r"\text{Take all points that satisfy }",
                    r"{\norm{x}_p = 1}", r"\text{ for a certain }", "{p}",
                    tex_to_color_map = {r"\norm{x}": PURPLE_A, "_p": RED,
                                        "{p}": RED, "1": YELLOW_E}))
        VGroup(*text).scale(0.8)

        [text[i].add_background_rectangle(opacity = 0.8) for i in range(3)]
        text[0].to_edge(UP)
        text[1].next_to(text[0], DOWN, 1.2*SMALL_BUFF)

        self.play(FadeIn(text[0]), run_time = 1.5)
        self.play(FadeIn(text[1]), run_time = 1.5)
        self.wait(1.5)
        self.play(FadeIn(text[2]))
        self.wait(1.5)
        self.play(FadeOut(VGroup(*text[:3])))
