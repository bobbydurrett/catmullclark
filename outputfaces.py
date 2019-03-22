from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

"""

desired output after one iteration
from http://rosettacode.org/wiki/Talk:Catmull%E2%80%93Clark_subdivision_surface

"""

output_points = [
  [-0.555556,  0.555556,  0.555556],
  [-0.555556, -0.555556,  0.555556],
  [ 0.555556, -0.555556,  0.555556],
  [ 0.555556,  0.555556,  0.555556],
  [ 0.555556, -0.555556, -0.555556],
  [ 0.555556,  0.555556, -0.555556],
  [-0.555556, -0.555556, -0.555556],
  [-0.555556,  0.555556, -0.555556],
  [ 0.000000,  0.000000,  1.000000],
  [-0.750000,  0.000000,  0.750000],
  [ 0.000000, -0.750000,  0.750000],
  [ 0.750000,  0.000000,  0.750000],
  [ 0.000000,  0.750000,  0.750000],
  [ 1.000000,  0.000000,  0.000000],
  [ 0.750000, -0.750000,  0.000000],
  [ 0.750000,  0.000000, -0.750000],
  [ 0.750000,  0.750000,  0.000000],
  [ 0.000000,  0.000000, -1.000000],
  [ 0.000000, -0.750000, -0.750000],
  [-0.750000,  0.000000, -0.750000],
  [ 0.000000,  0.750000, -0.750000],
  [ 0.000000,  1.000000,  0.000000],
  [-0.750000,  0.750000,  0.000000],
  [-1.000000,  0.000000,  0.000000],
  [-0.750000, -0.750000,  0.000000],
  [ 0.000000, -1.000000,  0.000000]
]

output_faces = [
  [ 0,  9,  8, 12],
  [ 1, 10,  8,  9],
  [ 2, 11,  8, 10],
  [ 3, 12,  8, 11],
  [ 3, 11, 13, 16],
  [ 2, 14, 13, 11],
  [ 4, 15, 13, 14],
  [ 5, 16, 13, 15],
  [ 5, 15, 17, 20],
  [ 4, 18, 17, 15],
  [ 6, 19, 17, 18],
  [ 7, 20, 17, 19],
  [ 7, 22, 21, 20],
  [ 0, 12, 21, 22],
  [ 3, 16, 21, 12],
  [ 5, 20, 21, 16],
  [ 7, 19, 23, 22],
  [ 6, 24, 23, 19],
  [ 1,  9, 23, 24],
  [ 0, 22, 23,  9],
  [ 6, 24, 25, 18],
  [ 1, 10, 25, 24],
  [ 2, 14, 25, 10],
  [ 4, 18, 25, 14]
]

"""

Plot each face

"""

for facenum in range(len(output_faces)):
    curr_face = output_faces[facenum]
    xcurr = []
    ycurr = []
    zcurr = []
    for pointnum in range(len(curr_face)):
        xcurr.append(output_points[curr_face[pointnum]][0])
        ycurr.append(output_points[curr_face[pointnum]][1])
        zcurr.append(output_points[curr_face[pointnum]][2])
    xcurr.append(output_points[curr_face[0]][0])
    ycurr.append(output_points[curr_face[0]][1])
    zcurr.append(output_points[curr_face[0]][2])
    
    ax.plot(xcurr,ycurr,zcurr,color='b')

plt.show()
