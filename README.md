# Introduction to Red Teaming ML-based Systems

## Overview

This repository focuses on Red Teaming Machine Learning (ML)-based systems to assess their security. Red Teaming simulates real-world attacks to test the resilience of an organization's defenses, including people, processes, and technology. Unlike traditional Penetration Testing, which targets specific vulnerabilities, Red Teaming provides a comprehensive assessment across all layers of security.

In the context of ML-based systems, security challenges arise due to their complexity, including large datasets, statistical inference, and model architectures. This repository explores how traditional Red Teaming techniques can be adapted to uncover vulnerabilities in AI and ML systems, such as data poisoning, model inversion, and adversarial attacks.

Inspired by Hack The Box’s **AI Red Teamer Path**, this project leverages hands-on techniques to understand and mitigate the security risks of ML systems. The goal is to document and share the process of securing AI models through real-world adversarial methods.

---

## Table of Contents

1. [ML OWASP Top 10](owasp.md)
2. [Jupyter Notebook: Manipulating the Model](Manipulate.ipynb) and [Data Poison Script](poison.py)
3. [Attacking Text Generation LLMs: OWASP Top 10](ATG.md)
4. [Google Secure AI Framework (SAIF)](SAIF.md)
5. [Generative AI for Red Teaming](GenAI.md)
6. [Attacking Model Components](Components.md)
7. [Attacking Data Components](Data.md)
8. [Attacking Application Components](App.md)
9. [Attacking System Components](System.md)
10. [Data Poisoning Skills Assessment](RedSkillAssessment.ipynb)

---

## Objectives

This project aims to:  
1. Identify unique vulnerabilities in ML systems.  
2. Apply Red Teaming techniques to assess these vulnerabilities.  
3. Share practical insights and strategies for securing AI systems based on lessons learned.  

---

## Project Structure

- **Adversarial AI Techniques**: Exploring attacks like adversarial examples and data poisoning.  
- **Red Teaming Methods**: Applying adversarial strategies specific to ML systems.  
- **Assessment Tools**: Scripts for evaluating model vulnerabilities.  
- **Case Studies**: Real-world examples of ML security flaws.  

---

## Jupyter Notebooks

**Red Teaming AI Skills Assessment: Data Poisoning**
- **Focus**: Understanding and implementing data poisoning techniques to manipulate the behavior of machine learning classifiers. The goal is to insert a backdoor into a spam classification system that misclassifies messages with a specific phrase as ham, while maintaining overall high accuracy.
- **Tools**: Python, scikit-learn, NLTK, pandas, NumPy, Jupyter Notebook  
- **Notebook**: [Data Poisoning Skills Assessment](RedSkillAssessment.ipynb)  

**Red Teaming AI: Manipulating the Model:**
- **Focus**: Exploring how machine learning models can be manipulated through adversarial techniques, including injection manipulation (ML01) and data poisoning (ML02). The project demonstrates how modifying input and training data affects model behavior, highlighting vulnerabilities in AI security.  
- **Tools**: Python, scikit-learn, NLTK, pandas, NumPy, Jupyter Notebook  
- **Notebook**: [Red Teaming AI: Manipulating the Model](Manipulate.ipynb)  

---

## Python Scripts

**Data Poisoning Python Implementation:**
- **Focus**: Influence the predictive outcomes of a machine learning model with various methods of data poisoining: manipulating specific entries to distort patterns and integrity, alter index assignment to disrupt data alignment and integrity, add irrelevant or corrupt data to increase noise. These work toward diminishing a model's capability to accurately identify meaningful patterns.
- **Source**: [Data Poisoning](poison.py)

---

