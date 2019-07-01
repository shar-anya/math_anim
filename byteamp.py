from manimlib.imports import *
import numpy as np

class ByteAmp1(GraphScene):
    CONFIG = {
    "x_min": -PI,
    "x_max": PI,
    "y_min": -PI/2,
    "y_max": PI/2,
    "axes_color": BLACK,
    "graph_origin": 4*LEFT,
    "x_axis_width":  4,
    "y_axis_height": 3,
    "exclude_zero_label": True,
    "x_axis_label" : "",
    "y_axis_label" : "",
    # "x_labeled_nums": [PI/4],
    # "y_labeled_nums": [0.5],
    }

    def sin_graph(self,x):
        return 0.5*np.sin(4*x)

    def construct(self):
        # DEFINITIONS
        Title = TexMobject("\\text{Byte}", "\\text{Amp}")
        Title.set_color_by_tex_to_color_map({"{Byte}": BLUE_C, "{Amp}": YELLOW_D})
        # Graph Settings
        self.x_leftmost_tick = self.x_max+1
        self.y_bottom_tick = self.y_max+1  #do not want any ticks on the axes as of now
        X_TICKS_DISTANCE = self.x_axis_width/(self.x_max- self.x_min)
        Y_TICKS_DISTANCE = self.y_axis_height/(self.y_max- self.y_min)
        # Creation of the digital signal ('._.)
        digital_signal = []
        part1 = Line(start = 2*LEFT, end = 2*LEFT+0.5*UP)
        cor = [2*LEFT, 0.5*UP]
        digital_signal.append(part1)
        for i in range(15):
            if i%2 is 0:
                digital_signal.append(Line(start = cor[0]+cor[1], end = cor[0]+cor[1]+ (PI/4*X_TICKS_DISTANCE*RIGHT)))
                cor[0] = cor[0] + (PI/4*X_TICKS_DISTANCE)*RIGHT
            else:
                if (cor[1][1] == 0.5):
                    digital_signal.append(Line(start = cor[0]+cor[1], end = cor[0]+cor[1]+1*DOWN))
                    cor[1] = 0.5*DOWN
                else:
                    digital_signal.append(Line(start = cor[0]+cor[1], end = cor[0]+cor[1]+1*UP))
                    cor[1] = 0.5*UP

        part2 = Line(start = cor[0]+cor[1], end = cor[0])
        digital_signal.append(part2)
        # [item.set_color(WH) for item in digital_signal]
        digital_group = VGroup(*digital_signal)

        # ANIMATION BEGINS HERE
        self.setup_axes()
        func_graph1 = self.get_graph(self.sin_graph, BLUE_C)
        self.play(ShowCreation(func_graph1, run_time = 2.5))
        self.play(FadeOut(func_graph1, run_time = 0.25) , ShowCreation(digital_group, run_time = 2.5))
        self.graph_origin = 4*RIGHT
        self.setup_axes()
        func_graph2 = self.get_graph(self.sin_graph, BLUE_C)
        self.play(FadeOut(digital_group, run_time = 0.25), ShowCreation(func_graph2, run_time = 2.5))
        self.play(FadeOut(func_graph2))

        Bigp = VGroup(func_graph1, digital_group, func_graph2)
        self.play(FadeIn(Bigp))

        self.play(Transform(Bigp, Title))
        self.wait(1)
        # self.add(TextMobject("siudj"))
