# Animation clip illustrating linear dependence and independence
# FILEID: H2
from manimlib.imports import *

VECTORS = [
            [[-2,2], [3,1], [1,3]]
            ]
class DisplayVectorSet(Scene):
    def construct(self):
        self.vectordisplay(VECTORS[self.n])
        self.wait(2)

    def vectordisplay(self, vectors):
        text = TextMobject(r"Consider the set of vectors in $\mathbb{R}^2$")
        text.shift(2*UP)
        text.scale(0.9)
        matrices = VGroup(*[Matrix(v) for v in vectors])
        matrices.scale(0.9)
        matrices.next_to(text, DOWN, MED_LARGE_BUFF)
        self.play(Write(text))

        comma = TextMobject(",")
        comma.scale(0.8)
        vgp = VGroup()

        vlby2 = int(len(matrices)/2)
        if (len(matrices)%2 == 1): # 0 1 2 3 4
            for i in range(vlby2-1, -1, -1):
                c = comma.copy()
                c.next_to(matrices[i+1], LEFT, MED_SMALL_BUFF)
                matrices[i].next_to(c, LEFT, MED_SMALL_BUFF)
                vgp.add(c, matrices[i])
            vgp.add(matrices[vlby2])
            for i in range(vlby2+1, len(matrices)):
                c = comma.copy()
                c.next_to(matrices[i-1], RIGHT, MED_SMALL_BUFF)
                matrices[i].next_to(c, RIGHT, MED_SMALL_BUFF)
                vgp.add(c, matrices[i])
        else: # 0 1 2 3 4 5
            c = comma.copy()
            c.move_to(matrices[vlby2].get_center())
            vgp.add(c)
            matrices[vlby2].next_to(c, RIGHT, MED_SMALL_BUFF)
            matrices[vlby2-1].next_to(c, LEFT, MED_SMALL_BUFF)
            vgp.add(*matrices[vlby2-1:vlby2+1])
            for i in range(vlby2-2, -1, -1):
                c = comma.copy()
                c.next_to(matrices[i+1], LEFT, MED_SMALL_BUFF)
                matrices[i].next_to(c, LEFT, MED_SMALL_BUFF)
                vgp.add(c, matrices[i])
            for i in range(vlby2+1, len(matrices)):
                c = comma.copy()
                c.next_to(matrices[i-1], RIGHT, MED_SMALL_BUFF)
                matrices[i].next_to(c, RIGHT, MED_SMALL_BUFF)
                vgp.add(c, matrices[i])
        b1 = Brace(matrices[0], LEFT)
        b2 = Brace(matrices[-1], RIGHT)
        vgp.add(b1, b2)
        self.play(ShowCreation(vgp, run_time = 3))

class DisplayVectorSet0(DisplayVectorSet):
    CONFIG = {
        "n": 0
    }

class DisplayVectorSet1(DisplayVectorSet):
    CONFIG = {
        "n": 1
    }

class VectorPlay(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "show_coordinates": False,
        "show_basis_vectors": False,
        "basis_vector_stroke_width": 3,
    }

    def construct(self):
        self.setup()
        self.playscene(0)
        self.wait(1)

    def playscene(self, n):
        ctext = [
                TextMobject(r"$c_1 = $"),
                TextMobject(r"$c_2 = $"),
                TextMobject(r"$c_2 = $"),
        ]
        for i in range(1,3):
            ctext[i].next_to(ctext[i-1], DOWN, MED_SMALL_BUFF)
        clabelgp = VGroup(*ctext)
        clabelgp.scale = 0.8
        clabelgp.shift(6.5*LEFT+3.5*UP)
        cvalues = [2, -1, -1]
        colors = [YELLOW, BLUE, MAROON_C]
        cvaluegp = VGroup(*[TextMobject(str(cvalues[i]), color = colors[i]) for i in range(len(colors))])
        [cvaluegp[i].next_to(clabelgp[i], RIGHT, MED_SMALL_BUFF) for i in range(len(colors))]
        labelgp = VGroup()
        vectorgp = VGroup()
        vectors_list = VECTORS[n]

        for i in range(len(vectors_list)):
            vector = self.add_vector(vectors_list[i], stroke_width = 4, color = colors[i])
            vector_label = self.get_vector_label(vector, str(vectors_list[i][0]) + r"\imath" + "+" + str(vectors_list[i][1]) + r"\jmath", at_tip = True)
            vector_label.scale(0.7)
            vectorgp.add(vector)
            labelgp.add(vector_label)
            self.play(ShowCreation(vector_label, run_time = 0.5))
            self.wait(0.5)

        self.wait(0.5)
        self.play(FadeOut(labelgp))
        self.wait(0.5)
        self.play(ShowCreation(clabelgp))
        self.wait(1)

        self.play(Write(cvaluegp[0]), Write(cvaluegp[1]))
        self.wait(1)

        vectorgp1 = VGroup()
        for i in range(len(vectors_list))
        vectors_list
        for i in range(1):
            vector = self.add_vector(vectors_list[i], stroke_width = 4, color = colors[i], animate = False)
            vectorgp1.add(Vector(cvalues[i]*vectors_list[i][0]))
        self.add(vectorgp1)
        # self.play(ApplyMethod(vecgroup[0].scale, c[0]))
        # self.play(ApplyMethod(vecgroup[0].shift, -1*vecgroup[0].get_start()))
        # self.play(ApplyMethod(vecgroup[1].scale, c[1]))

        # self.play(ApplyMethod(vecgroup[1].shift,vecgroup[0].get_end()))
        # v0v1 = Vector(vecgroup[1].get_end(), color = GREEN)
        # self.play(GrowArrow(v0v1))
        # self.wait(1)
        # self.play(FadeOut(vecgroup[:2]))
        # self.wait(1)
        #
        # self.play(Write(cgroup[2]))
        # self.wait(0.5)
        # mv2 = Vector(-1*vecgroup[2].get_end(), color = MAROON_C)
        # self.play(Transform(vecgroup[2],mv2))
        self.wait(2)

        # zero = Dot(ORIGIN, color = WHITE)
        # self.play(Transform(VGroup(v0v1, vecgroup[2]), zero))
        # self.wait(2)
