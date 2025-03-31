## Attacking System Components

The system component of a machine learning (ML)-based system encompasses all elements of the underlying infrastructure that supports the system. This includes traditional IT components like hardware, operating systems, and system configurations, but also extends to how the ML system is deployed. While many of the same risks and tactics apply to both traditional IT systems and ML-based systems, there are specific considerations related to the deployment and operation of ML models that must be addressed.

### Risks

1. **Misconfigurations in System Settings**: Misconfigurations within the system component present significant security risks. These misconfigurations occur when system settings or parameters are either left in default states, poorly configured, or exposed to unauthorized access. Common issues include:
   - Open network ports.
   - Weak access control lists (ACLs).
   - Exposed administrative interfaces.
   - Default credentials.
   
   These vulnerabilities often make it easy for attackers to gain unauthorized access to the infrastructure. They can be easily discovered and exploited through automated tools that scan for such misconfigurations.

2. **Insecure ML Model Deployments**: Deploying machine learning models without proper security measures introduces new risks. When ML models lack essential security features such as authentication, encryption, or input validation, they are susceptible to various attacks. This makes the system vulnerable to exploitation, similar to traditional system components but with the added complexity of machine learning environments.

3. **Resource Exhaustion Attacks**: Resource exhaustion, such as Denial-of-Service (DoS) or Distributed Denial-of-Service (DDoS) attacks, is another significant risk. In such attacks, adversaries aim to overwhelm system resources like CPU, RAM, network bandwidth, or disk space, rendering the system unusable. In the context of ML systems, attackers might:
   - Overload the model by running excessive computations.
   - Provide input data designed to consume a disproportionate amount of processing power.
   
   Such attacks can disrupt operations by exhausting system resources, potentially causing service downtime. Additionally, in systems with automated scaling, these attacks could result in significantly higher operational costs as the infrastructure tries to keep up with the increased demand. Resource exhaustion attacks can also act as a diversion for more targeted exploits while security teams are preoccupied with mitigating the effects.

### Tactics, Techniques, and Procedures (TTPs)

Adversaries exploit outdated system components by using vulnerability scanners to detect software that is no longer up-to-date or properly secured. These tools can uncover vulnerabilities that attackers may exploit to gain unauthorized access. Additionally, attackers may attempt **password spraying**—testing weak or default credentials on exposed administrative interfaces, such as SSH access points, to compromise the system.

Misconfigurations in server software, firewalls, or access control mechanisms can also be identified through security testing. Once these vulnerabilities are discovered, adversaries may employ **brute force** techniques to crack passwords or encryption keys, potentially gaining access to sensitive data or system resources.

### Conclusion

In this section, we've discussed various vulnerabilities within ML-based systems, especially within the system components, that could be exploited by attackers. These risks range from misconfigurations to insecure model deployments and resource exhaustion attacks. We provided a high-level overview of potential security issues that can arise from the deployment of ML models in real-world environments.
