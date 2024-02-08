## Convolutional Neural Network (CNN)

It is composed of 3 main segments, the layers where the image is processed and broken apart. The learning steps where it learns how to interpret data and what to interpret as valid/invalid. And then the final step, recognition where it is given unsorted data to create conclusions based off.

#### 1. Layers

Convolutional layers:
These scan the image in small sections, looking for patterns like edges, corners, textures etc
The areas that are looked at have overlapping sections called receptive fields. Using the patterns found locally, it allows the image to be pieced and processed together

Pooling layers:
They remove redundant data only keeping sections of the image that is identified to have useful information as the convolutional layer might not have done a perfect job or identified a redundant pattern and included it

They condense the most important and standout features that are collected by the convolutional layer and then discard the remainder, allowing the core of the image to be retained and easier to work with for the network

Fully connected layers:
These layers process all the information from previous layers (mainly the refined information from the pooling layers) and is responsible for sorting and interpreting the data given. The layer is tasked with providing a conclusion regarding what the image is about/contains.

#### 2. Learning

Before it can start recognising images, it needs to be trained. This is done by feeding it a large number of data that is already pre-labelled. The CNN adjusts its thinking accordingly based on the data fed.

The internal parameters of the CNN (the brain so to speak) is tweaked with each image that it processes, whether that is due to identifying a new potential pattern, or learning to disregard a certain type of background noise etc.

#### 3. Recognition

You start testing/using the CNN. Feed it unlabelled data and let it sort it out, it should get more and more accurate as it goes on as it has more training data.

With each image provided, the CNN goes through all the layers and other steps, tweaking its parameters as needed and replying with a conclusion when needed.

Ideally once it is able to distinguish "clean" images (simple background, target in focus, etc), the new data being provided should encourage the system to change its parameters and learn how to handle edge cases and/or abnormalities
