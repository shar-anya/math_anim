from manimlib.imports import *
import numpy as np

class Function_General(Scene):
    def construct(self):
        title = TextMobject("What is a function?")
        title.scale(1.3)
        title.to_edge(UP)
        self.play(ShowCreation(title))
        self.wait(1)

        # INTRODUCTION
        set1 = TextMobject(r"\{$\hspace{7pt}$\}")
        set1.scale(4.5)
        set1.shift(3.5*LEFT+0.5*DOWN)
        set1text = TextMobject("some Set $A$")
        set1text.shift(3.5*LEFT+2.3*DOWN)

        circle1 = Circle(radius = 0.25, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1)
        circle1.shift(3.5*LEFT+0.1*UP)
        square1 = Square(side_length = 0.4, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1)
        square1.shift(4*LEFT+0.7*DOWN)
        pentagon1 = RegularPolygon(n = 5, side_length=0.2, color = MAROON_C, fill_color = MAROON_C, fill_opacity = 1)
        pentagon1.shift(3.1*LEFT+1.2*DOWN)
        pentagon1.scale(0.27)

        self.play(ShowCreation(set1))
        self.play(ShowCreation(circle1), ShowCreation(square1), ShowCreation(pentagon1))
        self.play(ShowCreation(set1text))
        self.wait(1)

        function_notation = TexMobject("f(x) = y", tex_to_color_map={"x": MAROON_C, "y": BLUE_E})
        function_notation.to_edge(UP)
        function_notation.shift(0.5*DOWN)
        function_notation.scale(1.7)

        self.play(ReplacementTransform(title, function_notation))
        self.wait(1)

        circle2 = circle1.copy()
        square2 = square1.copy()
        pentagon2 = pentagon1.copy()
        self.add(circle2, square2, pentagon2)

        self.play(ApplyMethod(circle2.move_to, 0.55*LEFT+2.72*UP))
        circle3 = circle2.copy()
        circle3.scale(1.4)
        circle3.shift(1.95*RIGHT)
        circle3.set_color(BLUE_E)
        self.play(FadeOut(circle2), FadeIn(circle3))
        self.play(ApplyMethod(circle3.move_to, 3.5*RIGHT+0.1*UP))
        self.wait(1)

        self.play(ApplyMethod(square2.move_to, 0.55*LEFT+2.71*UP))
        square3 = square2.copy()
        square3.scale(1.6)
        square3.shift(1.95*RIGHT+0.07*DOWN)
        square3.set_color(BLUE_E)
        self.play(FadeOut(square2), FadeIn(square3))
        self.play(ApplyMethod(square3.move_to, 4.2*RIGHT+0.9*DOWN))
        self.wait(1)

        self.play(ApplyMethod(pentagon2.move_to, 0.55*LEFT+2.76*UP))
        pentagon3 = pentagon2.copy()
        pentagon3.scale(1.58)
        pentagon3.shift(1.95*RIGHT+0.07*DOWN)
        pentagon3.set_color(BLUE_E)
        self.play(FadeOut(pentagon2), FadeIn(pentagon3))
        self.play(ApplyMethod(pentagon3.move_to, 3*RIGHT+1*DOWN))
        self.wait(1)

        set2 = TextMobject(r"\{$\hspace{7pt}$\}"); set2.scale(4.5); set2.move_to(3.5*RIGHT+0.5*DOWN)
        self.play(ShowCreation(set2))

        set2text= TextMobject("Range"); set2text.shift(3.5*RIGHT+2.3*DOWN)
        self.play(ShowCreation(set2text))
        set1_transform_text = TextMobject("Domain"); set1_transform_text.shift(3.5*LEFT+2.3*DOWN)
        self.play(Transform(set1text, set1_transform_text))

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

        dot1 = Dot(color = MAROON_C)
        dot1.shift(self.graph_origin + X_TICKS_DISTANCE*RIGHT)
        dot2 = Dot(color = MAROON_C)
        dot2.shift(self.graph_origin + X_TICKS_DISTANCE*2*RIGHT)
        dot3 = Dot(color = MAROON_C)
        dot3.shift(self.graph_origin + X_TICKS_DISTANCE*3*RIGHT)

        dot1b = Dot(color = BLUE_A)
        dot1b.shift(self.graph_origin + Y_TICKS_DISTANCE*np.sin(1)*UP)
        dot2b = Dot(color = BLUE_E)
        dot2b.shift(self.graph_origin + Y_TICKS_DISTANCE*np.sin(2)*UP)
        dot3b = Dot(color = BLUE_C)
        dot3b.shift(self.graph_origin + Y_TICKS_DISTANCE*np.sin(3)*UP)

        dot1a= dot1.copy()
        dot2a= dot2.copy()
        dot3a= dot3.copy()

        dotlabel1 = TextMobject("1"); dotlabel1.scale(0.5)
        dotlabel1.shift(self.graph_origin+(X_TICKS_DISTANCE)*RIGHT+ 0.3*DOWN)
        dotlabel2 = TextMobject("2"); dotlabel2.scale(0.5)
        dotlabel2.shift(self.graph_origin+(2*X_TICKS_DISTANCE)*RIGHT+ 0.3*DOWN)
        dotlabel3 = TextMobject("3"); dotlabel3.scale(0.5)
        dotlabel3.shift(self.graph_origin+(3*X_TICKS_DISTANCE)*RIGHT+ 0.3*DOWN)

        self.play(ShowCreation(dot1), ShowCreation(dot2), ShowCreation(dot3), ShowCreation(dot1a), ShowCreation(dot2a), ShowCreation(dot3a))
        self.play(ShowCreation(dotlabel1), ShowCreation(dotlabel2), ShowCreation(dotlabel3))

        function_def = TexMobject(r"f(x) = sin(x)", tex_to_color_map={"f": YELLOW_D, "x": MAROON_C, "sin": BLUE_E})
        function_def.to_edge(UP)
        self.play(Transform(function_notation, function_def))

        self.play(ApplyMethod(dot1a.set_color, YELLOW_C), ApplyMethod(dot2a.set_color, YELLOW_D), ApplyMethod(dot3a.set_color, YELLOW_D))
        self.play(ApplyMethod(dot1a.shift, np.sin(1)*Y_TICKS_DISTANCE*UP), ShowCreation(dot1b))
        self.play(ApplyMethod(dot2a.shift, np.sin(2)*Y_TICKS_DISTANCE*UP), ShowCreation(dot2b))
        self.play(ApplyMethod(dot3a.shift, np.sin(3)*Y_TICKS_DISTANCE*UP), ShowCreation(dot3b))

        func_graph = self.get_graph(self.func_to_graph,YELLOW_E)
        self.play(ShowCreation(func_graph))
        self.wait(3)

    def func_to_graph(self,x):
        return np.sin(x)
