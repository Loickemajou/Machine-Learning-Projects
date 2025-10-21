# Summary of "Classifying Individual Micros" Notebook

This notebook explores the application of machine learning for breast cancer data classification, focusing on two distinct tasks: classifying individual micros and classifying the overall subject (patient) based on those micro predictions.

# Overall Approach and Task 1: Individual Micro Classification

The primary model used throughout the notebook is the Random Forest Classifier.

## Goal

Task 1 aimed to classify individual micros (likely small, localized regions or data points within the sample) as either malignant or benign based on their feature data.

## Methodology
 1-The necessary data (breast_cancer_data.csv and true_labels_and_clinical_data.csv) was loaded and prepared.

 2-Relevant features were selected to train the Random Forest model.

 3-The data was split into training and testing sets.

 4-The Random Forest model was trained on the individual micro data.

## Performance

The resulting classification accuracy for Task 1 on the test data (individual micros) was approximately 68%.

# Task 2: Subject-Level Classification

## Goal

Task 2 aimed to use the predictions from Task 1 to classify whether an entire subject (patient) had cancer (malignant) or not.

## Methodology

The individual micro predictions from the Random Forest model were used to calculate the percentage of predicted malignant micros for each subject.

A threshold was applied to this percentage to determine the subject's final classification (Malignant or Benign).

The notebook determined that a threshold of 35% (if 35% or more of a subject's micros were predicted malignant, the subject was classified as having cancer) provided a suitable balance for the task.

## Performance

The final classification accuracy for Task 2 on the subject-level test data (classifying the presence of cancer) was approximately 64.28%.
