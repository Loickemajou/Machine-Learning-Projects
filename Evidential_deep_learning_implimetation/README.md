#  Evidential Deep Learning on MNIST

This project demonstrates **Evidential Deep Learning (EDL)** applied to the **MNIST dataset** using PyTorch.  
The model not only performs digit classification but also estimates the **uncertainty** in its predictions using a **Dirichlet distribution** as the output layer.

---

##  Overview

The notebook trains a **LeNet-style convolutional neural network** with a custom **Dirichlet output layer** for evidential reasoning.  
Uncertainty is quantified by the **evidence** assigned to each class, as defined in the referenced EDL framework.

The project explores model behavior under **input perturbations** (e.g., image rotation) and visualizes how uncertainty changes with transformation.

---

##  Key Components

- **Dataset:** MNIST (handwritten digits)
- **Model Architecture:**  
  - Two convolutional layers  
  - Two max-pooling layers  
  - Two fully connected layers  
  - Custom `Dirichlet` layer as the output  
- **Loss Function:**  
  Custom evidential classification loss from EDL

---

##  References

This implementation uses core components (the **loss function** and **Dirichlet layer**) from the excellent open-source repository:  
 [teddykoker/evidential-learning-pytorch](https://github.com/teddykoker/evidential-learning-pytorch/tree/main)

---

##  Training and Evaluation

The model is trained on MNIST for 10 epochs using Adam optimizer.  
Training and testing functions report both **loss** and **accuracy** per epoch.



## Visualisation
https://github.com/Loickemajou/Machine-Learning-Projects/blob/main/Evidential_deep_learning_implimetation/images/image_evd.png
Uncertainty under rotation
https://github.com/Loickemajou/Machine-Learning-Projects/blob/main/Evidential_deep_learning_implimetation/images/uncertainty.png

