import numpy as np


def est_homography(X, Y):
    """
    Calculates the homography of two planes, from the plane defined by X
    to the plane defined by Y. In this assignment, X are the coordinates of the
    four corners of the soccer goal while Y are the four corners of the penn logo

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        Y: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
    Returns:
        H: 3x3 homogeneours transformation matrix s.t. Y ~ H*X

    """


    src_pts = np.array([
        [X[0,0], X[0,1]],
        [X[1,0], X[1,1]],
        [X[2,0], X[2,1]],
        [X[3,0], X[3,1]]
    ])

    dest_pts = np.array([
        [Y[0,0], Y[0,1]],
        [Y[1,0], Y[1,1]],
        [Y[2,0], Y[2,1]],
        [Y[3,0], Y[3,1]]
    ])


    A = []
    for i in range(4):
        x, y = src_pts[i][0], src_pts[i][1]
        x_prime, y_prime = dest_pts[i][0], dest_pts[i][1]
        A.append([-x, -y, -1, 0, 0, 0, x_prime * x, x_prime * y, x_prime])
        A.append([0, 0, 0, -x, -y, -1, y_prime * x, y_prime * y, y_prime])

    A = np.array(A)
    U, S, Vt = np.linalg.svd(A)
    H = Vt[-1].reshape(3, 3)
    H /= H[2, 2]

    return H


if __name__ == "__main__":
    # You could run this file to test out your est_homography implementation
    #   $ python est_homography.py
    # Here is an example to test your code, 
    # but you need to work out the solution H yourself.
    X = np.array([[0, 0],[0, 10], [5, 0], [5, 10]])
    Y = np.array([[3, 4], [4, 11],[8, 5], [9, 12]])
    H = est_homography(X, Y)
    print(H)
    
