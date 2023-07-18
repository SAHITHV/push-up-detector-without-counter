# Push-Up Detector

## Description

The Push-Up Detector is a computer vision application that uses a webcam to automatically detect and count push-up repetitions in real-time. The program utilizes deep learning techniques, specifically object detection models, to identify human body poses and track push-up movements.

## Table of Contents

Installation
Usage
Requirements
Contributing
License

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/SAHITHV/push-up-detector.git
```

2. Change into the project directory:

```bash
cd push-up-detector
```

3. Install any required dependencies (if any) by running:

```bash
pip install -r requirements.txt
```

4. Download the pre-trained object detection model (e.g., YOLO, SSD) by following the instructions in the `models/README.md` file.

## Usage

To use the Push-Up Detector, follow these steps:

1. Make sure you have Python and a compatible webcam connected to your machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the `push_up_detector.py` script:

```bash
python push_up_detector.py
```

4. The webcam feed will appear with bounding boxes around detected human body poses and a push-up counter displayed on the screen.

5. Perform push-ups within the webcam's view, and the detector will track and count each repetition.

6. Press the `q` key to exit the program.

## Requirements

The Push-Up Detector requires the following:

- Python (version >= 3.x)
- Webcam (built-in or external)

## Contributing

Contributions to this project are welcome! If you find any bugs, have feature requests, or want to improve the code, feel free to open an issue or submit a pull request.

When contributing, please follow the existing coding style, and make sure to thoroughly test your changes.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as you see fit. See the [LICENSE](LICENSE) file for more details.

## Credits

The Push-Up Detector was developed by SAHITH (https://github.com/SAHITHV). If you have any questions or need assistance, feel free to reach out to me. Happy push-up detecting!# push-up-detector-without-counter
