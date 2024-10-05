import numpy as np
from est_homography import est_homography


def warp_pts(X, Y, interior_pts):
    """
    First compute homography from video_pts to logo_pts using X and Y,
    and then use this homography to warp all points inside the soccer goal

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        Y: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
        interior_pts: Nx2 matrix of points inside goal
    Returns:
        warped_pts: Nx2 matrix containing new coordinates for interior_pts.
        These coordinate describe where a point inside the goal will be warped
        to inside the penn logo. For this assignment, you can keep these new
        coordinates as float numbers.

    """

    # You should Complete est_homography first!
    H = est_homography(X, Y)
    warped_pts = []

    ##### STUDENT CODE START #####
    for pt in interior_pts:
        
        pts = np.array([
            [pt[0]],
            [pt[1]],
            [1],
        ])

        val = H.dot(pts)

        val = val / val[2]
        

        # val_3d = np.array([
        #     [val[0][0]],
        #     [val[1][0]],
        # ])
        val_3d = [val[0][0], val[1][0]]

        warped_pts.append(val_3d)

    warped_pts = np.array(warped_pts)
    print(warped_pts.shape())
    


    

    return warped_pts
