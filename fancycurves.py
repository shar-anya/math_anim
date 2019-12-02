from manimlib.imports import *
import numpy as np

class FancyCurve(Scene):
    def construct(self):
        a = 1
        b = -2
        curve = ParametricFunction(
                    lambda t: np.array([
                    (a+b)*np.cos(TAU*t) + b*np.cos(TAU*(a + b)/b*t),
                    (a + b)*np.sin(TAU*t) + b*np.sin(TAU*(a + b)/b*t),
                    0,
                    ]),
                    color = BLUE_C,
                    stroke_width = 2,
                )
        curve1 = ParametricFunction(
                    lambda t: np.array([
                    ((a+b)*np.cos(-TAU*t) + b*np.cos(-TAU*(a + b)/b*t)),
                    ((a + b)*np.sin(-TAU*t) + b*np.sin(-TAU*(a + b)/b*t)),
                    0,
                    ]),
                    color = BLUE_C,
                    stroke_width = 2,
                )
        self.play(ShowCreation(curve))
        self.play(ShowCreation(curve1))
        self.wait(2)

class ParametricSurfaces(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # create a threeD axis
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        mobius = ParametricSurface(
            lambda t: np.array([
                (1 + np.cos(0.5*TAU*t))*np.cos(TAU*t),
                (1 + np.cos(0.5*TAU*t))*np.sin(TAU*t),
                np.sin(0.5*TAU*t),
            ]),t_max=TAU).scale(2)
        self.set_camera_orientation(phi=80 * DEGREES)

        self.play(ShowCreation(mobius))
        # self.play(ShowCreation(paraboloid))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(2)
