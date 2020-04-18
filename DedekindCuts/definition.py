from manimlib.imports import *

class Scene2(Scene):
    def construct(self):
        self.playpoint(3)
        self.wait(2)
        self.clear()
        self.createQLine()
        self.wait(1)
        num1 = 11
        num2 = 25
        saytext1 = self.saynum(num1)
        self.marknum(num1)
        self.wait(0.5)
        alsostuff1 = self.drawfromnum(num1)
        self.wait(1)
        self.play(FadeOut(saytext1), FadeOut(alsostuff1))
        self.saynum(num2)
        self.marknum(num2)
        self.wait(0.5)
        self.drawfromnum(num2)
        self.wait(2)
        self.clear()
        self.implication()
        self.wait(2)

    def playpoint(self, rt):
        point2= TexMobject(r"\text{2. If }",r"{p \in \alpha}", r"\text{ and }", "{r<p}", r"\text{, then }", r"{r \in \alpha}").shift(0.25*UP)
        self.play(ShowCreation(point2, run_time = rt))

    def createQLine(self):
        self.Q = NumberLine(
                    color= PURPLE,
                    x_min= -40,
                    x_max= 40,
                    unit_size= 0.1,
                    include_ticks= True,
                    leftmost_tick= 0,
                    tick_frequency = 100,
                    numbers_with_elongated_ticks= [],
                    include_numbers= True,
                    numbers_to_show= [0],
                    )
        Q = self.Q
        tip1 = ArrowTip(length = 0.2, color = PURPLE)
        tip2 = ArrowTip(length = 0.2, start_angle =  2*PI, color = PURPLE)
        tip1.shift(Q.get_start()- tip1.get_tip_point()/2)
        tip2.shift(Q.get_end() - tip2.get_tip_point()/2)
        label = TexMobject(r"\mathbb{Q}", color = PURPLE).shift(Q.get_end()+ MED_LARGE_BUFF*UP)
        Qtip = VGroup(Q, tip1, tip2, label)

        self.play(Write(Qtip))

    def saynum(self, num):
        latex = "{"+ str(num) + "}"
        saytext = TexMobject(r"\text{Suppose }", latex, r"{\hspace{3pt}\in \alpha").scale(0.7)
        saytext.shift(2*UP)

        self.play(Write(saytext))
        return saytext

    def marknum(self, num):
        pointnum = SmallDot(color = RED).shift(num*0.1*RIGHT)
        pointnumlabel = TexMobject(str(num)).scale(0.75)
        pointnumlabel.next_to(pointnum, DOWN, buff = 2.2*SMALL_BUFF)
        pointnum = VGroup(pointnum, pointnumlabel)

        self.play(FadeIn(pointnum))

    def drawfromnum(self, num):
        alsoalpha = Line(start = num*0.1*RIGHT, end = self.Q.get_start(), color = RED)
        then = TextMobject("Then").scale(0.7).shift(4.6*LEFT+ 1.25*DOWN)
        alsoalpha2 = alsoalpha.copy()
        alsotext = TextMobject(r"also belongs to $\alpha$").scale(0.7)

        self.play(ShowCreation(alsoalpha, run_time = 1.5))
        self.add(alsoalpha2)
        self.play(FadeIn(then), ApplyMethod(alsoalpha2.shift,1.3*DOWN))
        alsotext.next_to(alsoalpha2, RIGHT)
        self.play(FadeIn(alsotext))
        return VGroup(alsoalpha2, then, alsotext)

    def implication(self):
        implication2 = TexMobject(r"{\implies \alpha}", r"\text{doesn't have a lower bound}")
        self.playpoint(0.5)
        self.play(Write(implication2, run_time = 2))
