from manimlib.imports import *
import numpy as np

class Function_General(Scene):
    def construct(self):
        #TITLE DISPLAY
        title = TextMobject("What is a function?")
        title.scale(1.3)
        title.to_edge(UP)
        self.play(ShowCreation(title))
        self.wait(1)

        #DOMAIN SET DISPLAY
        domain_set = TextMobject(r"\{$\hspace{7pt}$\}")
        domain_set.scale(4.5)
        domain_set.shift(3.5*LEFT+0.5*DOWN)
        domain_set_text = TextMobject("some Set $A$")
        domain_set_text.shift(3.5*LEFT+2.3*DOWN)

        domain = []
        domain.append(Circle(radius = 0.25, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1) for i in range(3))
        domain.append(Square(side_length = 0.4, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1))
        domain.append(RegularPolygon(n = 5, side_length=0.2, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1))
        domain[0].shift(3.5*LEFT+0.1*UP)
        domain[1].shift(4*LEFT+0.7*DOWN)
        domain[2].shift(3.1*LEFT+1.2*DOWN)
        domain[2].scale(0.27)

        domaingp = VGroup(domain[0], domain[1], domain[2])
        self.play(ShowCreation(domaingp))
        self.play(ShowCreation(domain_set_text))
        self.wait(1)

        function_notation = TexMobject("f(x) = y", tex_to_color_map={"x": MAROON_C, "y": BLUE_E})
        function_notation.to_edge(UP)
        function_notation.shift(0.5*DOWN)
        function_notation.scale(1.7)

        self.play(ReplacementTransform(title, function_notation))
        self.wait(1)

        mid = [elem.copy() for elem in domain]
        self.add(mid[0], mid[1], mid[2])

        midmove = [0.55*LEFT+2.72*UP, 0.55*LEFT+2.72*UP, 0.55*LEFT+2.76*UP]
        rangeside = [1.95*RIGHT, 1.95*RIGHT+0.07*DOWN, 1.95*RIGHT+0.07*DOWN]
        rangemove = [3.5*RIGHT+0.1*UP, 4.2*RIGHT+0.9*DOWN, 3*RIGHT+1*DOWN]
        scale_list = (1.4, 1.6, 1.58)
        range = []

        for i in range(3):
            self.play(ApplyMethod(mid[i].move_to, midmove[i]))
            range.append(mid[i])
            range[i].scale(scale_list[i])
            range[i].shift(rangeside[i])
            range[i].set_color(BLUE_E)
            self.play(FadeOut(mid[i]), FadeIn(range[i]))
            self.play(ApplyMethod(range[i].move_to, rangemove[i]))
            self.wait(1)

        range_set = domain_set.copy()
        range_set.move_to(3.5*RIGHT+0.5*DOWN)
        self.play(ShowCreation(range_set))

        range_set_text= TextMobject("Range")
        range_set_text.shift(3.5*RIGHT+2.3*DOWN)
        self.play(ShowCreation(range_set_text))
        domain_set_transform_text = TextMobject("Domain"); domain_set_transform_text.shift(3.5*LEFT+2.3*DOWN)
        self.play(Transform(domain_set_text, domain_set_transform_text))

        self.wait(2)
        self.clear()
        self.wait(1)

class SingleVarFunction(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -3,
    "y_max": 3,
    "axes_color": GREY,
    "graph_origin": ORIGIN+DOWN,
    "x_axis_width": 8,
    "y_axis_height": 4.8,
    "exclude_zero_label": False
    }
    def construct(self):
        self.x_leftmost_tick = self.x_max+1
        self.y_bottom_tick = self.y_max+1  #do not want any ticks on the axes as of now
        X_TICKS_DISTANCE = self.x_axis_width/(self.x_max- self.x_min)
        Y_TICKS_DISTANCE = self.y_axis_height/(self.y_max- self.y_min)

        function_notation = TexMobject("f(x) = y", tex_to_color_map={"f": YELLOW_D, "x": MAROON_C, "y": BLUE_E})
        function_notation.to_edge(UP)
        self.play(Write(function_notation))
        self.wait(1)
        self.setup_axes(animate = True)
        self.wait(1)

        Dots = []
        for i in range(6):
            Dots.append(Dot(color = MAROON_C, radius = 0.07))
            Dots[i].shift(self.graph_origin + ((i%3)+1)*X_TICKS_DISTANCE*RIGHT)
        for i in range(6, 9):
            Dots.append(Dot(color = BLUE_C, radius = 0.07))
            Dots[i].shift(self.graph_origin + Y_TICKS_DISTANCE*np.sin(i-5)*UP)

        DotLabels = []
        for i in range(3):
            DotLabels.append(TextMobject(str(i+1)))
            DotLabels[i].scale(0.5)
            DotLabels[i].shift(self.graph_origin+((i+1)*X_TICKS_DISTANCE)*RIGHT+ 0.3*DOWN)

        #COMPACT_CODE_1
        self.play(ShowCreation(Dots[0]), ShowCreation(Dots[1]), ShowCreation(Dots[2]), ShowCreation(Dots[3]), ShowCreation(Dots[4]), ShowCreation(Dots[5]))
        self.play(ShowCreation(DotLabels[0]), ShowCreation(DotLabels[1]), ShowCreation(DotLabels[2]))
        self.wait(1.5)

        function_def = TexMobject(r"f(x) = \sin(x)", tex_to_color_map={"f": YELLOW_D, "x": MAROON_C, "sin": BLUE_E})
        function_def.to_edge(UP)
        self.play(Transform(function_notation, function_def))
        #COMPACT_CODE_2
        self.play(ApplyMethod(Dots[3].set_color, YELLOW_D), ApplyMethod(Dots[4].set_color, YELLOW_D), ApplyMethod(Dots[5].set_color, YELLOW_D))
        for i in range(3,6):
            self.play(ApplyMethod(Dots[i].shift, np.sin(i-2)*Y_TICKS_DISTANCE*UP) , ShowCreation(Dots[i+3]))

        x_line = Line(start = self.graph_origin + 5*LEFT*X_TICKS_DISTANCE, end = self.graph_origin + 5*RIGHT*X_TICKS_DISTANCE, color = MAROON_C)
        y_line = Line(start = self.graph_origin + 1*UP*Y_TICKS_DISTANCE, end = self.graph_origin + 1*DOWN*Y_TICKS_DISTANCE, color = BLUE_D)

        scale_list = [1, -1]
        Dashes = []
        ArTips = []
        ArAngles = [PI, 0]
        for i in range(2):
            Dashes.append(Rectangle(height = 0.01, width = 0.1, color = BLUE_D))
            Dashes[i].shift(self.graph_origin + scale_list[i]*Y_TICKS_DISTANCE*UP)
            ArTips.append(ArrowTip(color = MAROON_C, start_angle = ArAngles[i]))
            ArTips[i].scale(0.5)
            ArTips[i].shift(self.graph_origin+ scale_list[i]*4.7*X_TICKS_DISTANCE*LEFT)

        func_graph = self.get_graph(self.sin_graph, YELLOW_E)

        self.play(Write(x_line), ShowCreation(ArTips[0]), ShowCreation(ArTips[1]))
        self.wait(1)
        self.play(ShowCreation(func_graph), Write(y_line))
        #COMPACT_CODE_3
        self.play(ShowCreation(Dashes[0]), ShowCreation(Dashes[1]))
        self.wait(2)
        #COMPACT_CODE_4
        self.play(FadeOut(Dots[0]), FadeOut(Dots[1]),FadeOut(Dots[2]), FadeOut(Dots[3]),FadeOut(Dots[4]), FadeOut(Dots[5]),FadeOut(Dots[6]), FadeOut(Dots[7]),FadeOut(Dots[8]), FadeOut(DotLabels[0]), FadeOut(DotLabels[1]), FadeOut(DotLabels[2]) )
        self.wait(2)
        domain_text = TextMobject(r"Domain: $\mathbb{R}$\\Range: $\mathbb{R}$", tex_to_color_map={"Domain": MAROON_C, "Range": BLUE_E})
        domain_text.scale(0.7)
        domain_text.shift(UP+2*LEFT)
        self.play(Write(domain_text))
        self.wait(3)

    def sin_graph(self,x):
        return np.sin(x)
