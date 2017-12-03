import pyglet
from pyglet.gl import gl
from pyglet.gl.glu import gluLookAt
import numpy as np

class Camera:
    def __init__(self):
        self.phi = 0.0
        self.teta = 0.0
        self.vec3Pos = (0, 0, 0)
        self.vec3Target = (0, 0, 0)
        self.vec3UpAxis = (0, 1, 0)
        self.vec3Orientation = (0, 0, 0)
        self.lateral = (0, 0, 0)

    def orienter(self, x, y):
        # Modify phi and teta with mouse coordinates
        self.phi += -y * 0.5
        self.teta += -x * 0.5

        # Limit phi and teta
        if self.phi > 89.0:
            self.phi = 89.0
        if self.teta > 89.0:
            self.teta = 89.0

        # Degree to radian conversion
        phiRadian = self.phi * np.pi / 180
        tetaRadian = self.teta * np.pi / 180

        # Orientation vector with cos and sin
        self.vec3Orientation = (
        np.cos(phiRadian) * np.sin(tetaRadian), np.sin(phiRadian), np.cos(phiRadian) * np.cos(tetaRadian))

        # Normale
        self.lateral = np.cross(self.vec3UpAxis, self.vec3Orientation)
        # self.lateral = normalize(self.vec3UpAxis,self.vec3Orientation)