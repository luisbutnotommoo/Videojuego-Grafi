from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def romboColision(PosObj2_X,PosObj2_Y,PosObj2_Z,Obj2_width,Obj2_height,Obj2_depth,PosXobj1,PosYobj1,PosZobj1,Obj1_height):
    obj2_rombo = ((PosObj2_X-Obj2_width/2,PosObj2_Y,PosObj2_Z),
                  (PosObj2_X,PosObj2_Y,PosObj2_Z-Obj2_depth/2),
                  (PosObj2_X-Obj2_width/2,PosObj2_Y,PosObj2_Z),
                  (PosObj2_X,PosObj2_Y+Obj2_height,PosObj2_Z))
    
    obj1_rombo = ((PosXobj1-0.5,PosYobj1,PosZobj1),
                  (PosXobj1,PosYobj1,PosZobj1-0.5),
                  (PosXobj1+0.5,PosYobj1,PosZobj1),
                  (PosXobj1,PosYobj1+Obj1_height,PosZobj1))
    
    for p1 in obj2_rombo:
        for p2 in obj1_rombo:
            if abs(p1[0]-p2[0]+abs(p1[1]-p2[2])) <= 1.0:
                return True
    return False

def dibujar_rombo(PosObj_X, PosObj_Y, PosObj_Z, width, height, depth):
    glColor3f(1.0, 0.0, 0.0) 

    vertices = [
        (PosObj_X - width / 2, PosObj_Y, PosObj_Z - depth / 2),    # Vértice inferior izquierdo
        (PosObj_X + width / 2, PosObj_Y, PosObj_Z - depth / 2),    # Vértice inferior derecho
        (PosObj_X + width / 2, PosObj_Y, PosObj_Z + depth / 2),    # Vértice superior derecho
        (PosObj_X - width / 2, PosObj_Y, PosObj_Z + depth / 2),    # Vértice superior izquierdo
        (PosObj_X, PosObj_Y + height, PosObj_Z)                   # Punto superior central
    ]

    glBegin(GL_LINE_LOOP) 
    for vertex in vertices[:4]:
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

    glBegin(GL_LINES)
    for vertex in vertices[:4]:
        glVertex3f(vertex[0], vertex[1], vertex[2])
        glVertex3f(vertices[4][0], vertices[4][1], vertices[4][2])
    glEnd()

def romboColision2(x1, y1, z1, width1, height1, depth1, x2, y2, z2, width2, height2, depth2):
    x1_min = x1 - width1 / 2
    x1_max = x1 + width1 / 2
    y1_min = y1 - height1 / 2
    y1_max = y1 + height1 / 2
    z1_min = z1 - depth1 / 2
    z1_max = z1 + depth1 / 2
    
    x2_min = x2 - width2 / 2
    x2_max = x2 + width2 / 2
    y2_min = y2 - height2 / 2
    y2_max = y2 + height2 / 2
    z2_min = z2 - depth2 / 2
    z2_max = z2 + depth2 / 2
    
    colision_x = (x1_min <= x2_max and x1_max >= x2_min)
    colision_y = (y1_min <= y2_max and y1_max >= y2_min)
    colision_z = (z1_min <= z2_max and z1_max >= z2_min)
    
    return colision_x and colision_y and colision_z


def spheres(center1, radius1, center2, radius2):
    distance = math.sqrt((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2 + (center1[2] - center2[2])**2)
    return distance < (radius1 + radius2)

def aabb(box1_min, box1_max, box2_min, box2_max):
    return (box1_min[0] <= box2_max[0] and box1_max[0] >= box2_min[0] and
            box1_min[1] <= box2_max[1] and box1_max[1] >= box2_min[1] and
            box1_min[2] <= box2_max[2] and box1_max[2] >= box2_min[2])

def manhattan(p1, p2, collision_distance):
    distance = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2])
    return distance <= collision_distance