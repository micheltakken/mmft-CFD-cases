"""These are helper functions used to define channel objects that are written
in STL format"""

import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
import json

def main():
    channelWidth = 1e-4
    channelHeight = 1e-4;

    node0 = [0.0, 0.0]
    node1 = [0.0, 4e-3]
    node2 = [2e-3, 2e-3]
    node3 = [4e-3, 2e-3]
    node4 = [6e-3, 0.0]
    node5 = [6e-3, 4e-3]

    gamma = np.arctan(node2[0]/node2[1])
    beta = 0.5*np.pi - gamma


    vertices = np.zeros((16,2))

    vertices[0] = np.array([node0[0]-np.cos(gamma)*channelWidth*0.5, node0[1]+np.cos(beta)*channelWidth*0.5])
    vertices[1] = np.array([node0[0]+np.cos(gamma)*channelWidth*0.5, node0[1]-np.cos(beta)*channelWidth*0.5])
    vertices[2] = np.array([(node2[1]-0.5*channelWidth)/np.tan(beta)+(0.5*channelWidth)/np.sin(beta), node2[1]-0.5*channelWidth])
    vertices[3] = np.array([(node2[1]-(0.5*channelWidth)/np.cos(beta))/np.tan(beta), node2[1]])
    vertices[4] = np.array([node1[0]+np.cos(gamma)*channelWidth*0.5, node1[1]+np.cos(beta)*channelWidth*0.5])
    vertices[5] = np.array([node1[0]-np.cos(gamma)*channelWidth*0.5, node1[1]-np.cos(beta)*channelWidth*0.5])
    vertices[6] = np.array([vertices[2][0], node2[1]+0.5*channelWidth])
    vertices[7] = np.array([0.0, 0.0])
    vertices[8] = np.array([node4[0]-vertices[2][0], vertices[2][1]])
    vertices[9] = np.array([0.0, 0.0])
    vertices[10] = np.array([node4[0]-vertices[3][0], vertices[3][1]])
    vertices[11] = np.array([node4[0]-np.cos(gamma)*channelWidth*0.5, node4[1]-np.cos(beta)*channelWidth*0.5])
    vertices[12] = np.array([node4[0]+np.cos(gamma)*channelWidth*0.5, node4[1]+np.cos(beta)*channelWidth*0.5])
    vertices[13] = np.array([node4[0]-vertices[6][0], vertices[6][1]])
    vertices[14] = np.array([node5[0]+np.cos(gamma)*channelWidth*0.5, node5[1]-np.cos(beta)*channelWidth*0.5])
    vertices[15] = np.array([node5[0]-np.cos(gamma)*channelWidth*0.5, node5[1]+np.cos(beta)*channelWidth*0.5])

    vertices2 = np.zeros((6,2))

    vertices2[0] = np.array([vertices[2][0], node2[1]])
    vertices2[1] = np.array([vertices[8][0], node2[1]])
    vertices2[2] = np.array([vertices[3][0] + np.cos(gamma)*channelWidth, vertices[3][1] - np.sin(gamma)*channelWidth])
    vertices2[3] = np.array([vertices[3][0] + np.cos(gamma)*channelWidth, vertices[3][1] + np.sin(gamma)*channelWidth])
    vertices2[4] = np.array([vertices[10][0] - np.cos(gamma)*channelWidth, vertices[10][1] - np.sin(gamma)*channelWidth])
    vertices2[5] = np.array([vertices[10][0] - np.cos(gamma)*channelWidth, vertices[10][1] + np.sin(gamma)*channelWidth])

    print("vertices (")
    for vertex in vertices:
        print("\t({:.20f} {:.20f} 0)".format(vertex[0], vertex[1]))
    for vertex in vertices:
        print("\t({:.20f} {:.20f} 0.0001)".format(vertex[0], vertex[1]))
    for vertex in vertices2:
        print("\t({:.20f} {:.20f} 0)".format(vertex[0], vertex[1]))
    for vertex in vertices2:
        print("\t({:.20f} {:.20f} 0.0001)".format(vertex[0], vertex[1]))
    print(");")


if __name__ == "__main__":
    main()