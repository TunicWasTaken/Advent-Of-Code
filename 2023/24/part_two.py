import collections
import time

time_start = time.time()

VecXYZ = collections.namedtuple("VecXYZ", "x,y,z", defaults=(0, 0, 0))


def cross(a, b):
    return VecXYZ(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)


def indep(a, b):
    return any(val != 0 for val in cross(a, b))


def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


def sub(a, b):
    return VecXYZ(a.x - b.x, a.y - b.y, a.z - b.z)


def lin(r, a, s, b, t, c):
    x = r * a.x + s * b.x + t * c.x
    y = r * a.y + s * b.y + t * c.y
    z = r * a.z + s * b.z + t * c.z

    return VecXYZ(x, y, z)


def find_plane(pt1, vec1, pt2, vec2):

    pt12 = sub(pt1, pt2)
    vec12 = sub(vec1, vec2)
    vv = cross(vec1, vec2)
    
    return (cross(pt12, vec12), dot(pt12, vv))


def find_rock(pt1, vec1, pt2, vec2, pt3, vec3):

    a, A = find_plane(pt1, vec1, pt2, vec2)
    b, B = find_plane(pt1, vec1, pt3, vec3)
    c, C = find_plane(pt2, vec2, pt3, vec3)

    w = lin(A, cross(b, c), B, cross(c, a), C, cross(a, b))
    t = dot(a, cross(b, c))

    w = VecXYZ(round(w.x / t), round(w.y / t), round(w.z / t))

    w1 = sub(vec1, w)
    w2 = sub(vec2, w)
    ww = cross(w1, w2)

    E = dot(ww, cross(pt2, w2))
    F = dot(ww, cross(pt1, w1))
    G = dot(pt1, ww)
    S = dot(ww, ww)

    rock = lin(E, w1, -F, w2, G, ww)
    return (rock, S)

def parse_input():

    lines = [line.strip() for line in open("input.txt")]
    pts = []
    vecs = []

    for line in lines:
        pos, vec = line.split(" @ ")
        pts.append(VecXYZ(*map(int, pos.split(","))))
        vecs.append(VecXYZ(*map(int, vec.split(","))))

    return (pts, vecs)


def solve(pts, vecs):

    pt1, vec1 = pts[0], vecs[0]
    
    for i in range(1, len(pts)):
        if indep(vec1, vecs[i]):
            pt2, vec2 = pts[i], vecs[i]
            break
    
    for j in range(i + 1, len(pts)):
        if indep(vec1, vecs[j]) and indep(vec2, vecs[j]):
            pt3, vec3 = pts[j], vecs[j]
            break

    rock, S = find_rock(pt1, vec1, pt2, vec2, pt3, vec3)
    return sum(rock) / S



def main():

    return solve(*parse_input())

result = int(main())
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")