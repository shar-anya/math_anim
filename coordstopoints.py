from manimlib.imports import *
import numpy as np

class Scene1(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN
    }
    def construct(self):
        self.setup_axes(animate=True)
        xaxis = self.axes[0]
        x_points = list(range(-5,6))
        y_points = [np.cos(x) for x in x_points]
        for i in range(len(x_points)):
            line = Line(start = xaxis.n2p(x_points[i]), end = (xaxis.n2p(x_points[i]) + [0,y_points[i], 0]),  color=YELLOW)
            dot = Dot(line.get_end())
            self.play(ShowCreation(line), ShowCreation(dot), run_time = 0.5)
        self.wait(2)
