# emotion_attendance_system

- This project is a system that can detect the emotion of a person and mark the attendance of the person.
- The system uses the [FER2013](https://www.kaggle.com/msambare/fer2013) dataset for training the tensorflow model(model.h5).
- The system uses diffusers to create face data for training the [Scikit-learn](https://scikit-learn.org/stable/) model.
- The system uses [Scikit-learn](https://scikit-learn.org/stable/) library to training model based on the dataset create by [Mediapipe](https://mediapipe.dev/). 
- The system uses the [Mediapipe](https://mediapipe.dev/) library for detecting facial landmarks. 
- The system uses the [OpenCV](https://opencv.org/) library for capturing the video feed from the webcam.
