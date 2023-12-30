# Real-Time Webcam Image Processing

This Python project captures images from a webcam, applies a pipeline of filters to each image, and displays the result in real time. The user can switch between different pipelines by pressing 'a', 'b', or 'c', and can quit the program by pressing 'q'. The filters applied in the pipelines are an emboss filter, a histogram equalization, and a color inversion.

## Project Structure

The project consists of several functions:

- `initializeWebCam()`: This function initializes the webcam and returns the video device.
- `terminateWebCam(videoDevice)`: This function releases the webcam device.
- `getImage(videoDevice)`: This function captures an image from the webcam and returns it in PIL format.
- `embossFilter(npImage)`: This function applies an emboss filter to an image and returns the result.
- `equalizeFilter(npImage)`: This function equalizes the histogram of an image and returns the result.
- `invertFilter(npImage)`: This function inverts the colors of an image and returns the result.
- `showImage(npImage)`: This function displays an image.
- `prccessingPipeline(npImage, Pipeline)`: This function applies a pipeline of filters to an image and returns the result.

In the main function, these functions are used to capture an image from the webcam, apply the filters, and display the result.

## Requirements

- Python 3.8 or higher
- OpenCV 4.5.3 or higher
- PIL 8.3.2 or higher
- NumPy 1.21.2 or higher

## Running the Project

To run the project, simply execute the script. Make sure that the necessary libraries (OpenCV, PIL, and NumPy) are installed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license. For more information, please refer to the LICENSE file.

## Contact

For any queries or suggestions, please open an issue on this repository. Happy coding!
