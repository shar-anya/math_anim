# Writing of eigenvalues
# FILEID: 2CS
from manimlib.imports import *
class WriteEigenvalues(Scene):
    def construct(self):
        self.write_eig()
        self.wait(2)

    def write_eig(self):
        self.text = []
        text = self.text

        text.append(TexMobject(r"\text{The eigenvalues are }" , "{2}" ,
        r"\text{ , }", "{6}", tex_to_color_map = {"{2}" : GREEN_B , "{6}": GREEN_D }))
        text[0].shift(0.8*UP)

        text.append(text[0][1].copy())
        text.append(text[0][3].copy())
        text.append(TexMobject(r"\text{The eigenvectors are}"))
        text.append(TexMobject(r"{\begin{bmatrix}1 \\ 1 \end{bmatrix}}",
        r"\text{and}" , r"{\begin{bmatrix}-1 \\ 3 \end{bmatrix}}"))

        VGroup(*text).scale(0.8)

        self.play(Write(text[0]))
        self.play(Write(text[3]))
        text[4].shift(DOWN)
        text[-1].set_color_by_tex_to_color_map({"1": GREEN_B})
        text[-1].set_color_by_tex_to_color_map({"3": GREEN_D})
        self.play(Transform(text[1], text[4][0]))
        self.play(Write(text[4][1]))
        self.play(Transform(text[2], text[4][2]))
