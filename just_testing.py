from manimlib.imports import *

class TextTest(Scene):
    def construct(self):
        # test_text = TextMobject("Test text")
        domain_text = TextMobject(r"Domain: $\mathbb{R}$\\Range: $\mathbb{R}$")
        self.play(Write(domain_text))
        self.wait(2)

class HexTest(Scene):
    def construct(self):
        # hexagon = RegularPolygon(n = 2)
        # hexagon.round_corners(radius = 0.2)
        # self.play(ShowCreation(hexagon))
        circle = [Circle(radius = 0.25, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1) for i in range(3)]

        # curvearrow = ArrowTip(color = WHITE)
        # curvearrow.shift(2*RIGHT)
        # curvearrow.scale(0.5)
        self.play(ShowCreation(circle[1]))
        self.wait(2)
