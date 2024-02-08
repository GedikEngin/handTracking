## What is needed to be able to use hand tracking using cameras, and gestures to control a mouse:

#### Computer Vision basics:

- computer vision
  - image processing
  - feature extraction
  - object detection
- libraries such as OpenCV
  - example use:
  - reading an image, applying filters and detecting objects within the image
  - similar to captcha, maybe test on it?

#### Hand detection and tracking:

- learn how to detect and track a hand
  - be able to identify the differences one frame to another, and the change over time
  - potential prediction algorithm? to speed up processing, predict users momentum/hand movement and learn it over time or use a regression model?
- background subtraction
  - identify different skin tones, ignoring background noise, distinguishing what is the focus object
  - using Haar Cascades algorithm?
    - splitting the objects within the image into rectangles and subtracting areas to create a rough "image outline" of the subject
    - train using images that have "target" object (hand in this case)
    - train using images without "target" object
    - algo learns to distinguish based on the shapes and areas it learns to recognize
    - further trained and refined by giving "target" object from different positions (i.e. top left of image, bottom right etc) and different distances
- OpenCV has pre trained models for hand detection and tracking and built in functions
  - ideally avoid pre built models as its an opportunity to get into AI/machine learning as well, if needed use as guide and inspiration

#### Gesture recognition:

- understand how to recognize gestures and shapes being made by the hand/s
  - having a set of gestures and creating algorithms to recognize and interpret them
    - will need training to increase accuracy
- techniques to template match, machine learning or neural networks
  - template matching
    - having an image/set of images that execute the "perfect" gesture/motion
    - compare user input to that
  - machine learning classification
    - collect images of basic gestures/motions
    - either extract features
    - or use a convolutional neural network (machine learning/ai)
      - check [Machine Learning & AI notes](..\basicAiMl.md)

#### Integration with mouse control:

- learn how to simulate mouse movements and clocks
  - need to understand how an operating system might take in and handle the data and adjust accordingly
- libraries, API's, third-party libs exist that can do this
  - ideally try to create own one to have exposure to more low level io mechanics and potentially OS exposure
- potential library is PyAutoGui
  - automatically controls cursor position and executes clicks

#### Camera input handling:

- understand how capturing and processing images and video frames from a camera feed/s work
- learn how to calibrate camera/s, adjusting frame rate, resolution and distortion correction
  - camera distortion possibly fixed by using multiple cameras?
- OpenCV can be used to capture video frames from devices connected to system

#### UI:

- a simple UI to help configure parameters if needed, and receive visual feedback and confirmation from the app
- use gui frameworks such as
  - Tkinter (previous experience)
  - PyQt (new framework, might be difficult to explore but could lend itself to increased use when/if using C++ Qt)
  - Web based UI (chance to explore react, or have an easy time using HTML/CSS/JS)
- allows user to see how their hand is being recognized and treated

#### Optimisation:

- Optimize to be a valid substitute to real time mouse
- look at translating to CPP (Kadir abi for aid/support if needed?)
- Identify bottle necks and aim to optimize regions that are the most restricting
- Look at the introduction of multithreading and/or gpu acceleration to speed up the computing intensive tasks such as detection and tracking
