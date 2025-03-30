# OWASP Top 10 Machine Learning Security Risks

Just as OWASP has identified security risks for Web Applications, Web APIs, and Mobile Applications, they have also published a **Top 10** list for **Machine Learning (ML) Security**. This document provides an overview of these key security risks and their implications for ML-based systems.

## OWASP Top 10 for Machine Learning Security

|ID|Risk|Description|
|---|---|---|
|**ML01**|**Input Manipulation Attack**|Attackers modify input data to trigger incorrect or malicious model outputs.|
|**ML02**|**Data Poisoning Attack**|Malicious data is injected into training datasets, compromising model performance or creating backdoors.|
|**ML03**|**Model Inversion Attack**|Attackers attempt to reconstruct sensitive inputs from a model’s outputs.|
|**ML04**|**Membership Inference Attack**|Attackers analyze model behavior to determine if specific data was included in training, potentially leaking sensitive information.|
|**ML05**|**Model Theft**|Adversaries extract a model’s functionality by training a separate model on its outputs, stealing intellectual property.|
|**ML06**|**AI Supply Chain Attacks**|Vulnerabilities in the ML supply chain—data sources, libraries, or pre-trained models—are exploited to compromise security.|
|**ML07**|**Transfer Learning Attack**|Manipulating a pre-trained model before fine-tuning can introduce biases or backdoors into the final model.|
|**ML08**|**Model Skewing**|Attackers intentionally bias training data to influence the model’s behavior for malicious purposes.|
|**ML09**|**Output Integrity Attack**|Attackers intercept and modify model outputs before they are processed, altering the perceived decision of the model.|
|**ML10**|**Model Poisoning**|Direct manipulation of model parameters to compromise performance or introduce malicious behavior.|

---

## Deep Dive into OWASP ML Security Risks

### ML01: Input Manipulation Attack

**Description:** Input manipulation attacks exploit weaknesses in an ML model by altering its input data. These attacks typically aim to trigger incorrect or unintended behavior while maintaining an appearance of legitimacy.

**Example:** A self-driving car using an ML-based image classification system could be deceived by adversarial perturbations on a stop sign (e.g., small stickers or dirt). These minor modifications, imperceptible to human eyes, could cause the model to misclassify the sign—potentially leading to dangerous consequences.

### ML02: Data Poisoning Attack

**Description:** Data poisoning occurs when attackers inject malicious or misleading data into an ML model’s training dataset, corrupting the model’s performance or embedding backdoors.

**Example:** An adversary alters training data for an antivirus ML model, labeling certain malware samples as benign. The resulting model is unable to detect those specific malware samples post-training.

### ML03: Model Inversion Attack

**Description:** In a model inversion attack, an adversary trains a secondary model to reconstruct inputs from the target model’s outputs, extracting sensitive data.

**Example:** A model trained for medical diagnosis could inadvertently leak patient health information when attacked using model inversion techniques.

### ML04: Membership Inference Attack

**Description:** This attack allows an adversary to determine whether a particular data sample was part of the training dataset by analyzing the model’s confidence scores.

**Example:** If an ML model was trained on sensitive financial transactions, an attacker might infer whether a specific transaction was in the training data, leading to privacy breaches.

### ML05: Model Theft

**Description:** Model theft (or model extraction) occurs when an attacker queries an ML model multiple times and trains a replica with similar decision boundaries.

**Example:** A competitor reverse-engineers a proprietary fraud detection model by querying it extensively and using the outputs to train their own version, bypassing the need for expensive R&D.

### ML06: AI Supply Chain Attacks

**Description:** ML systems rely on numerous external dependencies, such as open-source libraries, datasets, and pre-trained models. Attackers exploit vulnerabilities in any part of this supply chain to introduce security risks.

**Example:** A malicious actor injects a backdoor into an open-source deep learning library. Any model trained with this compromised library inherits the vulnerability.

### ML07: Transfer Learning Attack

**Description:** Transfer learning attacks occur when adversaries manipulate a base model that is later fine-tuned by third parties, propagating hidden biases or backdoors.

**Example:** A malicious pre-trained language model could subtly insert misinformation into text summarization applications, skewing results based on specific keywords.

### ML08: Model Skewing

**Description:** In model skewing attacks, adversaries introduce biases or misleading patterns into training data to distort the model’s decision-making process.

**Example:** A financial fraud detection model is poisoned with fraudulent transactions labeled as legitimate, allowing future fraudulent transactions to pass undetected.

### ML09: Output Integrity Attack

**Description:** These attacks manipulate an ML model’s output before it reaches the intended system, altering its perceived behavior.

**Example:** An attacker intercepts and modifies the outputs of a malware classification model, making malicious software appear benign to security systems.

### ML10: Model Poisoning

**Description:** Unlike data poisoning, which targets training data, model poisoning directly modifies the model’s internal parameters, requiring privileged access.

**Example:** An attacker with internal access modifies a recommendation algorithm to unfairly promote certain products, misleading users for financial gain.

---

## Conclusion

Machine Learning models are vulnerable to a range of security threats, from adversarial input manipulation to sophisticated supply chain compromises. As ML adoption increases, it is crucial to integrate robust security practices into the entire lifecycle of ML development and deployment.

### Mitigation Strategies

To reduce ML security risks, organizations should consider:
- **Adversarial Testing:** Evaluating models with adversarial inputs.
- **Robust Training Data Curation:** Preventing data poisoning by using trusted sources.
- **Model Output Filtering:** Detecting and mitigating output integrity attacks.
- **Access Control & Monitoring:** Restricting access to ML models and monitoring suspicious queries.
- **Supply Chain Security:** Vetting third-party data, pre-trained models, and dependencies for potential risks.

By proactively addressing these challenges, organizations can build more secure and resilient ML systems.

---

### References

- [OWASP Top 10 for Machine Learning Security](https://owasp.org/www-project-machine-learning-security-top-10/)
- Research papers on adversarial ML, data poisoning, and model extraction attacks.
