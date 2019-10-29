# Writing of eigenvalues
# FILEID: 2CS
from manimlib.imports import *
class WriteEigenvalues(Scene):
    def construct(self):
        self.write_eig()
        self.wait(3)

    def write_eig(self):
        self.text = []
        text = self.text

        ORIGIN = 1.5*UP + 3.5*LEFT
        text.append(TexMobject(r"\text{For the matrix}" , r"{\begin{bmatrix} 5 & 1 \\ 3 & 3 \end{bmatrix}}"))
        text[0].set_color_by_tex_to_color_map({"5": BLUE_C})
        text[0].shift(3.5*UP+3.5*LEFT)
        text.append(TexMobject(r"\text{The eigenvalues are }" , "{2}" ,
        r"\text{ , }", "{6}", tex_to_color_map = {"{2}" : YELLOW_B , "{6}": YELLOW_D }))
        text[1].shift(ORIGIN + 0.8*UP)

        text.append(text[1][1].copy()) #1
        text.append(text[1][3].copy()) #2
        text.append(TexMobject(r"\text{The eigenvectors are}")) #3
        text[-1].shift(ORIGIN)
        text.append(TexMobject(r"{\begin{bmatrix}1 \\ 1 \end{bmatrix}}",
        r"\text{and}" , r"{\begin{bmatrix}-1 \\ 3 \end{bmatrix}}")) #4

        VGroup(*text).scale(0.8)
        self.play(Write(text[0]))
        self.play(Write(text[1]))
        self.play(Write(text[4]))
        text[5].shift(ORIGIN + 1.2*DOWN+ 0.7*RIGHT)
        text[-1].set_color_by_tex_to_color_map({"1": YELLOW_B})
        text[-1].set_color_by_tex_to_color_map({"3": YELLOW_D})
        self.play(Transform(text[2], text[5][0]))
        self.play(Write(text[5][1]))
        self.play(Transform(text[3], text[5][2]))

        text.append(TextMobject("Consequently, the solution will be:"))
        text[-1].scale(0.8)
        text[-1].shift(ORIGIN+ 2*DOWN)
        equation =  TextMobject(r"$y(t)$", "=" , r"$c_1$",r"$e^{6t}$", r"$\begin{bmatrix} 1 \\ 1 \end{bmatrix}$", "+", r"$c_2$",r"$e^{2t}$", r"$\begin{bmatrix} -1 \\ 3 \end{bmatrix}$")
        equation.set_color_by_tex(r"1",YELLOW_B)
        equation.set_color_by_tex(r"3",YELLOW_D)
        equation.set_color_by_tex("c_",BLUE)
        equation.set_color_by_tex("e^",GREEN_C)
        equation.scale(0.9)
        equation.shift(ORIGIN + 3.2*DOWN)
        text.append(equation)
        self.wait(1)
        self.play(Write(text[-2]))
        self.play(Write(text[-1]))
    
        # self.play(ApplyMethod(VGroup(*text).shift,ORIGIN + 3*UP+3*LEFT))
