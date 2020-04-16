from manimlib.imports import *
import numpy as np

class Scene1(Scene):
    def construct(self):
        axes1 = Axes(
        x_min = -3,
        x_max = 3,
        y_min = -1.5,
        y_max = 1.5,
        x_labeled_nums = [-2, 2],
        center_point= 3.4*LEFT,
        x_axis_config={
                "unit_size": 1,
                "tick_frequency": 1,
                "include_tip": False,
        },
        y_axis_config={
                "unit_size": 1,
                "tick_frequency": 1,
                "include_tip": False,
        })
        axes2 = Axes(
        x_min = -3,
        x_max = 3,
        y_min = -1.5,
        y_max = 1.5,
        x_labeled_nums = [-2, 2],
        center_point= 3.4*RIGHT,
        x_axis_config={
                "unit_size": 1,
                "tick_frequency": 1,
                "include_tip": False,
        },
        y_axis_config={
                "unit_size": 1,
                "tick_frequency": 1,
                "include_tip": False,
        })
        self.add(axes1, axes2)
        axes1.get_axis_labels(x_label_tex="x", y_label_tex="y")
        axes2.get_axis_labels(x_label_tex="x", y_label_tex="y")
        graph1 = axes1.get_graph(self.sin_graph, color = YELLOW)
        graph2 = axes2.get_graph(self.cos_graph, color = RED)
        self.play(ShowCreation(graph1))
        self.play(ShowCreation(graph2))
        self.wait(2)

    def sin_graph(self, x):
        return np.sin(x)

    def cos_graph(self, x):
        return np.cos(x)
