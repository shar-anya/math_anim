from manimlib.imports import *
import numpy as np

class Function_General(Scene):
    def construct(self):
        #TITLE
        title = TextMobject("What is a function?")
        title.scale(1.3)
        title.to_edge(UP)
        #FUNCTION NOTATION
        function_notation = TexMobject("f(x) = y", tex_to_color_map={"f": YELLOW_D, "x": MAROON_C, "y": BLUE_E})
        function_notation.to_edge(UP)
        function_notation.shift(0.5*DOWN)
        function_notation.scale(1.7)
        #TEXT FOR DOMAIN AND RANGE SETS
        domain_set_text = TextMobject(r"some Set $A$")
        domain_set_text.shift(3.5*LEFT+2.08*DOWN)
        domain_set_text.scale(0.8)
        domain_set_text1 = TextMobject("of shapes")
        domain_set_text1.shift(3.5*LEFT+2.6*DOWN)
        domain_set_text1.scale(0.8)
        domain_set_transform_text = TextMobject("Domain"); domain_set_transform_text.shift(3.5*LEFT+2.3*DOWN)
        range_set_text= TextMobject("Range")
        range_set_text.shift(3.5*RIGHT+2.3*DOWN)
        #DOMAIN {}
        domain_set = TextMobject(r"\{$\hspace{7pt}$\}")
        domain_set.scale(4.5)
        domain_set.shift(3.5*LEFT+0.5*DOWN)
        #RANGE {}
        range_set = domain_set.copy()
        range_set.move_to(3.5*RIGHT+0.5*DOWN)
        #CREATE SET OF DOMAIN SHAPES
        domain_shapes = []
        domain_shapes.append(Circle(radius = 0.25, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1))
        domain_shapes.append(Square(side_length = 0.4, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1))
        domain_shapes.append(RegularPolygon(n = 5, side_length=0.2, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1))
        domain_shapes[0].shift(3.5*LEFT+0.1*UP)
        domain_shapes[1].shift(4*LEFT+0.7*DOWN)
        domain_shapes[2].shift(3.1*LEFT+1.2*DOWN)
        domain_shapes[2].scale(0.27)
        domaingp = VGroup(*domain_shapes) #Grouping Domain set objects
        #CREATE SET OF INTERMEDIATE SHAPES
        mid_shapes = []
        for i in range(3):
            mid_shapes.append(domain_shapes[i].copy())
        #CREATE SET OF RANGE SHAPES
        range_shapes = []
        #TUPLES with constants for moving shapes
        midmove = (0.55*LEFT+2.72*UP, 0.55*LEFT+2.72*UP, 0.55*LEFT+2.76*UP)
        rangeside = (1.95*RIGHT, 1.95*RIGHT+0.07*DOWN, 1.95*RIGHT+0.07*DOWN)
        rangemove = (3.5*RIGHT+0.1*UP, 4.2*RIGHT+0.9*DOWN, 3*RIGHT+1*DOWN)
        scale_list = (1.4, 1.6, 1.58)

        #ANIMATION STARTS HERE
        self.play(Write(title))
        self.wait(1)

        self.play(ShowCreation(domain_set))
        self.play(ShowCreation(domaingp, run_time = 2))
        self.play(Write(domain_set_text))
        self.play(Write(domain_set_text1))
        self.wait(1)

        self.play(ReplacementTransform(title, function_notation))
        self.wait(1)
        self.add(mid_shapes[0], mid_shapes[1], mid_shapes[2])

        for i in range(3):
            self.play(ApplyMethod(mid_shapes[i].move_to, midmove[i]))
            range_shapes.append(mid_shapes[i].copy())
            range_shapes[i].scale(scale_list[i])
            range_shapes[i].shift(rangeside[i])
            range_shapes[i].set_color(BLUE_E)
            self.wait(0.5)
            self.play(FadeOut(mid_shapes[i]), FadeIn(range_shapes[i]))
            self.play(ApplyMethod(range_shapes[i].move_to, rangemove[i]))
            self.wait(1)
        #
        # self.play(ShowCreation(range_set))
        # self.play(ShowCreation(range_set_text))
        # self.play(Transform(domain_set_text, domain_set_transform_text))
        #
        # self.wait(2)
        # self.clear()
        # self.wait(1)

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
        #INITIALIZATION OF VARIABLES
        self.x_leftmost_tick = self.x_max+1
        self.y_bottom_tick = self.y_max+1  #do not want any ticks on the axes as of now
        X_TICKS_DISTANCE = self.x_axis_width/(self.x_max- self.x_min)
        Y_TICKS_DISTANCE = self.y_axis_height/(self.y_max- self.y_min)

        function_notation = TexMobject("f(x) = y", tex_to_color_map={"f": YELLOW_D, "x": MAROON_C, "y": BLUE_E})
        function_notation.to_edge(UP)
        function_def = TexMobject(r"f(x) = \sin(x)", tex_to_color_map={"f": YELLOW_D, "x": MAROON_C, "sin": BLUE_E})
        function_def.to_edge(UP)

        dot_color = (BLUE_E, BLUE_C, BLUE_D)
        Dots = []
        for i in range(6):
            Dots.append(Dot(color = MAROON_C, radius = 0.07))
            Dots[i].shift(self.graph_origin + ((i%3)+1)*X_TICKS_DISTANCE*RIGHT)
        for i in range(6, 9):
            Dots.append(Dot(color = dot_color[i-6], radius = 0.07))
            Dots[i].shift(self.graph_origin + Y_TICKS_DISTANCE*np.sin(i-5)*UP)
        dots_gp1 = VGroup(*Dots[:6])
        dots_gp2 = VGroup(*Dots[3:6])

        DotLabels = []
        for i in range(3):
            DotLabels.append(TextMobject(str(i+1)))
            DotLabels[i].scale(0.5)
            DotLabels[i].shift(self.graph_origin+((i+1)*X_TICKS_DISTANCE)*RIGHT+ 0.3*DOWN)
        dotlabel_gp = VGroup(*DotLabels)

        domain_text1 = TextMobject(r"Domain", tex_to_color_map={"Domain": MAROON_C})
        range_text1 = TextMobject(r"Range", tex_to_color_map=  {"Range": BLUE_E})
        domain_text1.shift(self.graph_origin + 1.55*RIGHT + 0.7*DOWN)
        range_text1.shift(self.graph_origin + 0.8*LEFT + 0.4*UP)
        domain_text1.scale(0.6)
        range_text1.scale(0.6)

        domain_text2 = TextMobject(r"Domain : $\mathbb{R}$", tex_to_color_map={"Domain": MAROON_C})
        range_text2 = TextMobject(r"Range : [-1,1]", tex_to_color_map={"Range": MAROON_C})
        domain_text2.shift(self.graph_origin + 1.6*RIGHT + 0.7*DOWN)
        range_text2.shift(self.graph_origin + 1.4*LEFT + 0.4*UP)
        domain_text2.scale(0.7)
        range_text2.scale(0.7)

        x_line = Line(start = self.graph_origin + 5*LEFT*X_TICKS_DISTANCE, end = self.graph_origin + 5*RIGHT*X_TICKS_DISTANCE)
        y_line = Line(start = self.graph_origin + 1*UP*Y_TICKS_DISTANCE, end = self.graph_origin + 1*DOWN*Y_TICKS_DISTANCE)

        scale_list = [1, -1]
        Dashes = []
        ArTips = []
        ArAngles = [PI, 0]

        for i in range(2):
            Dashes.append(Rectangle(height = 0.01, width = 0.1))
            Dashes[i].shift(self.graph_origin + scale_list[i]*Y_TICKS_DISTANCE*UP)
            ArTips.append(ArrowTip(color = WHITE, start_angle = ArAngles[i]))
            ArTips[i].scale(0.5)
            ArTips[i].shift(self.graph_origin+ scale_list[i]*4.7*X_TICKS_DISTANCE*LEFT)

        #ANIMATION BEGINS HERE
        self.play(Write(function_notation))
        self.wait(1)
        self.setup_axes(animate = True)
        self.wait(1)

        self.play(ShowCreation(dots_gp1))
        self.play(ShowCreation(dotlabel_gp))
        self.wait(0.5)
        self.play(Write(domain_text1))
        self.wait(1.5)
        self.play(Transform(function_notation, function_def))
        self.wait(0.7)
        self.play(ApplyMethod(dots_gp2.set_color, YELLOW_D))
        #SHIFTING YELLOW DOTS UP AND SHOWING RANGE DOTS
        for i in range(3,6):
            self.play(ApplyMethod(Dots[i].shift, np.sin(i-2)*Y_TICKS_DISTANCE*UP) , ShowCreation(Dots[i+3]))
            self.wait(0.3)
        self.wait(0.2)
        self.play(Write(range_text1))
        self.wait(2)

        func_graph = self.get_graph(self.sin_graph, YELLOW_E)
        self.play(Write(x_line), ShowCreation(ArTips[0]), ShowCreation(ArTips[1]))
        self.wait(0.5)
        self.play(Transform(domain_text1, domain_text2))
        self.wait(1.5)

        self.play(ShowCreation(func_graph), Write(y_line))
        self.play(ShowCreation(VGroup(*Dashes)))
        self.wait(0.5)
        self.play(Transform(range_text1, range_text2))
        self.wait(1.5)

        self.play(FadeOut(dots_gp1), FadeOut(dots_gp2), FadeOut(VGroup(*Dots[6:9])), FadeOut(dotlabel_gp))
        self.wait(2)
        self.remove(domain_text1, range_text1)
        self.play(ApplyMethod(domain_text2.move_to, self.graph_origin+3*Y_TICKS_DISTANCE*UP+2.2*LEFT), ApplyMethod(range_text2.move_to, self.graph_origin+2.4*Y_TICKS_DISTANCE*UP+2.1*LEFT))
        self.wait(3)

    def sin_graph(self,x):
        return np.sin(x)
