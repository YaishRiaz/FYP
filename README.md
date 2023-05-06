# AI-Ref Foul Recognition
AI-Ref Foul Recognition is an application that allows users to analyze video clips and detect fouls in a sports context. This project contains both server-side (backend) and client-side (frontend) code. In this document, you'll find instructions and step-by-step guides on how to run both the frontend and backend.

## Folder Structure

```
FYP/
│
├── README.md
├── requirements.txt
│
├── client/
│   ├── app.py
│   │
│   ├── static/
│   │
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   │
│   └── uploads/
│
└── server/
    ├── punch_classifier_model.h5
    └── PunchClassifierSystem.ipynb
```

## Prerequisites
Before running the application, make sure you have the following software installed on your system:

- Python 3.x
- Flask
- TensorFlow
- Numpy
- OpenCV

## Backend Setup

1. Navigate to the project directory.
2. Install the required Python packages by running 
```
pip install -r requirements.txt
```
3. Run the Flask server by executing the following
```
python app.py
```

## Frontend Setup
1. Ensure the backend is running before starting the frontend.
2. Open a web browser and navigate to http://localhost:5000 to access the frontend.

## Using the Application
1. Uploading a video
    1. On the homepage, click the "Choose File" button and select a video file (mp4 format).
    2. The video preview will appear on the left side of the screen.
2. Analyzing the video
    1. After selecting a video, click the "Analyze" button.
    2. The result will be displayed below the "Analyze" button.
3. Viewing the stats dashboard
    1. After analyzing the video, the "Check Stats" button will appear.
    2. Click the "Check Stats" button to view the stats dashboard, where you can find information about the detected foul and its type.

## Frontend Files
The frontend files are located in the templates folder:

- **index.html**: Contains the main interface for uploading and analyzing videos.
- **dashboard.html**: Contains the stats dashboard for displaying foul information.

## Application Structure
The main Flask application file, app.py, is located in the same level as the templates folder. The backend code handles video uploads, video analysis, and result generation. The application uses a pre-trained TensorFlow model to analyze the uploaded videos and detect fouls.

## Extra links
- **Google drive (Codes)** - https://drive.google.com/drive/folders/1OXDXDuMW1YsbwgvTlavdVp2os__c2h-z?usp=share_link - Contains the codes
- **Google drive (Dataset)** - https://drive.google.com/drive/folders/1kjMKhYegBG4J_p_sKeimlx_pZABXA1oa?usp=share_link - Contains the dataset of foul, non foul punches as well as test data to test the punches
- **Google drive (Thesis)** - https://drive.google.com/drive/folders/16ypct-mWBgXKW83J45xBg_0E9k_54baE?usp=share_link - Contains the thesis
- **Youtube (Demo)** - https://youtu.be/gcKHSCb46Bs - Contains the basic demo of the project