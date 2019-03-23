"""

Python solution to this Rosetta Code task:

http://rosettacode.org/wiki/Catmull%E2%80%93Clark_subdivision_surface

Input and output are assumed to be in this form based on the talk
page for the task:

input_points = [
  [-1.0,  1.0,  1.0],
  [-1.0, -1.0,  1.0],
  [ 1.0, -1.0,  1.0],
  [ 1.0,  1.0,  1.0],
  [ 1.0, -1.0, -1.0],
  [ 1.0,  1.0, -1.0],
  [-1.0, -1.0, -1.0],
  [-1.0,  1.0, -1.0]
]

input_faces = [
  [0, 1, 2, 3],
  [3, 2, 4, 5],
  [5, 4, 6, 7],
  [7, 0, 3, 5],
  [7, 6, 1, 0],
  [6, 1, 2, 4],
]

So, the graph is a list of points and a list of faces.
Each face is a list of indexes into the points list.

next part of the algorithm on the RC page is

3.

for each vertex point, its coordinates are updated from (new_coords):

    the old coordinates (old_coords),
     
    the average of the face points of the faces the point belongs to (avg_face_points),

    the average of the centers of edges the point belongs to (avg_mid_edges),

    how many faces a point belongs to (n), then use this formula:
    
         m1 = (n - 3) / n
         m2 = 1 / n
         m3 = 2 / n
         new_coords = (m1 * old_coords)
                    + (m2 * avg_face_points)
                    + (m3 * avg_mid_edges)

"""

def center_point(p1, p2):
    """ 
    returns a point in the center of the 
    segment ended by points p1 and p2
    """
    cp = []
    for i in range(3):
        cp.append((p1[i]+p2[i])/2)
        
    return cp
    
def sum_point(p1, p2):
    """ 
    adds points p1 and p2
    """
    sp = []
    for i in range(3):
        sp.append(p1[i]+p2[i])
        
    return sp

def div_point(p, d):
    """ 
    divide point p by d
    """
    sp = []
    for i in range(3):
        sp.append(p[i]/d)
        
    return sp

def get_face_points(input_points, input_faces):
    """
    From http://rosettacode.org/wiki/Catmull%E2%80%93Clark_subdivision_surface
    
    1. for each face, a face point is created which is the average of all the points of the face.
    """

    # 3 dimensional space
    
    NUM_DIMENSIONS = 3
    
    # face_points will have one point for each face
    
    face_points = []
    
    for curr_face in input_faces:
        face_point = [0.0, 0.0, 0.0]
        for curr_point_index in curr_face:
            curr_point = input_points[curr_point_index]
            # add curr_point to face_point
            # will divide later
            for i in range(NUM_DIMENSIONS):
                face_point[i] += curr_point[i]
        # divide by number of points for average
        num_points = len(curr_face)
        for i in range(NUM_DIMENSIONS):
            face_point[i] /= num_points
        face_points.append(face_point)
        
    return face_points
    
def get_edges_faces(input_points, input_faces):
    """
    
    Get list of edges and the one or two adjacent faces in a list.
    also get center point of edge
    
    Each edge would be [pointnum_1, pointnum_2, facenum_1, facenum_2, center]
    
    """
    
    # will have [pointnum_1, pointnum_2, facenum]
    
    edges = []
    
    # get edges from each face
    
    for facenum in range(len(input_faces)):
        face = input_faces[facenum]
        num_points = len(face)
        # loop over index into face
        for pointindex in range(num_points):
            # if not last point then edge is curr point and next point
            if pointindex < num_points - 1:
                pointnum_1 = face[pointindex]
                pointnum_2 = face[pointindex+1]
            else:
                # for last point edge is curr point and first point
                pointnum_1 = face[pointindex]
                pointnum_2 = face[0]
            # order points in edge by lowest point number
            if pointnum_1 > pointnum_2:
                temp = pointnum_1
                pointnum_1 = pointnum_2
                pointnum_2 = temp
            edges.append([pointnum_1, pointnum_2, facenum])
            
    # sort edges by pointnum_1, pointnum_2, facenum
    
    edges = sorted(edges)
    
    # merge edges with 2 adjacent faces
    # [pointnum_1, pointnum_2, facenum_1, facenum_2] or
    # [pointnum_1, pointnum_2, facenum_1, None]
    
    num_edges = len(edges)
    eindex = 0
    merged_edges = []
    
    while eindex < num_edges:
        e1 = edges[eindex]
        # check if not last edge
        if eindex < num_edges - 1:
            e2 = edges[eindex+1]
            if e1[0] == e2[0] and e1[1] == e2[1]:
                merged_edges.append([e1[0],e1[1],e1[2],e2[2]])
                eindex += 2
            else:
                merged_edges.append([e1[0],e1[1],e1[2],None])
                eindex += 1
        else:
            merged_edges.append([e1[0],e1[1],e1[2],None])
            eindex += 1
            
    # add edge centers
    
    edges_centers = []
    
    for me in merged_edges:
        p1 = input_points[me[0]]
        p2 = input_points[me[1]]
        cp = center_point(p1, p2)
        edges_centers.append(me+[cp])
            
    return edges_centers
       
def get_edge_points(input_points, edges_faces):
    """
    for each edge, an edge point is created which is the average 
    between the center of the edge and the center of the segment made
    with the face points of the two adjacent faces.
    """
    
    edge_points = []
    
    for edge in edges_faces:
        # get center of edge
        cp = edge[4]
        # get center of two facepoints
        fp1 = face_points[edge[2]]
        # if not two faces just use one facepoint
        # should not happen for solid like a cube
        if edge[3] == None:
            fp2 = fp1
        else:
            fp2 = face_points[edge[3]]
        cfp = center_point(fp1, fp2)
        # get average between center of edge and
        # center of facepoints
        edge_point = center_point(cp, cfp)
        edge_points.append(edge_point)      
        
    return edge_points
    
def get_avg_face_points(input_points, input_faces, face_points):
    """
    
    for each point calculate
    
    the average of the face points of the faces the point belongs to (avg_face_points)
    
    create a list of lists of two numbers [facepoint_sum, num_points] by going through the
    points in all the faces.
    
    then create the avg_face_points list of point by dividing point_sum (x, y, z) by num_points
    
    """
    
    # initialize list with [[0.0, 0.0, 0.0], 0]
    
    num_points = len(input_points)
    
    temp_points = []
    
    for pointnum in range(num_points):
        temp_points.append([[0.0, 0.0, 0.0], 0])
        
    # loop through faces updating temp_points
    
    for facenum in range(len(input_faces)):
        fp = face_points[facenum]
        for pointnum in input_faces[facenum]:
            tp = temp_points[pointnum][0]
            temp_points[pointnum][0] = sum_point(tp,fp)
            temp_points[pointnum][1] += 1
            
    # divide to create avg_face_points
    
    avg_face_points = []
    
    for tp in temp_points:
       afp = div_point(tp[0], tp[1])
       avg_face_points.append(afp)
       
    return avg_face_points
    
def get_avg_mid_edges(input_points, edges_faces):
    """
    
    the average of the centers of edges the point belongs to (avg_mid_edges)
    
    create list with entry for each point 
    each entry has two elements. one is a point that is the sum of the centers of the edges
    and the other is the number of edges. after going through all edges divide by
    number of edges.
    
    """
    
    # initialize list with [[0.0, 0.0, 0.0], 0]
    
    num_points = len(input_points)
    
    temp_points = []
    
    for pointnum in range(num_points):
        temp_points.append([[0.0, 0.0, 0.0], 0])
        
    # go through edges_faces using center updating each point
    
    for edge in edges_faces:
        cp = edge[4]
        for pointnum in [edge[0], edge[1]]:
            tp = temp_points[pointnum][0]
            temp_points[pointnum][0] = sum_point(tp,cp)
            temp_points[pointnum][1] += 1
    
    # divide out number of points to get average
    
    avg_mid_edges = []
        
    for tp in temp_points:
       ame = div_point(tp[0], tp[1])
       avg_mid_edges.append(ame)
       
    return avg_mid_edges

def get_points_faces(input_points, input_faces):
    # initialize list with 0
    
    num_points = len(input_points)
    
    points_faces = []
    
    for pointnum in range(num_points):
        points_faces.append(0)
        
    # loop through faces updating points_faces
    
    for facenum in range(len(input_faces)):
        for pointnum in input_faces[facenum]:
            points_faces[pointnum] += 1
            
    return points_faces
    
# square
"""
input_points = [
  [0.0, 0.0,  0.0],
  [1.0, 0.0,  0.0],
  [1.0, 1.0,  0.0],
  [0.0, 1.0,  0.0]
]

input_faces = [
  [0, 1, 2, 3]
]
"""
# cube

input_points = [
  [-1.0,  1.0,  1.0],
  [-1.0, -1.0,  1.0],
  [ 1.0, -1.0,  1.0],
  [ 1.0,  1.0,  1.0],
  [ 1.0, -1.0, -1.0],
  [ 1.0,  1.0, -1.0],
  [-1.0, -1.0, -1.0],
  [-1.0,  1.0, -1.0]
]

input_faces = [
  [0, 1, 2, 3],
  [3, 2, 4, 5],
  [5, 4, 6, 7],
  [7, 0, 3, 5],
  [7, 6, 1, 0],
  [6, 1, 2, 4],
]

# 1. for each face, a face point is created which is the average of all the points of the face.
# each entry in the returned list is a point (x, y, z).

face_points = get_face_points(input_points, input_faces)

# get list of edges with 1 or 2 adjacent faces
# [pointnum_1, pointnum_2, facenum_1, facenum_2, center] or
# [pointnum_1, pointnum_2, facenum_1, None, center]

edges_faces = get_edges_faces(input_points, input_faces)

# get edge points, a list of points

edge_points = get_edge_points(input_points, edges_faces)
                
# the average of the face points of the faces the point belongs to (avg_face_points)                
                
avg_face_points = get_avg_face_points(input_points, input_faces, face_points)
   
# the average of the centers of edges the point belongs to (avg_mid_edges)
   
avg_mid_edges = get_avg_mid_edges(input_points, edges_faces) 
   
# how many faces a point belongs to

points_faces = get_points_faces(input_points, input_faces)

for p in points_faces:
    print(p)