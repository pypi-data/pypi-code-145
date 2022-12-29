import copy

import imageio
import cv2
import numpy as np
import os.path
import os
import imageio
import cv2
import open3d as o3d
import scipy.io as sio
import json
import cv2
import random
import PIL.Image
import torch
import networkx as nx
from functools import reduce
from PIL import Image
from numpy import asarray
from ast import literal_eval
from matplotlib import pyplot as plt
from numpy.linalg import inv
from tqdm import tqdm
from glob import glob
from zqmtool.image import to_rgb

# from open3d import JVisualizer
# from open3d.j_visualizer import JVisualizer


"""GENERAL FUNCTIONS """


def load_point_clouds(voxel_size, path):
    pcd = o3d.io.read_point_cloud(path)
    pcd_down = pcd.voxel_down_sample(voxel_size)
    return pcd_down


def getCamera():
    return o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.Kinect2ColorCameraDefault)


#     # Get camera information for AVD scene
#     if os.path.isfile(datapath + scene + "/cameras.txt"):
#         f = open(datapath + scene + "/cameras.txt")
#     else: # if the scene does not have camera file then just use the one from scene 001_1
#         f = open(datapath + "Home_002_1/cameras.txt")

#     data = f.readlines()
#     tok = data[-1].split(" ")
#     intr = []

#     for i in range(4,len(tok)):
#         intr.append(float(tok[i]))

#     return np.asarray(intr, dtype=np.float32) # fx, fy, cx, cy, distortion params


def load_scene_info(avd_root):
    # annotations contains the action information
    # image_structs contains camera information for each image
    image_structs_path = os.path.join(avd_root, 'image_structs.mat')
    annotation_path = os.path.join(avd_root, 'annotations.json')
    data = sio.loadmat(image_structs_path)

    scale = data['scale'][0][0]
    image_structs = data['image_structs'][0]

    rot = image_structs['R']
    trans = image_structs['t']
    im_names_all = image_structs['image_name']  # info 0 # list of image names in the scene
    im_names_all = np.hstack(im_names_all)  # flatten the array
    world_poses = image_structs['world_pos']  # info 3
    directions = image_structs['direction']  # info 4
    annotations = json.load(open(annotation_path))
    return trans, rot, scale, im_names_all


def load_scene_info_rot(avd_root, scene):
    # annotations contains the action information
    # image_structs contains camera information for each image
    image_structs_path = os.path.join(avd_root, scene, 'image_structs.mat')
    annotation_path = os.path.join(avd_root, scene, 'annotations.json')
    data = sio.loadmat(image_structs_path)

    scale = data['scale'][0][0]
    image_structs = data['image_structs'][0]

    rot = image_structs['R']
    trans = image_structs['t']
    im_names_all = image_structs['image_name']  # info 0 # list of image names in the scene
    im_names_all = np.hstack(im_names_all)  # flatten the array
    world_poses = image_structs['world_pos']  # info 3
    directions = image_structs['direction']  # info 4
    annotations = json.load(open(annotation_path))
    return data, world_poses, directions


""" PROJECT RELATED FUNCTIONS """


# visualize the mask on any category (normal, Depth, RGB), for any image (rot)
# filetype , type of the output filr (jpg,png)
# outputFile, the name of the folder of output
# read_dictionary, directory that stors the mask.npy

def maskVisualization(read_dictionary, category, rot, filetype, outputFolder):
    masks = read_dictionary[rot[-19:-4] + '.jpg']
    count = 0

    for j in masks:
        print(j)

        # out = np.zeros((1080,1920,3))
        # new_im = cv2.imread(category +'/'+ rot[-19:-4]+filetype)
        # out[:,:,0] = np.where(j==True,new_im[:,:,0], 255)
        # out[:,:,1] = np.where(j==True,new_im[:,:,1], 255)
        # out[:,:,2] = np.where(j==True,new_im[:,:,2], 255)

        # if os.path.isfile("{}/{}_{}_{}{}".format(outputFolder,rot[-19:-4],category, count,filetype)):
        # print("True")
        # imageio.imwrite("{}/{}_{}_{}{}".format(outputFolder, rot[-19:-4],category, count, filetype),out.astype(np.uint8))

        # count = count+1


def addImgsTOgather(imgPath, outFolder):
    for filename1 in os.listdir(imgPath):
        idd = 0
        for filename2 in os.listdir(imgPath):

            if (filename1[0:15] == filename2[0:15] and idd == 0):
                img = cv2.imread(imgPath + '/' + filename2)
                idd = 1

            elif (filename1[0:15] == filename2[0:15] and idd == 1):
                img = cv2.imread(imgPath + '/' + filename2) + img

        cv2.imwrite("{}/{}{}".format(outFolder, filename1[0:15], filename1[-4:]), img)
        # imageio.imwrite("{}/{}{}".format(outFolder, filename1[0:15],filename1[-4:]),img)


def generatePcdinCameraCoordinat(imgPath, depthpath):
    # im = cv2.imread(imgPath,cv2.IMREAD_UNCHANGED)
    # newsize = (320,240)
    # im1 = cv2.resize(im, newsize)
    # Final_img = im1.astype(dtype=np.float32)
    # cv2.imwrite("out.jpg", Final_img)

    intr = getCamera()
    intr.width = 1920
    intr.height = 1080
    intrinsic_params = intr
    # intrinsic_params = o3d.camera.PinholeCameraIntrinsic()
    # intrinsic_params.set_intrinsics(1920, 1080, intr[0], intr[1], intr[2], intr[3])
    # intrinsic_params.set_intrinsics(320,240,intr[0]/6, intr[1]/4.5, intr[2]/6, intr[3]/4.5)

    color_img = o3d.io.read_image(imgPath)
    # print("color_img",imgPath,color_img)

    depth_img = o3d.io.read_image(depthpath)
    # print('depth_img',depthpath,depth_img)

    rgbd_img = o3d.geometry.RGBDImage.create_from_color_and_depth(color_img, depth_img, convert_rgb_to_intensity=False)
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_img, intrinsic_params)
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])

    return pcd




def convertPcd2WorldCoordinat(pcd, datapath, imgName):
    if imgName.find('.jpg')==-1:
        imgName = imgName+'.jpg'
    voxel_size = 0.02
    pcd = pcd.voxel_down_sample(voxel_size=voxel_size)
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])

    TRS = load_scene_info(datapath)

    [j], = np.where(TRS[3] == imgName)

    R = inv(TRS[1][j])
    t = np.dot(-R, TRS[0][j]) * TRS[2] / 1000
    # print("R Matrix : " , R.shape[0])
    # print("T Matrix : " , t.shape[0])

    if (R.shape[0] != 3 and t.shape[0] != 3):
        return None, None
    else:
        Transformation_Matrix = [[R[0][0], R[0][1], R[0][2], t[0]],
                                 [R[1][0], R[1][1], R[1][2], t[1]],
                                 [R[2][0], R[2][1], R[2][2], t[2]],
                                 [0, 0, 0, 1]]

        pcd = o3d.geometry.PointCloud.transform(pcd, Transformation_Matrix)
        return pcd, Transformation_Matrix


def multiViewPCL(listPclPath, pcdMultiViewOutFolder, name="outMultiView"):
    voxel_size = 0.02

    flag = 0
    for i in listPclPath:
        print("i", i)
        if (flag == 0):
            pcd = load_point_clouds(voxel_size, "{}".format(i))
            flag = 1
        else:
            pcdNew = load_point_clouds(voxel_size, "{}".format(i))
            pcd = pcd + pcdNew

    o3d.io.write_point_cloud("{}/{}.ply".format(pcdMultiViewOutFolder, name), pcd)
    # print(name + ".ply is saved.")


def mapPcdToGround(Pcdpath, mapOutFolder):
    voxel_size = 0.02
    pcd = load_point_clouds(voxel_size, "{}".format(Pcdpath))

    color_cloud = np.asarray(pcd.colors)
    Points = np.asarray(pcd.points)

    plt.scatter(Points[:, 0], Points[:, 2], c=color_cloud, s=1)
    plt.savefig('{}/{}'.format(mapOutFolder, Pcdpath))


def load_coordinate(path, shape, color):
    Transformation_Matrix = np.load(path,allow_pickle=True)
    if shape == 'box':
        scale = 0.2
        coordinate = o3d.geometry.TriangleMesh.create_box(width=scale, height=scale, depth=scale)
    elif shape == 'arrow':
        scale = 0.6
        coordinate = o3d.geometry.TriangleMesh.create_arrow(
            cylinder_height=1e-3, cylinder_radius=1e-3,
            cone_height=scale,cone_radius=0.1,
        )
    else:
        raise NotImplementedError
    coordinate.paint_uniform_color(color)
    # coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5)
    coordinate = o3d.geometry.PointCloud.transform(coordinate, Transformation_Matrix)
    return coordinate


def merge_pcd(path, colors, pcdOutFolder, init_pcd_list=[]):
    print(len(path), len(set(path)))
    voxel_size = 0.02
    pcd_list = copy.deepcopy(init_pcd_list)
    for i, img_name in tqdm(enumerate(glob(os.path.join(pcdOutFolder, '*.ply')))):
        img_name = os.path.basename(img_name).split('.')[0]
        if len(init_pcd_list) == 0:
            pcd_i = load_point_clouds(voxel_size, os.path.join(pcdOutFolder, f'{img_name}.ply'))
            pcd_i.transform([[1, 0, 0, 0], [0, 0, -1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
            pcd_list.append(pcd_i)

        if (img_name + '.jpg' in path):
            shape = 'arrow'
            coordinate_i = load_coordinate(os.path.join(pcdOutFolder, img_name+'.npy'),shape, colors[path.index(img_name + '.jpg')])
            coordinate_i.transform([[1, 0, 0, 0], [0, 0, -1, 0], [0, -1, 0, 0], [0, 0, 0, 1]])
            pcd_list.append(coordinate_i)

    return pcd_list


def visualize_pcd_list(pcd_list, vis, show=True, img_size=2048):
    vis.clear_geometries()
    for pcd in pcd_list:
        vis.add_geometry(pcd)
    set_visualizer_view(vis)

    if show:
        vis.run()
        vis.destroy_window()
        vis.close()
    else:
        vis.poll_events()
        vis.update_renderer()
        state = np.asarray(vis.capture_screen_float_buffer(do_render=True))
        h, w, c = state.shape
        state = cv2.resize(state, (int(img_size * (w / h)), img_size))
        state = np.asarray(state * 255, dtype=np.uint8)
        state = to_rgb(state)
        return state




def define_visualizer(visible):
    vis = o3d.visualization.Visualizer()
    vis.create_window(visible=visible)

    renderopt = vis.get_render_option()
    renderopt.point_size = 0.1

    return vis

def set_visualizer_view(vis):
    ctr = vis.get_view_control()
    # ctr.change_field_of_view(step=-60)
    ctr.set_zoom(0.45)
    # ctr.rotate(0, -100, 0)
