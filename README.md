# AI Virtual Painter

Welcome to the AI Virtual Painter! This Python application allows you to unleash your creativity by painting virtually using your webcam. Powered by various libraries such as OpenCV, NumPy, and MediaPipe, this project enables real-time hand detection and tracking, turning your hand gestures into colorful strokes on the canvas.

## Features

- Real-time hand detection and tracking.
- Painting with different colors and brush sizes.
- Erasing unwanted strokes.
- Clearing the canvas.
- Saving your masterpiece.

## Requirements

Make sure you have the following libraries installed:

- Python (3.x recommended)
- OpenCV
- NumPy
- MediaPipe

You can install these libraries using pip:

```bash
pip install opencv-python numpy mediapipe
```
## Usage

#### 1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/ai-virtual-painter.git
```
#### 2. Navigate to the project directory:
```bash
cd ai-virtual-painter
```
#### 3. Run the application:
##### - Run in terminal 
````bash
python virtual_painter.py
````

## How It Works
The AI Virtual Painter utilizes hand tracking provided by MediaPipe to detect and track the position of your hand in real-time. By analyzing the movement of your hand, the application interprets it as strokes on the canvas. Different hand gestures are mapped to various functionalities such as changing colors, adjusting brush size, and erasing the canvas.

## Future Improvements
- Implement additional features such as different brush shapes.
- Enhance the user interface for better interaction.
- Optimize performance for smoother painting experience.
- Add support for multiple users painting simultaneously.
- 
## Credits
This project is inspired by various tutorials and resources available online. Special thanks to the developers and contributors of OpenCV, NumPy, and MediaPipe for their amazing libraries.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


##### Feel free to contribute to this project by forking the repository and submitting pull requests! If you encounter any issues or have suggestions for improvements, please open an issue on GitHub. Happy painting! 🎨
