# Animation clip showing (text) how linear transformations are just combinations
# FILEID: H3
from manimlib.imports import *

class WrittenScene(Scene):
    def construct(self):
        self.text = []
        text = self.text

        text.append(TexMobject(r"\text{Let }" , "{A}" ,
                               r"\text{ be a linear transformation}",
                               tex_to_color_map = {"{A}": BLUE_C}))
        text.append(TexMobject(r"\text{And }", r"{\vec{v}}",
                               r"\text{ be a vector in the column-space of }",
                               "{A}", tex_to_color_map = {"{A}": BLUE_C, r"{\vec{v}}": MAROON_C}))
        text.append(TexMobject(r"{A}" , "{=}", tex_to_color_map = {"{A}": BLUE_C}))
        text.append(TexMobject(r"{\vec{v}}" , "{=}", tex_to_color_map = {r"{\vec{v}}": MAROON_C}))
        text.append(TexMobject("{=}"))
        text.append(TexMobject("{+}"))
        text[1].scale(0.8)
        text[0].scale(0.8)
        text[0].to_edge(UP)
        text[1].next_to(text[0], DOWN, MED_LARGE_BUFF)

        rows = [["a_1", "b_1", "c_1"],
                ["a_2", "b_2", "c_2"],
                ["a_3", "b_3", "c_3"]]

        col = ["v_1", "v_2", "v_3"]
        colcolors = (BLUE_B, BLUE_C, BLUE_D)
        linear_transform = Matrix([rows[0], rows[1], rows[2]])
        linear_transform.set_column_colors(colcolors[0], colcolors[1], colcolors[2])
        linear_transform.shift(LEFT)

        vector = Matrix(col)
        # column = VGroup(*vector.mob_matrix[:])
        vector.set_color(MAROON_C)
        text[2].next_to(linear_transform, LEFT, SMALL_BUFF)
        text[3].next_to(linear_transform, RIGHT, MED_LARGE_BUFF)
        vector.next_to(text[3], RIGHT, SMALL_BUFF)
        multiplication = VGroup(linear_transform, vector)

        self.play(Write(text[0]))
        self.play(Write(text[2]), Write(linear_transform))
        self.play(Write(text[1]))
        self.play(Write(text[3]), Write(vector))
        self.wait(1)
        self.play(FadeOut(VGroup(*text[:4])))
        self.play(ApplyMethod(vector.next_to, linear_transform, RIGHT, MED_SMALL_BUFF))
        self.wait(0.5)
        self.play(ApplyMethod(multiplication.scale, 0.8, run_time = 0.6))
        self.play(ApplyMethod(multiplication.to_edge, UP, run_time = 1))
        self.wait(1)

        text[4].shift(3.5*LEFT + 0.3*DOWN)
        text[4].scale(0.8)
        text[5].scale(0.8)

        colmatrices = []
        for i in range(3):
            colmatrices.append(Matrix([rows[0][i], rows[1][i], rows[2][i]]))
            colmatrices[i].set_color(colcolors[i])
            colmatrices[i].scale(0.8)

        vectorcopy = [vector.copy() for i in range(3)]
        vecelement = [TexMobject(col[i]).set_color(MAROON_C) for i in range(3)]
        pluscopy = [text[5].copy() for i in range(3)]
        self.add(*vectorcopy)

        frameBox = [
                    SurroundingRectangle(VGroup(linear_transform[0][i],
                                        linear_transform[0][i+6]),
                                        buff = 0.7*MED_SMALL_BUFF, color = colcolors[i],
                                        stroke_width = 2)
                                        for i in range(3)
                    ]

        colmatrices[0].next_to(text[4], RIGHT, MED_SMALL_BUFF)
        vecelement[0].next_to(colmatrices[0], RIGHT, SMALL_BUFF)
        self.play(ShowCreation(text[4]))
        self.play(ShowCreation(frameBox[0]))
        self.play(Transform(frameBox[0],colmatrices[0]),
                  Transform(vectorcopy[0], vecelement[0]),
                  run_time = 1.3)
        # self.play()

        for i in range(1,3):
            pluscopy[i].next_to(vectorcopy[i-1], RIGHT, MED_SMALL_BUFF)
            colmatrices[i].next_to(pluscopy[i], RIGHT, MED_SMALL_BUFF)
            vecelement[i].next_to(colmatrices[i], RIGHT, SMALL_BUFF)
            self.play(ShowCreation(pluscopy[i]))
            self.play(ShowCreation(frameBox[i]))
            self.play(Transform(frameBox[i],colmatrices[i]),
                      Transform(vectorcopy[i], vecelement[i]),
                      run_time = 1.3)
            # self.play()
            self.wait(0.5)

        self.wait(1)

        # self.play(ShowCreation(VGroup(*frameBox)))
        self.wait(3)
