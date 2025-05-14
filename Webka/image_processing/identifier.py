import cv2
import numpy as np
import mediapipe as mp


class ObjectIdentifier:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        try:
            self.pose_detector = self.mp_pose.Pose(
                static_image_mode=False,
                model_complexity=1,
                enable_segmentation=False,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
            )
        except Exception as e:
            print(f"Ошибка инициализации MediaPipe Pose: {e}. Убедитесь, что mediapipe установлен корректно.")
            self.pose_detector = None

        self.person_label = "человек"
        self.dog_label = "собака"

    def identify_objects(self, image_path=None, frame_data=None):
        if not self.pose_detector:
            return ["ошибка инициализации MediaPipe"]

        if frame_data is not None:
            frame = frame_data
        elif image_path is not None:
            frame = cv2.imread(image_path)
        else:
            return ["аргументы не предоставлены"]

        if frame is None:
            return ["ошибка кадра"]

        identified = []

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        results = self.pose_detector.process(image_rgb)
        image_rgb.flags.writeable = True

        if results.pose_landmarks:
            identified.append(self.person_label)

        if not identified:
            identified.append(self.dog_label)

        return identified
