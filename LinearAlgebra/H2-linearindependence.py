# Animation clip illustrating linear dependence and independence
# FILEID: H2
from manimlib.imports import *

VECTORS = [ ([0.5,1], [1.5,2], [2,3]),
            ([1,2], [2,3], [3,4], [4,5]),
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
        "n": 0
    }

class Scene1(LinearTransformationScene):
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
        clist = [
                TextMobject(r"$c_1 = $"),
                TextMobject(r"$c_2 = $"),
                TextMobject(r"$c_2 = $"),
        ]
        clabelgroup = VGroup(*clist)
        clabelgroup.scale = 0.8
        clabelgroup.shift(6.5*LEFT+3.5*UP)
        for i in range(1,3):
            clist[i].next_to(clist[i-1], DOWN, MED_SMALL_BUFF)

        colors = [YELLOW, BLUE, MAROON_C]
        v = VECTORS[n] # ( [0.5,1] , [1.5,2] , [2,3] )
        labelgp = VGroup()
        vecgroup = VGroup()
        for i in range(len(v)):
            v1 = self.add_vector(v[i], stroke_width = 4, color = colors[i])
            vecgroup.add(v1)
            vlabel = self.get_vector_label(v1, str(v[i][0]) + r"\imath" + "+" + str(v[i][1]) + r"\jmath", at_tip = True)
            vlabel.scale(0.7)
            labelgp.add(vlabel)
            self.play(ShowCreation(vlabel, run_time = 0.5))
            self.wait(0.5)
        self.wait(0.5)
        self.play(FadeOut(labelgp))
        self.wait(0.5)
        self.play(ShowCreation(clabelgroup))
        self.wait(1)

        c = [1, 1, -1]
        cgroup = VGroup(*[TextMobject(str(c[i]), color = colors[i]) for i in range(len(c))])
        [cgroup[i].next_to(clabelgroup[i], RIGHT, MED_SMALL_BUFF) for i in range(len(c))]
        self.play(Write(cgroup[0]), Write(cgroup[1]))
        self.wait(1)

        self.play(ApplyMethod(vecgroup[1].shift,vecgroup[0].get_end()))
        v0v1 = Vector(vecgroup[1].get_end(), color = GREEN)
        self.play(GrowArrow(v0v1))
        self.wait(1)
        self.play(FadeOut(vecgroup[:2]))
        self.wait(1)

        self.play(Write(cgroup[2]))
        self.wait(0.5)
        mv2 = Vector(-1*vecgroup[2].get_end(), color = MAROON_C)
        # print(-1*vecgroup[2].get_end())
        self.play(Transform(vecgroup[2],mv2))
        # self.remove(vecgroup[2])
        self.wait(2)

        zero = Dot(ORIGIN, color = WHITE)
        self.play(Transform(VGroup(v0v1, vecgroup[2]), zero))
        self.wait(2)

        
