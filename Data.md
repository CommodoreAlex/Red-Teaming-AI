## Attacking Data Components

The data component of a machine learning (ML) system includes everything related to the data the model uses, from the training data to the data used during inference. Since ML models are highly data-dependent, targeting the data is a viable attack vector. The quality of both the model and its outputs relies heavily on the training data, meaning that even minor data manipulation can have significant consequences. Additionally, if sensitive data such as personally identifiable information (PII) is involved, data leaks can lead to legal ramifications, such as GDPR violations.

### Risks

- **Training Data Quality**: The success of an ML model is highly dependent on the quality of the training data. If the data is biased, incomplete, or not representative of the model's use case, the model's performance will degrade. The impact of low-quality or biased data includes generating harmful, biased, or discriminatory output.

- **Data Poisoning**: Data poisoning attacks involve adversaries manipulating the training data to alter the model's behavior without directly affecting the model's parameters. This attack can result in:
  - Misleading outputs
  - Biased outputs
  - Harmful content generation
  - Subtle backdoor triggers, where specific inputs cause the model to behave maliciously (backdoor attacks).

- **Data Leaks**: With large datasets required to train ML models, there is an inherent risk of data leaks. Attackers may exploit security vulnerabilities to gain unauthorized access to sensitive training or inference data, leading to:
  - Financial and legal consequences
  - Exposing valuable proprietary data
  - Enabling further attacks on the system or its components.
  
### Tactics, Techniques, and Procedures (TTPs)

As discussed, the quality of an ML model is highly dependent on the quality of the training data. Consequently, manipulating training data is a potent attack vector. However, identifying and injecting malicious data into the training set may be difficult depending on factors like how the data is collected, sanitized, and validated. Here are some common TTPs:

1. **Injecting Poisoned Data**: In federated learning systems, where multiple parties contribute to model training, attackers can inject poisoned data or updates during their participation. This can skew the global model without raising suspicion.

2. **Exploiting Data Storage Weaknesses**: Attackers may exploit weak security practices related to the storage and transmission of training data, such as:
   - Poorly configured cloud storage
   - Insufficient encryption at rest or in transit
   - Vulnerable data pipelines
   - Insecure APIs

3. **Supply Chain Attacks**: Attackers may compromise third-party vendors or data providers supplying or curating the training data, gaining access to the data before it reaches the target organization. This can be used to manipulate data or introduce malicious content.

4. **Insider Threats**: Employees or contractors with legitimate access to sensitive data can pose a significant risk. They may be compromised through traditional attack methods such as phishing or social engineering, or they may intentionally exfiltrate data for personal gain or espionage.

