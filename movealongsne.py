from manimlib.imports import *
import numpy as np

class SineIllustration(GraphScene):
    CONFIG = {
    "x_min": 0,
    "x_max": 2*np.pi,
    "y_min": -3,
    "y_max": 3,
    "axes_color": GREY,
    "graph_origin": 6*LEFT,
    "x_axis_label": r"$y = \sin(\theta)$",
    "y_axis_label": r"",
    }
    def construct(self):
        self.x_leftmost_tick = self.x_max+1
        self.y_bottom_tick = self.y_max+1
        circle = Circle()
        circle.shift(5*RIGHT)
        dot1 = Dot().shift(6*RIGHT)
        line = Line(5*RIGHT, 6*RIGHT, color = PURPLE)

        self.setup_axes(animate = True)
        func_graph = self.get_graph(self.sin_graph, YELLOW_E)
        dot2 = Dot().shift(6*LEFT)

        objgroup = VGroup(circle, func_graph, dot1, dot2)
        self.play(ShowCreation(objgroup))

        self.wait(1)
        self.play(MoveAlongPath(dot1, circle), MoveAlongPath(dot2, func_graph), run_time = 3)
        self.wait(3)

    def sin_graph(self,x):
        return np.sin(x)

        # return (0.5*x*x)
