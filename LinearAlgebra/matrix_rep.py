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
        TexMobject("{\\frac{dx}{dt}}" , "{=}" , "{5}" , "{x}" , "{+}" , "{1}" , "{y}"),
        TexMobject("{\\frac{dy}{dt}}" , "{=}" , "{3}" , "{x}" , "{+}" , "{3}" , "{y}"),
        ]
        text = self.text
        self.text[0].shift(1.3*UP)
        self.text[0].scale(0.7)
        self.play(ShowCreation(self.text[0]))

        text[2].shift(1.5*DOWN)
        text[1].set_color_by_tex_to_color_map({"{x}": BLUE_C, "{y}": MAROON_C, "{5}":YELLOW_C , "{1}": YELLOW_C})
        text[2].set_color_by_tex_to_color_map({"{x}": BLUE_C, "{y}": MAROON_C, "{3}":YELLOW_C , "{3}": YELLOW_C})
        self.play(Write(text[1]))
        self.play(Write(text[2]))

        text.append(TextMobject("Two equations in two variables"))
        text[-1].scale(0.7)
        text[-1].shift(text[0].get_center())

        self.wait(2)
        self.play(Transform(text[0], text[-1]))
        self.wait(2)

        text.append(TextMobject("Matrix form"))
        text[-1].scale(0.7)
        text[-1].shift(text[0].get_center())

        self.wait(1)
        self.play(Transform(text[0], text[-1]))
        self.wait(1)

        text.append(self.text[1][3].copy()) # x
        text.append(self.text[1][6].copy()) # y
        text.append(self.text[2][3].copy()) # x
        text.append(self.text[2][6].copy()) # y

        text.append(self.text[1][2].copy()) # 5
        text.append(self.text[1][5].copy()) # 1
        text.append(self.text[2][2].copy()) # 3
        text.append(self.text[2][5].copy()) # 3

        self.add(*text[-8:])

        text.append(TextMobject(r"$\begin{bmatrix} 5 & 1 \\ 3 & 3 \end{bmatrix}$")) # Matrix A
        text[-1].to_edge(UP)
        text[-1].shift(0.5*RIGHT)
        text.append(TextMobject(r"$\begin{bmatrix} x \\ y \end{bmatrix}$")) # Matrix [x \\ y]
        text[-1].to_edge(UP)
        text[-1].shift(1.6*RIGHT)

        matrixnumbers = VGroup(*text[9:13])
        vectorvars = VGroup(*text[5:9])

        self.play(Transform(matrixnumbers , text[13], run_time = 2))
        self.play(Transform(vectorvars, text[14], run_time = 2))

        text.append(TextMobject("$=$"))
        text[-1].shift(text[13].get_center()+ 1*LEFT)
        self.play(ShowCreation(text[-1]))

        text.append(text[1][0].copy())
        text.append(text[2][0].copy())
        self.add(*text[-2:])
        diffvec = VGroup(*text[-2:])

        text.append(TexMobject(r"{\frac{d}{dt}}", r"{\begin{bmatrix} x \\ y \end{bmatrix}}")) # Matrix [x \\ y]
        text[-1].to_edge(UP)
        text[-1].shift(1.5*LEFT)
        self.play(Transform(diffvec, text[-1]))
