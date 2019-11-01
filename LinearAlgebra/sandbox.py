# Animation clip showing how a vector space can be formed from a basis
# FILEID: H1
from manimlib.imports import *

class Reconstruction(VectorScene):
    CONFIG = {
        "vector1" : [1, 2],
        "vector2" : [3, -1],
        "vector1_color" : MAROON_C,
        "vector2_color" : BLUE,
        "vector1_label" : "v",
        "vector2_label" : "w",
        "sum_color" : PINK,
        "scalar_pairs" : [
            (1.5, 0.3),
            ]
        }

    def construct(self):
        self.lock_in_faded_grid()
        
        v2 = self.add_vector(self.vector2, color = self.vector2_color, stroke_width = 3)

        self.initial_scaling(v1, v2)
        self.wait(2)

    def get_rate_func_pair(self):
        return [
            squish_rate_func(smooth, a, b)
            for a, b in [(0, 0.7), (0.3, 1)]
        ]

    def initial_scaling(self, v1, v2):
        scalar_pair = self.scalar_pairs.pop(0)
        anims = [
            ApplyMethod(v.scale, s, rate_func = rf)
            for v, s, rf in zip(
                [v1, v2],
                scalar_pair,
                self.get_rate_func_pair()
            )
        ]
        # anims += [
        #     ApplyMethod(v.copy().fade, 0.7)
        #     for v in (v1, v2)
        # ]

        self.play(*anims, **{"run_time" : 2})
        self.wait()


    def lock_in_faded_grid(self, dimness=0.7, axes_dimness=0.5):
        plane = self.add_plane()
        axes = plane.get_axes()
        plane.fade(dimness)
        axes.set_color(WHITE)
        axes.fade(axes_dimness)
        self.add(axes)
        # self.freeze_background()
