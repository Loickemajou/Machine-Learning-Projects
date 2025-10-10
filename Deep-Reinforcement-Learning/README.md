# 🚀 Deep Q-Learning for Lunar Lander

This project implements a **Deep Q-Network (DQN)** to train an agent to land a lunar module safely in the OpenAI Gym environment.

---

## 🎯 Objectives
- Use reinforcement learning to solve a control problem.
- Implement Q-learning with a neural network as a function approximator.

---

## 🧠 Model Architecture
- Input: 8 continuous state variables (position, velocity, angle, etc.)
- Output: Q-values for 4 discrete actions.
- Hidden Layers: 2 fully connected layers (ReLU activation)

---

## 🧩 Results
The agent successfully learns to land with an average score > 200 after ~500 episodes.
![Lunar Lander Result](./lunar_landing.mp4)


---

## 📊 Libraries
- Python  
- PyTorch  
- NumPy  
- Matplotlib 
- OpenAI Gym

---

## 🔗 View Notebook
[Open in nbviewer](https://nbviewer.org/github/Loickemajou/Machine-Learning-Projects/blob/main/Deep-Reinforcement-Learning/Deep_Q_Learning_for_Lunar_Landing_Complete.ipynb)
