# Animation clip demonstrating solution of points when they're near parallel and orthogonal
# FILEID: H4
from manimlib.imports import *
import numpy as np
from decimal import Decimal

class Scene1(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": False,
        "show_coordinates": False,
        "show_basis_vectors": False,
        }
    def construct(self):
        self.setup()
        self.text = []
        text = self.text
        slopeval = [1, 1.1, 11]
        constantval = str(0.5)
        eqcolors = [
                    [MAROON_E, YELLOW_E],
                    [MAROON_C, YELLOW_C],
                    [MAROON_B, YELLOW_B],
                    ]
        for i in range(3): #0 - 5
            slope = "{m_" + str(i+1) + "}"
            constant = "{c_" + str(i+1) + "}"
            text.append(TexMobject("{y}", "{ = }", slope, "{x}", "{ + }", constant,
                        tex_to_color_map = {slope: eqcolors[i][0], constant: eqcolors[i][1]}))
            text.append(TexMobject("{y}", "{ = }", str(slopeval[i]), "{x}", "{ + }", constantval,
                        tex_to_color_map = {str(slopeval[i]): eqcolors[i][0], constantval: eqcolors[i][1]}))
            text[2*i].add_background_rectangle()
            text[2*i+1].add_background_rectangle()
            text[2*i].to_edge(UP)
            text[2*i+1].to_edge(UP)
        [text.append([TexMobject("{m_" + str(i+1)+ "}", "{=}", tex_to_color_map = {"{m_" + str(i+1)+ "}": eqcolors[i][0]}),
                      TexMobject("{c_" + str(i+1)+ "}", "{=}", tex_to_color_map = {"{c_" + str(i+1)+ "}": eqcolors[i][1]})])
                                            for i in range(3)] #6[], 7[], 8[]
        [[text[i][j].scale(0.8) for i in range(6,9)] for j in range(2)]
        text[6][0].shift(6.5*LEFT+3.5*UP)
        text[6][1].next_to(text[6][0], RIGHT, 0.8*LARGE_BUFF)
        text[7][0].next_to(text[6][0], DOWN, MED_SMALL_BUFF)
        text[7][1].next_to(text[7][0], RIGHT, 0.8*LARGE_BUFF)
        text[8][0].next_to(text[6][0], DOWN, MED_SMALL_BUFF)
        text[8][1].next_to(text[7][0], RIGHT, 0.8*LARGE_BUFF)
        text.append(TexMobject(r"\text{Freeze the first line and vary}").scale(0.7)) #9
        text.append(TextMobject(r"{the y-intercept (c) of the other line}").scale(0.7)) #10
        text[9].to_edge(DOWN)
        text[9].shift(MED_SMALL_BUFF*UP)
        text[10].next_to(text[9], DOWN, SMALL_BUFF)
        text[9].add_background_rectangle()
        text[10].add_background_rectangle()
        m1 = TexMobject("{1}", color = LIGHT_GREY).scale(0.75)
        c1 = TexMobject("{0.5}", color = LIGHT_GREY).scale(0.75)
        m1.next_to(text[6][0], RIGHT, SMALL_BUFF)
        c1.next_to(text[6][1], RIGHT, SMALL_BUFF)

        m2 = TexMobject("{1.1}").scale(0.75)
        c2 = TexMobject("{0.5}").scale(0.75)
        m2.next_to(text[7][0], RIGHT, SMALL_BUFF)
        c2.next_to(text[7][1], RIGHT, SMALL_BUFF)

        m3 = TexMobject("{11}").scale(0.75)
        c3 = TexMobject("{0.5}").scale(0.75)
        m3.next_to(text[7][0], RIGHT, SMALL_BUFF)
        c3.next_to(text[7][1], RIGHT, SMALL_BUFF)

        line1 = Line(start = 7*LEFT+ 6.5*DOWN, end = 7*RIGHT + 7.5*UP, stroke_width = 3, color = BLUE_E)
        line2 = Line(start = 7*LEFT+ 7.2*DOWN, end = 7*RIGHT + 8.2*UP, stroke_width = 3, color = BLUE_B)
        line3 = Line(start = 0.682*LEFT+ 7*DOWN, end = 0.591*RIGHT + 7*UP, stroke_width = 3, color = BLUE_B)
        solution = Dot(color = RED_C, radius = 0.07).shift(0.5*UP)

        self.play(ShowCreation(text[0]))
        self.wait(1)
        self.play(Transform(text[0], text[1]))
        self.wait(1)
        self.play(ShowCreation(line1))
        self.wait(0.5)
        self.play(FadeOut(text[0]) ,FadeIn(VGroup(text[6][0],text[6][1], m1, c1)), run_time = 1.5)
        self.wait(1)

        self.play(ShowCreation(text[2]))
        self.wait(1)
        self.play(Transform(text[2], text[3]))
        self.wait(1)
        self.play(ShowCreation(line2))
        self.wait(0.5)
        self.play(FadeOut(text[2]) ,FadeIn(VGroup(text[7][0],text[7][1], m2, c2)), run_time = 1.5)
        self.play(FadeIn(solution))
        self.wait(1)

        self.play(ShowCreation(text[9]))
        self.play(ShowCreation(text[10]))
        self.wait(2.5)
        self.play(FadeOut(VGroup(*text[9:11])), run_time = 0.5)
        self.wait(2)
        # np.set_printoptions(precision=2)
        for c in np.arange(0.1,0.6, 0.1):
            c21 = TexMobject(str(round(c,2)+0.5)).scale(0.75)
            c21.shift(c2.get_center())
            self.play(Transform(c2, c21), ApplyMethod(line2.shift, 0.1*UP),
                      ApplyMethod(solution.shift, 1*LEFT+1*DOWN),
                      run_time = 0.5)
            # self.wait()
        for c in np.arange(0.1,1.0, 0.1):
            c21 = TexMobject(str(round(1.0-c,3))).scale(0.75)
            c21.shift(c2.get_center())
            self.play(Transform(c2, c21), ApplyMethod(line2.shift, 0.1*DOWN),
                      ApplyMethod(solution.shift, 1*UP+1*RIGHT),
                      run_time = 0.5)
        self.wait(2.5)
        self.play(FadeOut(VGroup(text[7][0],text[7][1], m2, c2, line2, solution)))

        solution = SmallDot(color = PINK, radius = 0.05).move_to(0.5*UP)
        self.play(ShowCreation(text[4]))
        self.wait(1)
        self.play(Transform(text[4], text[5]))
        self.wait(1)
        self.play(ShowCreation(line3))
        self.wait(0.5)
        self.play(FadeOut(text[4]) , FadeIn(VGroup(text[8][0],text[8][1], m3, c3)), run_time = 1.5)
        self.play(FadeIn(solution))
        self.wait(1)

        for c in np.arange(0.1,0.6, 0.1):
            c31 = TexMobject(str(round(c,2)+0.5)).scale(0.75)
            c31.shift(c3.get_center())
            self.play(Transform(c3, c31), ApplyMethod(line3.shift, 0.1*UP),
                      ApplyMethod(solution.shift, 0.01*LEFT+0.01*DOWN),
                      run_time = 0.5)
            # self.wait()
        for c in np.arange(0.1,1.0, 0.1):
            c31 = TexMobject(str(round(1.0-c,3))).scale(0.75)
            c31.shift(c3.get_center())
            self.play(Transform(c3, c31), ApplyMethod(line3.shift, 0.1*DOWN),
                      ApplyMethod(solution.shift, 0.01*UP+0.01*RIGHT),
                      run_time = 0.5)
        self.wait(2.5)
        self.play(FadeOut(VGroup(text[7][0],text[7][1], m2, c2, line3, solution)))
        self.wait(2)
