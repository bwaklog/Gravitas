import os
import numpy as np
import math as mt
import json


class gravity(object):

    def __init__(self, cateogry, name, mass, radius):
        self.cat = cateogry
        self.name = name
        self.mass = mass
        self.radius = radius

    def cDensity(self):
        mass, radius = self.mass, self.radius
        return (3*mass)/(4 * np.pi * (radius**3))

    def NGFC(self, cSep, cObj, t=False):
        ngc = 6.67430E-11
        m1, r1 = self.mass, self.radius
        m2, r2 = cObj.mass, cObj.radius

        sNet = r1 + r2 + cSep

        ngf = (ngc * m1 * m2) / (cSep + r1 + r2) ** 2

        vOrb = np.sqrt((ngc * m2) / cSep)

        revT = (2 * np.pi * sNet) / (vOrb)

        res = {
            'ngf': ngf,
            'vOrb': vOrb,
            'T': revT,
            'freq': revT ** -1,
            'omega': (2 * np.pi) / revT
        }

        if t:
            print(json.dumps(res, indent=4))

        return res

    def KEPL(self):
        pass


class charge(object):
    def __init__(self, charge):
        self.ch = charge

    def intr(self, cis: list, t=False):
        q = self.ch

        fnet = sum((9E9 * q * i[0].ch)/(i[1])**2 for i in cis)

        uEng = sum((9E9 * q * i[0].ch)/i[1] for i in cis)

        # missing Potential!
        res = {
            'fNet': fnet,
            'eField': fnet/q,
            'uEng': uEng,
        }

        if t:
            print(json.dumps(res, indent=4))

        return res

    def dipole(self, qSep, point=None, t=False):

        if point is None:
            point = []
        pBar = self.ch * qSep

        # if point != []:
        #     eNet = ((9E9 * pBar)/point[0]**3) * \
        #         np.sqrt(3 * mt.cos(point[1])**2 + 1)
        # else:
        #     eNet = 0

        # print((9E9 * pBar)/point[0])

        res = {
            'pBar': pBar,
            # 'eField': eNet
        }

        if t:
            print(json.dumps(res, indent=4))

        return res


class atom(object):
    pass



# q1 = charge(2E-6)
# q2 = charge(4E-6)
# q1.intr([[q2, 2]], True)

# q2.dipole(0.001, [2E-4, 0], True)
