from manimlib.imports import *

class SetIntersection(Scene): # inheriting class Scene ...
    def construct(self):
        circleA = Circle(radius= 2, color= BLACK, fill_color= BLUE_D, fill_opacity= 0.5)
        circleB = Circle(radius= 1.5, color= BLACK, fill_color= YELLOW_D, fill_opacity= 0.5, stroke_width=0.1)
        labelA = TextMobject("A")
        labelB = TextMobject("B")

        circleA.shift(2.5*RIGHT)
        circleB.shift(2.5*LEFT)
        labelA.shift(3.5*RIGHT)
        labelB.shift(3.3*LEFT)

        self.play(ShowCreation(circleA))
        self.play(ShowCreation(labelA))
        self.play(ShowCreation(circleB))
        self.play(ShowCreation(labelB))
        self.play(ApplyMethod(circleA.shift,1.5*LEFT), ApplyMethod(circleB.shift,1.5*RIGHT), ApplyMethod(labelA.shift, 1.5*LEFT), ApplyMethod(labelB.shift, 1.5*RIGHT))

        labelAB= TextMobject(r"A $\cap$ B")
        labelAB.shift(0.2*LEFT)
        labelAB.scale(0.7)
        self.play(ShowCreation(labelAB))
        self.wait(3)
