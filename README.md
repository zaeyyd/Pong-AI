# Pong-AI

Small project that I've been working on to learn more about applications of AI. 

 ### Version 1 
 
![Gif of Pong v1](v1gif.gif) 

 ### Version 2
 
![Gif of Pong v2](v2gif.gif) 



## AI-Overview

  The pong AI was created using a Neural Network consisting of 4 dense layers.
  ```
  const model = tf.sequential();
  model.add(tf.layers.dense({units: 256, inputShape: [8]})); 
  model.add(tf.layers.dense({units: 512, inputShape: [256]}));
  model.add(tf.layers.dense({units: 256, inputShape: [512]}));
  model.add(tf.layers.dense({units: 3, inputShape: [256]}));
  ```
 - The first layer takes in 8 data points to train the model:
  
     1.  Player Paddle Location 
     2.  Computer Paddle Location 
     3.  Ball x coordinate
     4.  Ball y coordinate
     5.  Previous Ball x coordinate
     6.  Previous Ball y coordinate
     7.  Previous Player Paddle Location
     8.  Previous Computer Paddle Location
   
  - The forth and final layer outputs 3 data points that determines if the paddle goes left,right or stays in the same location.
  
### Version 1: 

  **Training**
  
  Version 1 was trained on data collected from a human playing against a simple pong computer algorithm for **15 rounds**.
  
  **Performance** 
  
  Performance was very interesting for a model with such a small training dataset. As seen in the gif at the top of the README, the AI would hit the ball sometimes, and other times it would just stay still and not even attempt to hit the ball. 
  
  Another interesting observation was that sometimes the AI would just mimic the human player's moves, irrespective of of the ball's location.
  
  
### Version 2: 

  **Training**
  Version 2 was trained on **100,000 rounds** against a computer algorithm (the same algorithm that the a human plays against in Version 1). The computer algorithm essentially tries to keep the paddle aligned with the ball at all times.
  
  **Performance** 
  
  Performance was much better than Version 1. As seen in the gif at the top of the README, the AI would almost always hit the ball. 
  
  The AI was basically being taught to play like the computer algorithm mentioned before, and it succeeded in doing so.

## Acknowledgments

* Big thanks to @Sentdex for his ML videos
