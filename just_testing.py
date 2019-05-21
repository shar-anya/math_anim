from manimlib.imports import *

class TextTest(Scene):
    def construct(self):
        test_text = TextMobject("Test text")
        self.play(Write(test_text))
        self.wait(2)

class HexTest(Scene):
    def construct(self):
        hexagon = RegularPolygon(n = 5)
        hexagon.round_corners(radius = 0.2)
        self.play(ShowCreation(hexagon))
        self.wait(2)
