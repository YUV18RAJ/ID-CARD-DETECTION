# ID Card Detection Project

## Overview
This project implements an ID card detection system using YOLOv5, an advanced deep learning model for image segmentation and detection. The system focuses on segmenting individuals based on the presence of ID cards and ID tags, particularly identifying whether they are wearing the ID card. Key components include image annotation with CVAT.ai, bulk image resizing with bermi.net, and training/testing the model on video data.

## Key Components
- **YOLOv5:** State-of-the-art deep learning model for real-time object detection.
- **CVAT.ai:** Tool for image annotation, crucial for labeling ID cards and tags in the training data.
- **bermi.net:** Used for bulk image resizing, ensuring compatibility with YOLOv5 requirements.

## Project Structure

|-- data/ # Directory for storing dataset and annotations
|-- models/ # Directory for YOLOv5 model configurations
|-- src/ # Source code directory
| |-- train.py # Script for training the YOLOv5 model
| |-- detect_video.py # Script for testing the model on video data
|-- utils/ # Utility scripts and tools
|-- README.md # Project documentation
|-- requirements.txt # List of required Python packages
|-- your_data.yaml # Configuration file for YOLOv5 training data
|-- .gitignore # Git ignore file



## Getting Started
1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Install required packages: `pip install -r requirements.txt`
3. Set up your dataset and annotations in the `data/` directory.
4. Configure YOLOv5 training in `your_data.yaml` and run `src/train.py`.
5. Test the trained model on video data using `src/detect_video.py`.

## Results
The project aims to accurately segment individuals based on ID card presence. Output includes annotated images or video frames showcasing detected ID cards.

## End Users
- Security personnel
- Access control systems operators
- Facility managers
- Human resources (HR) departments
- Institutions and organizations
- Event organizers
- Government agencies
- System administrators
- Compliance officers
- Application developers
- End users of integrated applications


## License
This project is licensed under the [MIT License](LICENSE).
