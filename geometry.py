from vector import *


class Light:
    def __init__(self, pos=Vector3(-1000, 0, 1000), i=255):
        self.position = pos
        self.I = i

class HitRecord:
    def __init__(self, kakskdp, nvl, i):
        # for shading coefficients
        self.Ka, self.Ks, self.Kd, self.p = kakskdp

        # for vectors
        self.n, self.v, self.l = nvl

        # for light intense
        self.I = i


class Surface:

    def hit(self, ray, light, t0, t1):
        pass

class Ground(Surface):
    def __init__(self):
        self.earth = Vector3(0, 0, 0)
        self.n = Vector3(0, 0, 1)

    def hit(self, ray, light, t0, t1):

        is_hit = False





class Sphere(Surface):
    def __init__(self, center=Vector3(0, 800, 0), radius=100, kakskdp=(0.4, 0.5, 0.3, 20)):
        #  shape of sphere
        self.center = center
        self.radius = radius

        # variables for shading
        self.Ka, self.Ks, self.Kd, self.p = kakskdp

    def hit(self, ray, light, t0, t1):
        def in_scope(t):
            if t0 < t < t1:
                return True
            else:
                return False

        is_hit = False

        e_minus_c = ray.origin.minus(self.center)
        dd = ray.direction.dot(ray.direction)
        d_e_c =ray.direction.dot(e_minus_c)

        delta = d_e_c**2 \
                - dd * (e_minus_c.dot(e_minus_c) - self.radius**2)

        if delta < 0:
            return is_hit, 0, 0
        else:
            t_a = (-1 * d_e_c + sqrt(delta)) / dd
            t_b = (-1 * d_e_c - sqrt(delta)) / dd

        if in_scope(t_b):
            t = t_b
        elif in_scope(t_a):
            t = t_a
        else:
            return is_hit, 0, 0

        p = ray.origin.plus(ray.direction.s_multip(t))

        v = ray.origin.minus(p)
        v.normalize()
        n = p.minus(self.center)
        n.normalize()
        l = light.position.minus(p)
        l.normalize()

        is_hit = True

        rec = HitRecord((self.Ka, self.Ks, self.Kd, self.p), (n, v, l), light.I)
        return is_hit, t, rec



# class Triangle(Surface):
#     def __init__(self):
#         # shape of triangle
#         self.point_a =
#         self.point_b =
#         self.point_c =
#
#
#     def hit(self,ray,light,t0,t1):

