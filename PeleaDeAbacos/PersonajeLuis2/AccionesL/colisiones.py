def rombo_collision(PosObj2_X, PosObj2_Y, PosObj2_Z,Obj2_width, Obj2_height,Obj2_depth,
    PosXob1, PosYob1, PosZob1,Obj1_height):

    obj2_rombo=((PosObj2_X-Obj2_width/2, PosObj2_Y, PosObj2_Z),
    (PosObj2_X, PosObj2_Y, PosObj2_Z-Obj2_depth/2),
    (PosObj2_X+Obj2_width/2, PosObj2_Y, PosObj2_Z),
    (PosObj2_X, PosObj2_Y+Obj2_height/2, PosObj2_Z)) #x, y, x

    obj1_rombo=((PosXob1-0.5, PosYob1, PosZob1),
                (PosXob1, PosYob1, PosZob1-0.5),
                (PosXob1+0.5, PosYob1, PosZob1),
                (PosXob1, PosYob1+Obj1_height, PosZob1))
    
    for p1 in obj2_rombo:
        for p2 in obj1_rombo:
            if abs(p1[0]-p2[0]+abs(p1[1]-p2[1]))<=1.0:
                return True
    return False

