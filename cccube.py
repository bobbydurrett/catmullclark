from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

"""

cube from http://rosettacode.org/wiki/Talk:Catmull%E2%80%93Clark_subdivision_surface

"""

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

"""

Plot each face

"""

for facenum in range(len(input_faces)):
    curr_face = input_faces[facenum]
    xcurr = []
    ycurr = []
    zcurr = []
    for pointnum in range(len(curr_face)):
        xcurr.append(input_points[curr_face[pointnum]][0])
        ycurr.append(input_points[curr_face[pointnum]][1])
        zcurr.append(input_points[curr_face[pointnum]][2])
    xcurr.append(input_points[curr_face[0]][0])
    ycurr.append(input_points[curr_face[0]][1])
    zcurr.append(input_points[curr_face[0]][2])
    
    ax.plot(xcurr,ycurr,zcurr,color='b')

plt.show()
