import cv2 as cv
import numpy as np


sift = None

def show_features(gray):
    global sift

    if sift is None:
        sift = cv.SIFT_create()

    kps = sift.detect(gray,None)
    img = cv.drawKeypoints(gray, kps, gray)

    cv.imshow('sift_keypoints',img)
    cv.waitKey(0)

def find(temp, scene, MIN_QUALITY):
    global sift

    if sift is None:
        sift = cv.SIFT_create()

    gfrm = scene
    gobj = temp

    tkp, tdsc = sift.detectAndCompute(gfrm, None)

    index_params = dict(algorithm = 1, trees = 24)
    search_params = dict(checks = 250)
    matcher = cv.FlannBasedMatcher(index_params, search_params)

    good = []
    kps  = []

    kp, dsc = sift.detectAndCompute(gobj, None)

    for k in kp:
        kps.append(k)

    matches = matcher.knnMatch(dsc, tdsc, k=2)

    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)
        
    quality = len(good)

    if quality <= MIN_QUALITY:
        return None
    else:
        src_pts = np.float32([kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([tkp[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        m, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
        mask = mask.ravel().tolist()
        h, w = gobj.shape[:2]
        pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
        dst = cv.perspectiveTransform(pts, m)

        box = cv.boundingRect(dst)

        return box