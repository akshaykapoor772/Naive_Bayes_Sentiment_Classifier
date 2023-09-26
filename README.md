# Naive Bayes Sentiment Classifier

## Overview
This project implements a Naive Bayes classifier for sentiment analysis. The goal is to classify given text data (such as movie reviews) into one of three categories: positive, negative, or neutral.

## Files in the Repository

* __bayes.py:__ Contains the primary implementation of the Naive Bayes classifier. If dictionaries are not present, it will train the model. Once training is complete, it can classify text data.

* __bayesbest.py:__ An optimized or variant version of the classifier in bayes.py.

* __singleline.py:__ A script to quickly test the classifier on individual sentences provided by the user.

* __evaluate.py:__ Evaluates the performance of the classifier from bayes.py against a test dataset located in the testing/ directory.

* __evaluatebest.py:__ Similar to evaluate.py, but evaluates the classifier from bayesbest.py.

* __Evaluation.pdf:__ A document detailing the evaluation metrics and results for the classifier on a testing dataset of 400 files.

* __Readme.pdf:__ Original documentation file for this project.

## Evaluation Metrics and Results
Metrics Used:

* __Precision:__ The ratio of correctly predicted positive observations to the total predicted positives.
* __Recall (Sensitivity):__ The ratio of correctly predicted positive observations to the all actual positives.
* __F-measure:__ The weighted average of Precision and Recall.

__Bayes Classifier (Normal)__ 
* Precision: 0.54
* Recall: 0.77
* F-measure: 0.63

__Bayes Classifier (Improved)__ 
* Precision: 0.55 
* Recall: 0.90 
* F-measure: 0.68 

## Insights
The system produces satisfactory results according to the evaluated metrics. However, there are occasional incorrect outputs due to the limited word occurrences in the respective dictionary. A word might have a low occurrence in a dictionary but could still belong to a particular class. This limitation can be addressed by training the model on a larger dataset and storing more words in the dictionary.

## Future Work
* __Enhanced Training:__ Training the model on a more extensive dataset can improve accuracy and handle less frequent words better.
* __Model Optimization:__ Exploring other techniques or optimizations, such as incorporating word embeddings, could further enhance the model's performance.

## Sample Run Example
To classify the sentiment of a single sentence using the classifier, you can use the singleline.py script. Here's how to do it:

1. Running the script:

```bash
python singleline.py
```
2. Prompt:\
Once you run the script, you'll be prompted to enter a sentence:
```bash
Enter a sentence to classify its sentiment: 
```
3. User Input: \
Enter a sentence of your choice. For example:
```bash
Enter a sentence to classify its sentiment: The movie was fantastic!
```
4. Output: \
The script will then classify the sentiment of the sentence and display the result:
```bash
The sentiment of the sentence is: Positive
```
This example provides a quick way to test the sentiment classifier on individual sentences. For bulk classification or evaluation, refer to the respective evaluation scripts.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
