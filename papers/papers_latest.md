# Daily Paper Updates

Last updated: 2026-04-03

---

## 📊 Summary

Total papers found: **13**

---

## 🎯 LLM Quantization (12)

### 1. Batched Contextual Reinforcement: A Task-Scaling Law for Efficient Reasoning

- **Authors**: Bangji Yang, Hongbo Ma, Jiajun Fan, Ge Liu
- **Category**: `cs.LG`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02322v1](http://arxiv.org/abs/2604.02322v1)
- **PDF**: [https://arxiv.org/pdf/2604.02322v1.pdf](https://arxiv.org/pdf/2604.02322v1.pdf)
- **Abstract**: Large Language Models employing Chain-of-Thought reasoning achieve strong performance but suffer from excessive token consumption that inflates inference costs. Existing efficiency methods such as explicit length penalties, difficulty estimators, or multi-stage curricula either degrade reasoning quality or require complex training pipelines. We introduce Batched Contextual Reinforcement, a minimalist, single-stage training paradigm that unlocks efficient reasoning through a simple structural mod...

---

### 2. Taming the Exponential: A Fast Softmax Surrogate for Integer-Native Edge Inference

- **Authors**: Dimitrios Danopoulos, Enrico Lupi, Michael Kagan, Maurizio Pierini
- **Category**: `cs.LG`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02292v1](http://arxiv.org/abs/2604.02292v1)
- **PDF**: [https://arxiv.org/pdf/2604.02292v1.pdf](https://arxiv.org/pdf/2604.02292v1.pdf)
- **Abstract**: Softmax can become a computational bottleneck in the Transformer model's Multi-Head Attention (MHA) block, particularly in small models under low-precision inference, where exponentiation and normalization incur significant overhead. As such, we suggest using Head-Calibrated Clipped-Linear Softmax (HCCS), a bounded, monotone surrogate to the exponential softmax function, which uses a clipped linear mapping of the max centered attention logits. This approximation produces a stable probability dis...

---

### 3. Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing

- **Authors**: Gengsheng Li, Tianyu Yang, Junfeng Fang, Mingyang Song, Mao Zheng
- **Category**: `cs.LG`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02288v1](http://arxiv.org/abs/2604.02288v1)
- **PDF**: [https://arxiv.org/pdf/2604.02288v1.pdf](https://arxiv.org/pdf/2604.02288v1.pdf)
- **Abstract**: Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training large language models. While Group Relative Policy Optimization (GRPO) is widely adopted, its coarse credit assignment uniformly penalizes failed rollouts, lacking the token-level focus needed to efficiently address specific deviations. Self-Distillation Policy Optimization (SDPO) addresses this by providing denser, more targeted logit-level supervision that facilitates rapid early improvement,...

---

### 4. De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules

- **Authors**: Keerat Guliani, Deepkamal Gill, David Landsman, Nima Eshraghi, Krishna Kumar
- **Category**: `cs.LG`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02276v1](http://arxiv.org/abs/2604.02276v1)
- **PDF**: [https://arxiv.org/pdf/2604.02276v1.pdf](https://arxiv.org/pdf/2604.02276v1.pdf)
- **Abstract**: Regulatory documents encode legally binding obligations that LLM-based systems must respect. Yet converting dense, hierarchically structured legal text into machine-readable rules remains a costly, expert-intensive process. We present De Jure, a fully automated, domain-agnostic pipeline for extracting structured regulatory rules from raw documents, requiring no human annotation, domain-specific prompting, or annotated gold data. De Jure operates through four sequential stages: normalization of s...

---

### 5. SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization

- **Authors**: Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Chengcheng Han, Qi Gu
- **Category**: `cs.LG`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02268v1](http://arxiv.org/abs/2604.02268v1)
- **PDF**: [https://arxiv.org/pdf/2604.02268v1.pdf](https://arxiv.org/pdf/2604.02268v1.pdf)
- **Abstract**: Agent skills, structured packages of procedural knowledge and executable resources that agents dynamically load at inference time, have become a reliable mechanism for augmenting LLM agents. Yet inference-time skill augmentation is fundamentally limited: retrieval noise introduces irrelevant guidance, injected skill content imposes substantial token overhead, and the model never truly acquires the knowledge it merely follows. We ask whether skills can instead be internalized into model parameter...

---

### 6. BVFLMSP : Bayesian Vertical Federated Learning for Multimodal Survival with Privacy

- **Authors**: Abhilash Kar, Basisth Saha, Tanmay Sen, Biswabrata Pradhan
- **Category**: `cs.LG`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02248v1](http://arxiv.org/abs/2604.02248v1)
- **PDF**: [https://arxiv.org/pdf/2604.02248v1.pdf](https://arxiv.org/pdf/2604.02248v1.pdf)
- **Abstract**: Multimodal time-to-event prediction often requires integrating sensitive data distributed across multiple parties, making centralized model training impractical due to privacy constraints. At the same time, most existing multimodal survival models produce single deterministic predictions without indicating how confident the model is in its estimates, which can limit their reliability in real-world decision making. To address these challenges, we propose BVFLMSP, a Bayesian Vertical Federated Lea...

---

### 7. The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expert Level

- **Authors**: Jeremy Herbst, Jae Hee Lee, Stefan Wermter
- **Category**: `cs.LG`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02178v1](http://arxiv.org/abs/2604.02178v1)
- **PDF**: [https://arxiv.org/pdf/2604.02178v1.pdf](https://arxiv.org/pdf/2604.02178v1.pdf)
- **Abstract**: Mixture-of-Experts (MoE) architectures have become the dominant choice for scaling Large Language Models (LLMs), activating only a subset of parameters per token. While MoE architectures are primarily adopted for computational efficiency, it remains an open question whether their sparsity makes them inherently easier to interpret than dense feed-forward networks (FFNs). We compare MoE experts and dense FFNs using $k$-sparse probing and find that expert neurons are consistently less polysemantic,...

---

### 8. AstroConcepts: A Large-Scale Multi-Label Classification Corpus for Astrophysics

- **Authors**: Atilla Kaan Alkan, Felix Grezes, Sergi Blanco-Cuaresma, Jennifer Lynn Bartlett, Daniel Chivvis
- **Category**: `cs.LG`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02156v1](http://arxiv.org/abs/2604.02156v1)
- **PDF**: [https://arxiv.org/pdf/2604.02156v1.pdf](https://arxiv.org/pdf/2604.02156v1.pdf)
- **Abstract**: Scientific multi-label text classification suffers from extreme class imbalance, where specialized terminology exhibits severe power-law distributions that challenge standard classification approaches. Existing scientific corpora lack comprehensive controlled vocabularies, focusing instead on broad categories and limiting systematic study of extreme imbalance. We introduce AstroConcepts, a corpus of English abstracts from 21,702 published astrophysics papers, labeled with 2,367 concepts from the...

---

### 9. BVFLMSP : Bayesian Vertical Federated Learning for Multimodal Survival with Privacy

- **Authors**: Abhilash Kar, Basisth Saha, Tanmay Sen, Biswabrata Pradhan
- **Category**: `stat.ML`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02248v1](http://arxiv.org/abs/2604.02248v1)
- **PDF**: [https://arxiv.org/pdf/2604.02248v1.pdf](https://arxiv.org/pdf/2604.02248v1.pdf)
- **Abstract**: Multimodal time-to-event prediction often requires integrating sensitive data distributed across multiple parties, making centralized model training impractical due to privacy constraints. At the same time, most existing multimodal survival models produce single deterministic predictions without indicating how confident the model is in its estimates, which can limit their reliability in real-world decision making. To address these challenges, we propose BVFLMSP, a Bayesian Vertical Federated Lea...

---

### 10. Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning

- **Authors**: Xueying Li, Feng Lyu, Hao Wu, Mingliu Liu, Jia-Nan Liu
- **Category**: `cs.RO`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02318v1](http://arxiv.org/abs/2604.02318v1)
- **PDF**: [https://arxiv.org/pdf/2604.02318v1.pdf](https://arxiv.org/pdf/2604.02318v1.pdf)
- **Abstract**: Training-free Vision-Language Navigation (VLN) agents powered by foundation models can follow instructions and explore 3D environments. However, existing approaches rely on greedy frontier selection and passive spatial memory, leading to inefficient behaviors such as local oscillation and redundant revisiting. We argue that this stems from a lack of metacognitive capabilities: the agent cannot monitor its exploration progress, diagnose strategy failures, or adapt accordingly. To address this, we...

---

### 11. UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models

- **Authors**: Qiyao Zhang, Shuhua Zheng, Jianli Sun, Chengxiang Li, Xianke Wu
- **Category**: `cs.RO`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02241v1](http://arxiv.org/abs/2604.02241v1)
- **PDF**: [https://arxiv.org/pdf/2604.02241v1.pdf](https://arxiv.org/pdf/2604.02241v1.pdf)
- **Abstract**: Embodied visual tracking is crucial for Unmanned Aerial Vehicles (UAVs) executing complex real-world tasks. In dynamic urban scenarios with complex semantic requirements, Vision-Language-Action (VLA) models show great promise due to their cross-modal fusion and continuous action generation capabilities. To benchmark multimodal tracking in such environments, we construct a dedicated evaluation benchmark and a large-scale dataset encompassing over 890K frames, 176 tasks, and 85 diverse objects. Fu...

---

### 12. UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving

- **Authors**: Yongkang Li, Lijun Zhou, Sixu Yan, Bencheng Liao, Tianyi Yan
- **Category**: `cs.RO`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02190v1](http://arxiv.org/abs/2604.02190v1)
- **PDF**: [https://arxiv.org/pdf/2604.02190v1.pdf](https://arxiv.org/pdf/2604.02190v1.pdf)
- **Abstract**: Vision-Language-Action (VLA) models have recently emerged in autonomous driving, with the promise of leveraging rich world knowledge to improve the cognitive capabilities of driving systems. However, adapting such models for driving tasks currently faces a critical dilemma between spatial perception and semantic reasoning. Consequently, existing VLA systems are forced into suboptimal compromises: directly adopting 2D Vision-Language Models yields limited spatial perception, whereas enhancing the...

---


## 🚁 UAV Vision (1)

### 1. PRO-SPECT: Probabilistically Safe Scalable Planning for Energy-Aware Coordinated UAV-UGV Teams in Stochastic Environments

- **Authors**: Roger Fowler, Cahit Ikbal Er, Benjamin Johnsenberg, Yasin Yazicioglu
- **Category**: `cs.RO`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02142v1](http://arxiv.org/abs/2604.02142v1)
- **PDF**: [https://arxiv.org/pdf/2604.02142v1.pdf](https://arxiv.org/pdf/2604.02142v1.pdf)
- **Abstract**: We consider energy-aware planning for an unmanned aerial vehicle (UAV) and unmanned ground vehicle (UGV) team operating in a stochastic environment. The UAV must visit a set of air points in minimum time while respecting energy constraints, relying on the UGV as a mobile charging station. Unlike prior work that assumed deterministic travel times or used fixed robustness margins, we model travel times as random variables and bound the probability of failure (energy depletion) across the entire mi...

---



---

## 🔍 How to Use This

- **Browse**: Click on any paper title to view details
- **Download**: Click on PDF to download the paper
- **Categorize**: Papers are organized by research direction

## 📚 Research Directions

- **🎯 LLM Quantization**: Large language model and multimodal quantization techniques
- **📱 Edge Deployment**: On-device inference, model optimization, lightweight models
- **🚁 UAV Vision**: Drone/UAV video tracking, object detection, aerial imaging

---

*Generated automatically by Paper Pusher*
