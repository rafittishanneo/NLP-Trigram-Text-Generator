# 📚 NLP Trigram Text Generator

## 📖 Overview

This project demonstrates the implementation of a **Trigram Language Model** using Python without relying on pre-built n-gram modeling libraries.

The model analyzes a text corpus to learn the probability of a word based on the **two words that appear before it**. It can then use these learned probabilities to generate new text from a given starting phrase.

The project also demonstrates **Laplace smoothing**, **text generation**, **perplexity-based evaluation**, and an optional **linear interpolation** approach.

---

## 🚀 Key Features

* 🔤 Text cleaning and tokenization
* 📊 Unigram, bigram, and trigram frequency calculation
* 🧮 Trigram probability estimation
* 🛡️ Laplace/Add-1 smoothing for unseen sequences
* ✍️ Seed-based text generation
* 📈 Perplexity calculation
* ⭐ Optional linear interpolation model
* 🐍 Implemented entirely in Python

---

## 📊 Dataset

The project uses the **NLTK Gutenberg Corpus** as its source of training text.

### Selected Text

**Shakespeare's *Julius Caesar***

The corpus provides a large collection of naturally occurring English sentences that can be used to train and test the statistical language model.

---

## 🧠 Methodology

### 1. Text Preprocessing

Before constructing the language model, the corpus is prepared by:

* Converting all text to lowercase
* Removing unnecessary punctuation
* Splitting the text into individual words
* Creating a vocabulary
* Preparing word sequences for n-gram analysis

---

### 2. Building the Trigram Model

A trigram consists of three consecutive words.

For example:

```text
the king is
king is dead
is dead now
```

The model estimates the probability of the third word using the previous two words:

```text
P(w₃ | w₁, w₂)
```

Frequency dictionaries are used to store the required word and sequence counts.

---

### 3. Laplace Smoothing

A major problem with statistical language models is the **zero-probability problem**.

If a particular trigram does not appear in the training corpus, its probability would normally become zero.

To overcome this, the project uses **Add-1/Laplace smoothing**:

```text
P(w₃ | w₁,w₂) =
(count(w₁,w₂,w₃) + 1)
/
(count(w₁,w₂) + V)
```

where `V` represents the vocabulary size.

This allows the model to assign a non-zero probability to previously unseen word sequences.

---

## ✍️ Text Generation

The trained model can generate text from a user-provided seed containing two words.

For example:

```text
Seed: the king
```

The model examines possible next words and selects the word with the highest estimated probability.

The process continues until the requested number of words has been generated.

### Generation Strategy

The basic generator uses **greedy selection**, meaning that the most probable next word is selected at each step.

---

## 📈 Model Evaluation

The language model is evaluated using **perplexity**.

Perplexity measures how well the model predicts a sequence of words.

```text
Lower perplexity → Better prediction
Higher perplexity → Poorer prediction
```

The evaluation can be performed on a test sentence that was not directly used during model construction.

---

## ⭐ Linear Interpolation

As an additional approach, the project can combine probabilities from different n-gram models.

The interpolation model considers:

* Unigram probability
* Bigram probability
* Trigram probability

The combined probability can be represented as:

```text
P = λ₁P(unigram)
  + λ₂P(bigram)
  + λ₃P(trigram)
```

where the lambda values control the contribution of each model.

This provides a more flexible probability estimate when trigram information is unavailable or unreliable.

---

## 📌 Example Output

```text
=== Corpus Information ===
Vocabulary Size: 8000
Total Tokens: 30000

=== Text Generation ===
Seed: the king

Generated Text:
the king ...

=== Model Evaluation ===
Test Sentence:
the king is dead

Perplexity:
120.45
```

*The actual values depend on the corpus, preprocessing steps, and implementation.*

---

## 🛠️ Technologies Used

* **Python**
* **NLTK**
* **Natural Language Processing**
* **Statistical Language Modeling**
* **Gutenberg Corpus**

---

## 🎯 Learning Objectives

This project provides practical experience with:

* Understanding n-gram language models
* Working with text corpora
* Building probability-based NLP models
* Solving unseen-word sequence problems
* Applying smoothing techniques
* Generating text statistically
* Measuring language model performance with perplexity

---

## ⚠️ Implementation Notes

* The core trigram model is implemented manually.
* No dedicated n-gram language-modeling library is required.
* The project is intended for **educational and academic purposes**.
* Generated text quality depends heavily on the training corpus and model configuration.

---

## 👨‍💻 Project Purpose

This project was developed as part of an **NLP academic assignment** to gain hands-on understanding of statistical language modeling and probabilistic text generation.
