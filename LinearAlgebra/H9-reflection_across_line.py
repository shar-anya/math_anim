# Animation clip illustrating reflection of a vector v across line
# FILEID: H9
from manimlib.imports import *

class Reflection(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "show_coordinates": False,
        "show_basis_vectors": False,
        "foreground_plane_kwargs": {
            "background_line_style": {
                "stroke_color": DARK_BLUE,
                                    },
            "axis_config": {
                "stroke_color": GREY_BROWN,
            }
                                }
        }
    def construct(self):
        line = Line(start = FRAME_X_RADIUS*(LEFT+ 0.5*UP), end = FRAME_X_RADIUS*(RIGHT+ 0.5*DOWN), stroke_width = 5, color = WHITE)
        self.play(FadeIn(line))

        vector_coords = [-2,2]
        line_slope = [2, -1]
        I = np.array([[1,0],[0,1]])
        v = np.array([[-1*line_slope[1]],[line_slope[0]]])
        vt = np.transpose(v)
        norm_v = np.power(v[0],2) + np.power(v[1],2)
        calculated = I - (2*np.matmul(v,vt)/norm_v)
        reflected = np.matmul(calculated,np.array([[vector_coords[0]],[vector_coords[1]]]))

        colors = [TEAL_D, MAROON_D]
        vec = [
                Vector(vector_coords, color = colors[0], stroke_width = 4),
                Vector(reflected, color = colors[1], stroke_width = 4)
            ]

        arc =[
            Arc(
                start_angle=line.get_angle(),
                angle= vec[0].get_angle()-line.get_angle(),
                radius=0.4,
                arc_center=ORIGIN,
                stroke_width=3,
                stroke_color=colors[0],
                stroke_opacity=0.5,
            ),
            Arc(
                start_angle=line.get_angle(),
                angle= (vec[1].get_angle()-line.get_angle()),
                radius=0.4,
                arc_center=ORIGIN,
                stroke_width=3,
                stroke_color=colors[1],
                stroke_opacity=0.5,
            )]
        arclabel = [((TexMobject(r"{\theta}").scale(0.7)).set_color(colors[i])).next_to(arc[i], RIGHT, SMALL_BUFF) for i in range(2)]

        self.play(ShowCreation(vec[0]))
        self.play(ShowCreation(arc[0]))
        self.play(ShowCreation(arclabel[0]))
        self.play(ShowCreation(arc[1]))
        self.play(ShowCreation(arclabel[1]))
        self.play(ShowCreation(vec[1]))
        self.wait(2)
