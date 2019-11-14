# Animation clip showing how a vector space can be formed from a basis
# FILEID: H1
from manimlib.imports import *

# EXAMPLE_TRANFORM = [[0, 1], [-1, 1]]
VECTORS = [[1, 2],
           [-4, 2],
           [-3, -3]]

class Scene1(LinearTransformationScene):
    '''
    Show Vectors with Labels in Untransformed R^2
    '''
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "show_coordinates": False,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 3,
    }
    def construct(self):
        self.setup()
        ihat, jhat = self.get_basis_vectors()
        labels = self.get_basis_vector_labels()
        self.add(ihat, jhat)
        self.add(*labels)
        self.write_stuff()
        self.show_vector_as_basis_sum()
        self.wait(2)

    def show_vector_as_basis_sum(self):
        for i in range(len(VECTORS)):
            v = self.add_vector(VECTORS[i], stroke_width = 4)
            linei = Line(start = ORIGIN, end = VECTORS[i][0]*RIGHT)
            linei.set_color(GREEN_C)
            linej = Line(start = linei.get_end(),
                         end = linei.get_end() + VECTORS[i][1]*UP)
            linej.set_color(RED_C)
            self.play(ShowCreation(linei))
            self.play(ShowCreation(linej))
            vlabel = self.get_vector_label(v, str(VECTORS[i][0]) +
                                           r"\imath" + "+" +
                                           str(VECTORS[i][1]) +
                                           r"\jmath", at_tip = True)
            self.play(ShowCreation(vlabel))
            bunch = VGroup(v, linei, linej, vlabel)
            self.play(FadeOut(bunch))
            self.wait(0.3)

    def write_stuff(self):
        self.text = []
        text = self.text

        text.append(TexMobject(r"\text{Consider the Vector Space }",
                               r"{\mathbb{R}^2}")) #0
        self.add_title(text[0], 0.7, animate = True)
        text.append(TexMobject(r"{\mathbb{R}^2}",
                               tex_to_color_map = {r"{\mathbb{R}^2}": BLUE_E}))
        text[1].shift(6.5*LEFT+3.5*UP)
        self.wait(0.5)
        self.play(Transform(text[0], text[1]))
        text.append(TexMobject(r"\text{Consider arbitrary vectors in }",
                               r"{\mathbb{R}^2}").scale(0.7)) #2
        text[2].to_edge(UP)
        text[2].add_background_rectangle()
        self.play(Write(text[2]))
        self.wait(1)

class Scene2(LinearTransformationScene):
    CONFIG = {
        "num_vectors" : 16,
        "start_color" : PINK,
        "end_color" : BLUE_E,
    }

    def get_vectors(self):
        return [
            Vector([x, y], stroke_width = 3.5)
            for x in np.arange(-int(FRAME_X_RADIUS), int(FRAME_X_RADIUS)+0.5, 0.5)
            for y in np.arange(-int(FRAME_Y_RADIUS), int(FRAME_Y_RADIUS)+0.5, 0.5)
        ]

    def lock_in_faded_grid(self, dimness=0.7, axes_dimness=0.5):
        plane = self.add_plane()
        axes = plane.get_axes()
        plane.fade(dimness)
        axes.set_color(WHITE)
        axes.fade(axes_dimness)
        self.add(axes)

    def construct(self):
        self.lock_in_faded_grid()

        vectors = self.get_vectors()
        colors = Color(self.start_color).range_to(
            self.end_color, len(vectors)
        )
        for vect, color in zip(vectors, colors):
            vect.set_color(color)

        vector_group = VGroup(*vectors)
        self.play(
            ShowCreation(
                vector_group,
                run_time = 3
            )
        )

        self.wait(1)

        vectors.sort(key=lambda v: v.get_length())
        def v_to_dot(vector):
            return Dot(vector.get_end(), fill_color = vector.get_stroke_color())
        self.wait()
        rate_functions = [
            squish_rate_func(smooth, float(x)/(len(vectors)+2), 1)
            for x in range(len(vectors))
        ]
        self.play(*[
            Transform(v, v_to_dot(v), rate_func = rf, run_time = 3)
            for v, rf in zip(vectors, rate_functions)
        ])
        self.wait(2)
        self.play_final_animation(vectors, rate_functions)
        self.wait(2)

        text = [TexMobject(r"\text{Clearly, all vectors in }", r"{\mathbb{R}^2}"),
                TexMobject(r"\text{are a }", r"\text{linear }", r"\text{combination }" , r"\text{of the basis vectors}" )]
        text[1].set_color_by_tex_to_color_map({"{linear }": RED, "{combination }": GREEN})
        textgp = VGroup(*text)
        textgp.scale(0.8)
        textgp.add_background_rectangle()
        textgp.to_edge(UP)
        text[1].shift(0.7*DOWN)

        self.play(ShowCreation(text[0]))
        self.play(ShowCreation(text[1]))
        self.play(ShowCreation(self.get_basis_vectors()))
        self.wait(3)

    def play_final_animation(self, vectors, rate_functions):

        h_line = Line(
            FRAME_X_RADIUS*RIGHT, FRAME_X_RADIUS*LEFT,
            stroke_width = 0.5,
            color = BLUE_E
        )
        v_line = Line(
            FRAME_Y_RADIUS*UP, FRAME_Y_RADIUS*DOWN,
            stroke_width = 0.5,
            color = BLUE_E
        )
        line_pairs = [
            VGroup(h_line.copy().shift(y), v_line.copy().shift(x))
            for v in vectors
            for x, y, z in [v.get_center()]
        ]
        plane = NumberPlane()
        self.play(
            ShowCreation(plane),
            *[
                Transform(v, p, rate_func = rf)
                for v, p, rf in zip(vectors, line_pairs, rate_functions)
            ]
        )
        self.remove(*vectors)

class Scene3(LinearTransformationScene, MovingCameraScene):
    '''
    Illustrates basis vectors for transformed R^2
    '''

    def construct(self):
        self.setup()
        self.linear_transform = [[2,1], [1,2]]
        self.write_stuff()
        self.apply_matrix(self.linear_transform)
        self.wait(1)
        self.play(FadeOut(VGroup(*self.text[0:2])))

        self.play(ApplyMethod(self.camera_frame.scale , 2.5))
        self.show_vector_as_basis_sum()
        self.play(ApplyMethod(self.camera_frame.scale , 0.4))
        self.play(Write(self.text[2]))
        self.wait(2)
        self.play(FadeOut(self.text[2]))


    def setup(self):
        LinearTransformationScene.setup(self)
        MovingCameraScene.setup(self)

    def write_stuff(self):
        self.text = []
        text = self.text
        text.append(TextMobject("Consider the linear transformation"))
        text.append(Matrix(self.linear_transform))
        text.append(TextMobject("Coordinates of vectors in terms of new basis remain the same").add_background_rectangle())

        text[0].add_background_rectangle()
        text[1].add_background_rectangle()
        text01 = VGroup(*text[0:2])
        text01.scale(0.8)
        text[1].next_to(text[0],RIGHT)
        text01.to_edge(UP)
        text01.shift(LEFT)

        text[2].to_edge(UP)
        text[2].scale(0.8)
        self.play(Write(text01))
        self.wait(1)

    def show_vector_as_basis_sum(self):
        for i in range(len(VECTORS)):
            v1 = Vector(VECTORS[i])
            v2 = Vector(
                np.dot(np.array(self.linear_transform).transpose(), VECTORS[i]),
                color = YELLOW,
                stroke_width = 4,
            )
            self.add_vector(v2)
            self.wait(0.5)
            # v = self.add_vector(VECTORS[i], stroke_width = 4)
            linei = Line(start = ORIGIN, end = (self.linear_transform[0][0]*RIGHT + self.linear_transform[0][1]*UP)*VECTORS[i][0], stroke_width = 4)
            linei.set_color(GREEN)
            linej = Line(start = ORIGIN, end = (self.linear_transform[1][0]*RIGHT + self.linear_transform[1][1]*UP)*VECTORS[i][1], stroke_width = 4)
            linej.shift(linei.get_end())
            linej.set_color(RED_C)
            self.play(ShowCreation(linei))
            self.play(ShowCreation(linej))
            vlabel = self.get_vector_label(v2, str(VECTORS[i][0]) +
                                           r"\imath_1" + "+" +
                                           str(VECTORS[i][1]) +
                                           r"\jmath_1", at_tip = True)
            vlabel.scale(1.5)
            self.play(ShowCreation(vlabel))
            self.wait(1.5)
            bunch = VGroup(v2, linei, linej, vlabel)
            self.play(FadeOut(bunch))
            self.wait(0.3)

class TransformManyVectors(LinearTransformationScene, MovingCameraScene):
    CONFIG = {
        "transposed_matrix" : [[2, 1], [1, 2]],
        "use_dots" : True,
        "include_background_plane": False,
    }
    def setup(self):
        LinearTransformationScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.setup()
        self.wait(1.5)
        vectors = VGroup(*[
            Vector([x, y], stroke_width = 3)
            for x in np.arange(-int(FRAME_X_RADIUS), int(FRAME_X_RADIUS)+0.5)
            for y in np.arange(-int(FRAME_Y_RADIUS), int(FRAME_Y_RADIUS)+0.5)
        ])
        vectors.set_submobject_colors_by_gradient(BLUE_C, MAROON_E)
        self.play(ShowCreation(vectors, lag_ratio = 0.5))
        self.wait(0.5)
        self.apply_matrix(self.transposed_matrix)

        t_matrix = self.transposed_matrix
        transformed_vectors = VGroup(*[
            Vector(
                np.dot(np.array(t_matrix).transpose(), v.get_end()[:2]),
                color = v.get_color(), stroke_width = 3
            )
            for v in vectors.split()
        ])
        self.wait()
        self.play(Transform(
        vectors, transformed_vectors,
        run_time = 3,
        path_arc = -np.pi/2
        ))
        if self.use_dots:
            self.play(Transform(
                vectors, self.vectors_to_dots(vectors),
                run_time = 3,
                lag_ratio = 0.5
            ))
            transformed_vectors = self.vectors_to_dots(transformed_vectors)
            self.wait()
        self.wait(3)


    def vectors_to_dots(self, vectors):
        return VGroup(*[
            Dot(v.get_end(), color = v.get_color())
            for v in vectors.split()
        ])
