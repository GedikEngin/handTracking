## Plan

To execute actions and have the computer interpret and do the appropriate event/action, you need to first have the code for the instruction in place.

<br>

#### 1. Creating commands

Using an ESP32 to act as a medium between buttons and computer, it is used to emulate mouse actions such as left click, right click, mouse wheel etc

It should also have other functions and/or shortcuts that might be needed , such as scrolling/zooming in and out, done by using a sliding potentiometer

Testing that the buttons and commands work properly

<br>

#### Interpreting hand gestures and motions

One of the reasons for this project is the exposure to machine learning and neural networks. To develop a convolutional neural network, you need to gather the data to train it on first, consisting of the target (hands) from different angles, different lighting, different backgrounds etc to give it exposure to different "common/day to day" differences

Training the model itself, you need to adjust parameters and the network architecture. Doing this as well as mixing up the dataset provided, it should increase the accuracy and generalisation of the model as a whole.

<br>

#### 3. Linking the hand gestures to motions

Once the commands, functions and instructions are ready, as well as the trained neural network, you can integrate both parts together. The CNN should recognize your hand, gesture, position and motion, and then execute the command that corresponds to it.

It should be able to process the images and frames passed through from the camera in real time and execute the corresponding code/function once it is certain of the gesture/action being displayed

<br>

#### 4. Additions

A basic UI either web based or running a full app using Tkinter or PyQt, so that the user can see what the cameras are picking up, how the users hand is being tracked and broken down, and what gesture the CNN thinks the user is trying to do.

The code may need optimisation, enough where the delay is negligible between action being initiated and the end result of said action. Best way would be to identify the largest bottle necks within the system and target those directly, and then if further optimisation is needed, work on the smaller areas
