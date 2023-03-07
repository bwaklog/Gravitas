import numpy as np


class celestial(object):

    def __init__(self, cateogry, name, mass, radius):
        self.cat = cateogry
        self.name - name
        self.mass = mass
        self.radius = radius

    def cDensity(self):
        mass, radius = self.mass, self.radius
        return (3*mass)/(4 * np.pi * (radius**3))

    def NGF(self, cSep, cObj: __name__.celestial):
        ngc = 6.67430E-11
        m1, r1 = self.mass, self.radius
        m2, r2 = cObj.mass, cObj.radius

        ngf = (ngc * m1 * m2) / (cSep + r1 + r2) ** 2

        vOrb = np.sqrt((ngc * m2) / cSep)

        return {
            ngf: ngf,
            vOrb: vOrb
        }
