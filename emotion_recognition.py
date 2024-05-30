from deepface import DeepFace


def recognize_emotion(face_image):
    result = DeepFace.analyze(face_image, actions=['emotion'])
    return result['dominant_emotion']
