# Drawing square function of Fourier Transform
from manimlib.imports import *
import numpy as np

class PlotFunction(Scene):
    def construct(self):
        axes = Axes(animate = True)
        sine = axes.get_graph(self.some)
        self.add(sine)

    def some(self, x):
        return 4/np.pi*(np.cos(np.pi*x) - np.cos(3*np.pi*x)/3 + np.cos(5*np.pi*x)/5 - np.cos(7*np.pi*x)/7+ np.cos(9*np.pi*x)/9 - np.cos(11*np.pi*x)/11)
