from manimlib.imports import *

class TextTest(Scene):
    def construct(self):
        # test_text = TextMobject("Test text")
        domain_text = TextMobject(r"Domain: $\mathbb{R}$\\Range: $\mathbb{R}$")
        self.play(Write(domain_text))
        self.wait(2)

class HexTest(Scene):
    def construct(self):
        # hexagon = RegularPolygon(n = 5)
        # hexagon.round_corners(radius = 0.2)
        # self.play(ShowCreation(hexagon))

        curvearrow = ArrowTip(color = WHITE)
        curvearrow.shift(2*RIGHT)
        curvearrow.scale(0.5)
        self.play(ShowCreation(curvearrow))
        self.wait(2)
