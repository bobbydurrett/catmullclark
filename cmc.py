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

First part of the algorithm on the RC page is

for each face, a face point is created which is the average of all the points of the face.

"""

# square

input_points = [
  [0.0, 0.0,  0.0],
  [1.0, 0.0,  0.0],
  [1.0, 1.0,  0.0],
  [0.0, 1.0,  0.0]
]

input_faces = [
  [0, 1, 2, 3]
]

# 3 dimensional space

NUM_DIMENSIONS = 3

# face points will have one point for each face

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
    
for fp in face_points:
    print(fp)
    
    
            

