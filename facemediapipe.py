import cv2
import mediapipe as mp
import time
import numpy as np

cap = cv2.VideoCapture(0)

p_time = 0

mp_draw = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
face_img = cv2.imread("img/face1.png", cv2.IMREAD_UNCHANGED)

