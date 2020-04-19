from manimlib.imports import *

class Example1(Scene):
    def construct(self):
        # self.add(Rectangle(width = 2*FRAME_X_RADIUS, height = 2*FRAME_Y_RADIUS))
        examples = [
                TexMobject(r"{\alpha_1 = \{ p \in \mathbb{Q} \mid  p <101 \} }"),
                TexMobject(r"{\alpha_2 = \{ q \in \mathbb{Q} \mid q<33.\overline{33}  \} }"),
                TexMobject(r"{\beta_1  = \{ r \in \mathbb{Q} \mid r^2 < 7 \hspace{2.5pt} or \hspace{2.5pt}r<0\} }"),
        ]
        nums = [101, 33.33, 2.6457]
        self.x_min = -120
        self.x_max = 120
        self.scale = 0.05
        for i in range(3):
            self.writeexample(examples[i])
            self.wait(2)
            if not i:
                self.createQLine()
                self.wait()
            pointnum = self.marknum(nums[i])
            rectangle = self.drawrectangle(nums[i])
            self.wait(2)
            if i != 2:
                self.play(FadeOut(VGroup(examples[i], pointnum, rectangle)))
        self.wait(2)

    def writeexample(self, example):
        example.shift(2*UP)
        self.play(Write(example))

    def createQLine(self):
        self.Q = NumberLine(
                    color= PURPLE,
                    x_min= self.x_min,
                    x_max= self.x_max,
                    unit_size= self.scale,
                    include_ticks= True,
                    leftmost_tick= 0,
                    tick_frequency = 200,
                    numbers_with_elongated_ticks= [],
                    include_numbers= False,
                    numbers_to_show= [0],
                    )
        Q = self.Q
        tip1 = ArrowTip(length = 0.2, color = PURPLE)
        tip2 = ArrowTip(length = 0.2, start_angle =  2*PI, color = PURPLE)
        tip1.shift(Q.get_start()- tip1.get_tip_point()/2)
        tip2.shift(Q.get_end() - tip2.get_tip_point()/2)
        label = TexMobject(r"\mathbb{Q}", color = PURPLE).shift(Q.get_end()+ MED_LARGE_BUFF*UP)
        Qtip = VGroup(Q, tip1, tip2, label)

        self.play(ShowCreation(Qtip))

    def marknum(self, num):
        if num == 2.6457:
             latexnum = r"\sqrt7"
             opacity = 1
        else:
            latexnum = str(num)
            opacity = 0
        pointnum = Circle(color = YELLOW, fill_color = BLACK, fill_opacity = opacity, radius = 0.04, stroke_width = 2).shift(num*self.scale*RIGHT)
        pointnumlabel = (TexMobject(latexnum).set_color(YELLOW)).scale(0.75)
        pointnumlabel.next_to(pointnum, DOWN, buff = 2.3*SMALL_BUFF)
        pointnum = VGroup(pointnum, pointnumlabel)

        self.play(FadeIn(pointnum))
        return pointnum

    def drawrectangle(self, num):
        rectangle = Polygon(self.Q.get_start()+0.15*UP, num*self.scale*RIGHT+0.04*LEFT+0.15*UP,
                        num*self.scale*RIGHT+0.04*LEFT+0.15*DOWN, self.Q.get_start()+0.15*DOWN,
                        stroke_width = 2, stroke_color = RED_E)
        rectangle2 = Polygon(self.Q.get_start()+0.15*UP, num*self.scale*RIGHT+0.04*LEFT+0.15*UP,
                        num*self.scale*RIGHT+0.04*LEFT+0.15*DOWN, self.Q.get_start()+0.15*DOWN,
                        stroke_width = 0, fill_opacity = 0.5, fill_color = RED)
        self.play(ShowCreation(rectangle))
        self.wait(1)
        self.play(ReplacementTransform(rectangle, rectangle2))

        return VGroup(rectangle2)
