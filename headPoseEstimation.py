import cv2
import dlib
import numpy as np
from imutils import face_utils

face_landmark_path = 'shape_predictor_68_face_landmarks.dat'

K = [6.2500000000000000e+002, 0.0, 3.1250000000000000e+002,
     0.0, 6.2500000000000000e+002, 3.1250000000000000e+002,
     0.0, 0.0, 1.0]

cam_matrix = np.array(K).reshape(3, 3).astype(np.float32)
dist_coeffs = np.zeros((4,1))

object_pts = np.float32([[6.825897, 6.760612, 4.402142],
                         [1.330353, 7.122144, 6.903745],
                         [-1.330353, 7.122144, 6.903745],
                         [-6.825897, 6.760612, 4.402142],
                         [5.311432, 5.485328, 3.987654],
                         [1.789930, 5.393625, 4.413414],
                         [-1.789930, 5.393625, 4.413414],
                         [-5.311432, 5.485328, 3.987654],
                         [2.005628, 1.409845, 6.165652],
                         [-2.005628, 1.409845, 6.165652],
                         [2.774015, -2.080775, 5.048531],
                         [-2.774015, -2.080775, 5.048531],
                         [0.000000, -3.116408, 6.097667],
                         [0.000000, -7.415691, 4.070434]])

reprojectsrc = np.float32([[10.0, 10.0, 10.0],
                           [10.0, 10.0, -10.0],
                           [10.0, -10.0, -10.0],
                           [10.0, -10.0, 10.0],
                           [-10.0, 10.0, 10.0],
                           [-10.0, 10.0, -10.0],
                           [-10.0, -10.0, -10.0],
                           [-10.0, -10.0, 10.0]])

line_pairs = [[0, 1], [1, 2], [2, 3], [3, 0],
              [4, 5], [5, 6], [6, 7], [7, 4],
              [0, 4], [1, 5], [2, 6], [3, 7]]


def get_head_pose(shape):
    image_pts = np.float32([shape[17], shape[21], shape[22], shape[26], shape[36],
                            shape[39], shape[42], shape[45], shape[31], shape[35],
                            shape[48], shape[54], shape[57], shape[8]])

    _, rotation_vec, translation_vec = cv2.solvePnP(object_pts, image_pts, cam_matrix, dist_coeffs)

    reprojectdst, _ = cv2.projectPoints(reprojectsrc, rotation_vec, translation_vec, cam_matrix,
                                        dist_coeffs)

    reprojectdst = tuple(map(tuple, reprojectdst.reshape(8, 2)))

    # calc euler angle
    rotation_mat, _ = cv2.Rodrigues(rotation_vec)
    pose_mat = cv2.hconcat((rotation_mat, translation_vec))
    _, _, _, _, _, _, euler_angle = cv2.decomposeProjectionMatrix(pose_mat)

    return reprojectdst, euler_angle


def getHeadPose(frame):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(face_landmark_path)
    face_rects = detector(frame, 0)

    if len(face_rects) > 0:
        shape = predictor(frame, face_rects[0])
        shape = face_utils.shape_to_np(shape)

        reprojectdst, euler_angle = get_head_pose(shape)

        if -5 < int(euler_angle[2,0]) < 5:
            cv2.putText(frame, "Looking: " + "{a}".format(a="Center"), (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (0, 0, 0), thickness=2)
        elif int(euler_angle[2,0]) <= -5:
            cv2.putText(frame, "Looking: " + "{a}".format(a="Left"), (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (0, 0, 0), thickness=2)
        elif int(euler_angle[2,0]) >=5 :
            cv2.putText(frame, "Looking: " + "{a}".format(a="Right"), (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (0, 0, 0), thickness=2)

        return int(euler_angle[2,0])
