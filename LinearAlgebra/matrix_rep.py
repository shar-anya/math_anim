# Animation of representation of a differential equation in matrix form
# FILEID: AS2
from manimlib.imports import *

class WriteDE(Scene):
    def construct(self):
        self.show_text1()
        self.wait(2)

    def show_text1(self):
        self.text = [
        TextMobject(r"System of Linear Differential Equations", #0
        tex_to_color_map={"System": MAROON_C, "Linear": GREEN_C}),
        TexMobject("{\\frac{dx}{dt}}" , "{=}" , "{5}" , "{x}" , "{+}" , "{1}" , "{y}"),
        TexMobject("{\\frac{dy}{dt}}" , "{=}" , "{3}" , "{x}" , "{+}" , "{3}" , "{y}"),
        ]
        text = self.text
        self.text[0].shift(0.2*UP)
        self.text[0].scale(0.7)

        text[1].shift(0.6*DOWN)
        text[2].shift(2*DOWN)
        VGroup(*text[1:3]).scale(0.8)
        text[1].set_color_by_tex_to_color_map({"{x}": BLUE_C, "{y}": BLUE_C, "{5}":YELLOW_D , "{1}": YELLOW_D})
        text[2].set_color_by_tex_to_color_map({"{x}": BLUE_C, "{y}": BLUE_C, "{3}":YELLOW_D , "{3}": YELLOW_D})
        self.play(Write(text[1]))
        self.play(Write(text[2]))
        self.play(ShowCreation(self.text[0]))
        self.wait(1)
        text[0].set_color_by_tex_to_color_map({"System": WHITE, "Linear": WHITE})

        text.append(TextMobject("Two equations in two variables")) #3
        text[-1].scale(0.7)
        text[-1].shift(text[0].get_center())

        # self.wait(2)
        # self.play(Transform(text[0], text[-1]))
        # self.wait(2)

        text.append(TextMobject("Matrix form")) #4
        text[-1].scale(0.7)
        text[-1].to_edge(UP)

        self.wait(1)
        self.play(ShowCreation(text[-1]))
        self.wait(1)

        text.append(self.text[1][3].copy()) # x , 5
        text.append(self.text[1][6].copy()) # y
        text.append(self.text[2][3].copy()) # x
        text.append(self.text[2][6].copy()) # y

        text.append(self.text[1][2].copy()) # 5
        text.append(self.text[1][5].copy()) # 1
        text.append(self.text[2][2].copy()) # 3
        text.append(self.text[2][5].copy()) # 3 ,12

        self.add(*text[-8:])

        text.append(TexMobject(r"{\begin{bmatrix} 5 & 1 \\ 3 & 3 \end{bmatrix}}")) # Matrix A , 13
        text[-1].to_edge(UP)
        text[-1].shift(0.5*RIGHT+0.9*DOWN)
        text[-1].set_color_by_tex_to_color_map({"x": YELLOW_D})

        text.append(TexMobject(r"{\begin{bmatrix} x \\ y \end{bmatrix}}")) # Matrix [x \\ y] , 14
        text[-1].to_edge(UP)
        text[-1].shift(1.6*RIGHT+0.9*DOWN)
        text[-1].set_color_by_tex_to_color_map({"x": BLUE_C})

        matrixnumbers = VGroup(*text[9:13])
        vectorvars = VGroup(*text[5:9])

        self.play(Transform(matrixnumbers , text[13], run_time = 2))
        self.play(Transform(vectorvars, text[14], run_time = 2))

        text.append(TextMobject("$=$")) #15
        text[-1].shift(text[13].get_center()+ 1*LEFT)
        self.play(ShowCreation(text[-1]))

        text.append(text[1][0].copy())
        text.append(text[2][0].copy()) #17
        self.add(*text[-2:])
        diffvec = VGroup(*text[-2:])

        text.append(TexMobject(r"{\frac{d}{dt}}", r"{\begin{bmatrix} x \\ y \end{bmatrix}}")) # Matrix [x \\ y] , 18
        text[-1].to_edge(UP)
        text[-1].shift(1.5*LEFT+0.9*DOWN)
        text[-1].set_color_by_tex_to_color_map({"x": BLUE_C})

        self.play(Transform(diffvec, text[-1]))
        self.wait(1)
        self.play(FadeOut(VGroup(*text[:3])))

        text.append(VGroup(*text[13:16], text[18]).copy())

        text.append(TexMobject(r"{\frac{d}{dt}}", r"{\vec{u}}",
         r"{\hspace{2pt}=\hspace{2pt}}", "{A}", r"{\vec{u}}",
         tex_to_color_map={r"{\vec{u}}": BLUE_C, "{A}": YELLOW_D})) #20
        text
        self.play(Transform(text[-2], text[-1]))
        self.wait(2)
