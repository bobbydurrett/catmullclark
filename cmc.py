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

for each edge, an edge point is created which is the average 
between the center of the edge and the center of the segment made
with the face points of the two adjacent faces.

My thoughts:

Using our representation of faces there are the same number of 
edges as points. A quadrilateral has 4 points and 4 edges.
The last point in the list has an edge connecting back to the
first point.

To find the two faces that are adjacent to an edge we need
to find the two faces that have the two edge points in them 
in either order.

In the example above these two faces:

  [0, 1, 2, 3]
  [3, 2, 4, 5]

are adjacent to the edge 2,3 or 3,2

"""

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
    
    Each edge would be [pointnum_1, pointnum_2, facenum_1, facenum_2]
    
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
            
    return merged_edges
        
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
# [pointnum_1, pointnum_2, facenum_1, facenum_2] or
# [pointnum_1, pointnum_2, facenum_1, None]

edges = get_edges_faces(input_points, input_faces)
            
for e in edges:
    print(e)

