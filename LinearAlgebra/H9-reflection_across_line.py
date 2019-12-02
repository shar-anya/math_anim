# Animation clip illustrating reflection of a vector v across line[k]
# FILEID: H9
from manimlib.imports import *

class ReflectionY(LinearTransformationScene):
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
        line =  [Line(start = FRAME_X_RADIUS*(LEFT),
                end = FRAME_X_RADIUS*(RIGHT),
                stroke_width = 5, color = BLUE_B),
                Line(start = FRAME_Y_RADIUS*(UP),
                end = FRAME_Y_RADIUS*(DOWN),
                stroke_width = 5, color = BLUE_C),
                ]
                # Line(start = FRAME_X_RADIUS*(LEFT+ 0.5*UP),
                # end = FRAME_X_RADIUS*(RIGHT+ 0.5*DOWN),
                # stroke_width = 5, color = BLUE_A),
        vector_coords = [[3,1],
                         [1.5,3],
                         [0,4],
                         [-2,4],
                         [-4,0]]
        line_slopes = [[1,0],[0,1]] #,[2, -1
        colors = [TEAL_D, MAROON_D]

        for k in range(1,2):
            I = np.array([[1,0],[0,1]])
            v = np.array([[-1*line_slopes[k][1]],[line_slopes[k][0]]])
            vt = np.transpose(v)
            norm_v = np.power(v[0],2) + np.power(v[1],2)
            calculated = I - (2*np.matmul(v,vt)/norm_v)
            self.play(FadeIn(line[k]))
            self.wait(0.5)
            # line_slope = line_slopes[i]
            for i in range(len(vector_coords)):
                reflected = np.matmul(calculated,np.array([[vector_coords[i][0]],[vector_coords[i][1]]]))
                vec = [
                        Vector(vector_coords[i], color = colors[0], stroke_width = 4),
                        Vector(reflected, color = colors[1], stroke_width = 4)
                    ]

                arc = [Arc(
                            start_angle=line[k].get_angle(),
                            angle= vec[j].get_angle()-line[k].get_angle(),
                            radius=0.4,
                            arc_center=ORIGIN,
                            stroke_width=3,
                            stroke_color=colors[j],
                            stroke_opacity=0.8,
                        )
                    for j in range(2)]
                # if i is (len(vector_coords)-1):
                if k is (1):
                    arc[1] = Arc(
                            start_angle=line[k].get_angle(),
                            # angle= -(vec[1].get_angle()-line[1].get_angle()),
                            angle= -vec[0].get_angle()-np.pi/2,
                            radius=0.4,
                            arc_center=ORIGIN,
                            stroke_width=3,
                            stroke_color=colors[1],
                            stroke_opacity=0.8,
                        )
                direction = [RIGHT,LEFT]
                arclabel = [((TexMobject(r"{\theta}").scale(0.7)).set_color(colors[i])).next_to(arc[i], direction[i], 1.4*SMALL_BUFF) for i in range(2)]
                # arclabel[1].shift((0.2+0.07*i)*DOWN+(0.1+0.1*i)*LEFT)
                self.play(ShowCreation(vec[0]))
                self.play(ShowCreation(arc[0]),ShowCreation(arclabel[0]))
                self.play(ShowCreation(arc[1]),ShowCreation(arclabel[1]))
                self.play(ShowCreation(vec[1]))
                self.wait(1)
                self.play(FadeOut(VGroup(*vec,*arc,*arclabel)))
            self.wait(1)
            self.play(FadeOut(line[k]))
