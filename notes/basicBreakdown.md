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
- look at translating to CPP / C# (Kadir abi for aid/support if needed?)
- Identify bottle necks and aim to optimize regions that are the most restricting
- Look at the introduction of multithreading and/or gpu acceleration to speed up the computing intensive tasks such as detection and tracking

## Using multiple cameras

#### Benefits

- Improved depth perception, allows for easier and more accurate tracking of 3D coordinates. Also aids in the understanding the motion better.
  - zooming in and out gestures or pulling something to yourself?
- Larger field of view, more room to move your hand,
  - ideal for multiple displays?
- redundancy and robustness, if you have multiple cameras, they can make up for the inaccuracy, delay, errors of the other cameras
- reduced occlusions, if you can see the hand from multiple angles, it means that if something blocks the view of the first camera you can rely on the second one until first one is unobstructed/repositioned
- improved accuracy, more data points to help triangulate information, meaning more accuracy

#### Drawbacks

- cost, requires multiple cameras that are compatible with a use case like this, as well as calibration and syncing equipment if needed
- calibrating cameras, they need to be able to work with one another, in synchronisation and alignment. can be expensive and time consuming and difficult
- data fusion and integration, you need to be able to interpret and process the data from multiple sources and understand what is going on from different perspectives
- physical setup, can be difficult as it requires enough space to have cameras that are steady, do not overlap and have obstructions in front of them

_copy paste of gpt_

The choice between using one infrared (IR) and one regular camera, two infrared cameras, or two regular cameras depends on several factors, including the specific requirements of your hand tracking application, the environment in which it will be used, and the capabilities of the cameras themselves. Here's a breakdown of each option:

1. **One Infrared and One Regular Camera:**

   - **Advantages:**
     - Combining an infrared camera with a regular RGB camera can provide complementary information. The infrared camera can capture depth information, enabling better depth perception for hand tracking.
     - Infrared cameras are less affected by changes in ambient lighting conditions compared to RGB cameras, making them suitable for indoor environments with varying lighting conditions.
   - **Considerations:**
     - Integration and synchronization of data from two different types of cameras (IR and RGB) may require additional effort and calibration to ensure accurate alignment of the depth and color information.
     - Cost may be higher compared to using two cameras of the same type, as you'll need to invest in both an infrared and an RGB camera.

2. **Two Infrared Cameras:**

   - **Advantages:**
     - Using two infrared cameras can provide stereoscopic vision, enabling accurate depth perception and 3D reconstruction of the hand's position and movement.
     - Infrared cameras are less affected by ambient lighting conditions, making them suitable for indoor environments with varying lighting conditions.
   - **Considerations:**
     - Integration and synchronization of data from two infrared cameras are typically easier compared to combining data from different types of cameras. However, you'll still need to ensure accurate calibration and alignment of the cameras.
     - Cost may be higher compared to using two regular RGB cameras, as infrared cameras tend to be more expensive.

3. **Two Regular RGB Cameras:**
   - **Advantages:**
     - Using two RGB cameras can provide stereo vision, enabling depth perception and 3D reconstruction of the hand's position and movement.
     - RGB cameras are more widely available and may be more affordable compared to infrared cameras.
   - **Considerations:**
     - RGB cameras may be more sensitive to changes in ambient lighting conditions compared to infrared cameras. You may need to consider using additional lighting or implementing techniques to mitigate the effects of varying lighting conditions.
     - Ensuring accurate synchronization and calibration of two RGB cameras is essential for accurate depth perception and tracking. Calibration may be more challenging compared to infrared cameras due to potential color variations.

In summary, the choice between using one infrared and one regular camera, two infrared cameras, or two regular RGB cameras depends on factors such as depth perception requirements, environmental conditions, cost considerations, and technical feasibility. Evaluate the specific needs of your hand tracking application and consider the advantages and considerations of each option before making a decision.
