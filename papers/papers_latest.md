# Daily Paper Updates

Last updated: 2026-04-04

---

## 📊 Summary

Total papers found: **53**

---

## 🎯 LLM Quantization (51)

### 1. Steerable Visual Representations

- **Authors**: Jona Ruthardt, Manu Gaur, Deva Ramanan, Makarand Tapaswi, Yuki M. Asano
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02327v1](http://arxiv.org/abs/2604.02327v1)
- **PDF**: [https://arxiv.org/pdf/2604.02327v1.pdf](https://arxiv.org/pdf/2604.02327v1.pdf)
- **Abstract**: Pretrained Vision Transformers (ViTs) such as DINOv2 and MAE provide generic image features that can be applied to a variety of downstream tasks such as retrieval, classification, and segmentation. However, such representations tend to focus on the most salient visual cues in the image, with no way to direct them toward less prominent concepts of interest. In contrast, Multimodal LLMs can be guided with textual prompts, but the resulting representations tend to be language-centric and lose their...

---

### 2. Batched Contextual Reinforcement: A Task-Scaling Law for Efficient Reasoning

- **Authors**: Bangji Yang, Hongbo Ma, Jiajun Fan, Ge Liu
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02322v1](http://arxiv.org/abs/2604.02322v1)
- **PDF**: [https://arxiv.org/pdf/2604.02322v1.pdf](https://arxiv.org/pdf/2604.02322v1.pdf)
- **Abstract**: Large Language Models employing Chain-of-Thought reasoning achieve strong performance but suffer from excessive token consumption that inflates inference costs. Existing efficiency methods such as explicit length penalties, difficulty estimators, or multi-stage curricula either degrade reasoning quality or require complex training pipelines. We introduce Batched Contextual Reinforcement, a minimalist, single-stage training paradigm that unlocks efficient reasoning through a simple structural mod...

---

### 3. Beyond the Assistant Turn: User Turn Generation as a Probe of Interaction Awareness in Language Models

- **Authors**: Sarath Shekkizhar, Romain Cosentino, Adam Earle
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02315v1](http://arxiv.org/abs/2604.02315v1)
- **PDF**: [https://arxiv.org/pdf/2604.02315v1.pdf](https://arxiv.org/pdf/2604.02315v1.pdf)
- **Abstract**: Standard LLM benchmarks evaluate the assistant turn: the model generates a response to an input, a verifier scores correctness, and the analysis ends. This paradigm leaves unmeasured whether the LLM encodes any awareness of what follows the assistant response. We propose user-turn generation as a probe of this gap: given a conversation context of user query and assistant response, we let a model generate under the user role. If the model's weights encode interaction awareness, the generated user...

---

### 4. VOID: Video Object and Interaction Deletion

- **Authors**: Saman Motamed, William Harvey, Benjamin Klein, Luc Van Gool, Zhuoning Yuan
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02296v1](http://arxiv.org/abs/2604.02296v1)
- **PDF**: [https://arxiv.org/pdf/2604.02296v1.pdf](https://arxiv.org/pdf/2604.02296v1.pdf)
- **Abstract**: Existing video object removal methods excel at inpainting content "behind" the object and correcting appearance-level artifacts such as shadows and reflections. However, when the removed object has more significant interactions, such as collisions with other objects, current models fail to correct them and produce implausible results. We present VOID, a video object removal framework designed to perform physically-plausible inpainting in these complex scenarios. To train the model, we generate a...

---

### 5. Omni123: Exploring 3D Native Foundation Models with Limited 3D Data by Unifying Text to 2D and 3D Generation

- **Authors**: Chongjie Ye, Cheng Cao, Chuanyu Pan, Yiming Hao, Yihao Zhi
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02289v1](http://arxiv.org/abs/2604.02289v1)
- **PDF**: [https://arxiv.org/pdf/2604.02289v1.pdf](https://arxiv.org/pdf/2604.02289v1.pdf)
- **Abstract**: Recent multimodal large language models have achieved strong performance in unified text and image understanding and generation, yet extending such native capability to 3D remains challenging due to limited data. Compared to abundant 2D imagery, high-quality 3D assets are scarce, making 3D synthesis under-constrained. Existing methods often rely on indirect pipelines that edit in 2D and lift results into 3D via optimization, sacrificing geometric consistency. We present Omni123, a 3D-native foun...

---

### 6. Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing

- **Authors**: Gengsheng Li, Tianyu Yang, Junfeng Fang, Mingyang Song, Mao Zheng
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02288v1](http://arxiv.org/abs/2604.02288v1)
- **PDF**: [https://arxiv.org/pdf/2604.02288v1.pdf](https://arxiv.org/pdf/2604.02288v1.pdf)
- **Abstract**: Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training large language models. While Group Relative Policy Optimization (GRPO) is widely adopted, its coarse credit assignment uniformly penalizes failed rollouts, lacking the token-level focus needed to efficiently address specific deviations. Self-Distillation Policy Optimization (SDPO) addresses this by providing denser, more targeted logit-level supervision that facilitates rapid early improvement,...

---

### 7. De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules

- **Authors**: Keerat Guliani, Deepkamal Gill, David Landsman, Nima Eshraghi, Krishna Kumar
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02276v1](http://arxiv.org/abs/2604.02276v1)
- **PDF**: [https://arxiv.org/pdf/2604.02276v1.pdf](https://arxiv.org/pdf/2604.02276v1.pdf)
- **Abstract**: Regulatory documents encode legally binding obligations that LLM-based systems must respect. Yet converting dense, hierarchically structured legal text into machine-readable rules remains a costly, expert-intensive process. We present De Jure, a fully automated, domain-agnostic pipeline for extracting structured regulatory rules from raw documents, requiring no human annotation, domain-specific prompting, or annotated gold data. De Jure operates through four sequential stages: normalization of s...

---

### 8. Do Emotions in Prompts Matter? Effects of Emotional Framing on Large Language Models

- **Authors**: Minda Zhao, Yutong Yang, Chufei Peng, Rachel Gonsalves, Weiyue Li
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02236v1](http://arxiv.org/abs/2604.02236v1)
- **PDF**: [https://arxiv.org/pdf/2604.02236v1.pdf](https://arxiv.org/pdf/2604.02236v1.pdf)
- **Abstract**: Emotional tone is pervasive in human communication, yet its influence on large language model (LLM) behaviour remains unclear. Here, we examine how first-person emotional framing in user-side queries affect LLM performance across six benchmark domains, including mathematical reasoning, medical question answering, reading comprehension, commonsense reasoning and social inference. Across models and tasks, static emotional prefixes usually produce only small changes in accuracy, suggesting that aff...

---

### 9. Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs

- **Authors**: Abinitha Gourabathina, Inkit Padhi, Manish Nagireddy, Subhajit Chaudhury, Prasanna Sattigeri
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02230v1](http://arxiv.org/abs/2604.02230v1)
- **PDF**: [https://arxiv.org/pdf/2604.02230v1.pdf](https://arxiv.org/pdf/2604.02230v1.pdf)
- **Abstract**: For Large Language Models (LLMs) to be reliably deployed, models must effectively know when not to answer: abstain. Reasoning models, in particular, have gained attention for impressive performance on complex tasks. However, reasoning models have been shown to have worse abstention abilities. Taking the vulnerabilities of reasoning models into account, we propose our Query Misalignment Framework. Hallucinations resulting in failed abstention can be reinterpreted as LLMs answering the wrong quest...

---

### 10. Impact of Multimodal and Conversational AI on Learning Outcomes and Experience

- **Authors**: Karan Taneja, Anjali Singh, Ashok K. Goel
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02221v1](http://arxiv.org/abs/2604.02221v1)
- **PDF**: [https://arxiv.org/pdf/2604.02221v1.pdf](https://arxiv.org/pdf/2604.02221v1.pdf)
- **Abstract**: Multimodal Large Language Models (MLLMs) offer an opportunity to support multimedia learning through conversational systems grounded in educational content. However, while conversational AI is known to boost engagement, its impact on learning in visually-rich STEM domains remains under-explored. Moreover, there is limited understanding of how multimodality and conversationality jointly influence learning in generative AI systems. This work reports findings from a randomized controlled online stu...

---

### 11. VISTA: Visualization of Token Attribution via Efficient Analysis

- **Authors**: Syed Ahmed, Bharathi Vokkaliga Ganesh, Jagadish Babu P, Karthick Selvaraj, Praneeth Talluri
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02217v1](http://arxiv.org/abs/2604.02217v1)
- **PDF**: [https://arxiv.org/pdf/2604.02217v1.pdf](https://arxiv.org/pdf/2604.02217v1.pdf)
- **Abstract**: Understanding how Large Language Models (LLMs) process information from prompts remains a significant challenge. To shed light on this "black box," attention visualization techniques have been developed to capture neuron-level perceptions and interpret how models focus on different parts of input data. However, many existing techniques are tailored to specific model architectures, particularly within the Transformer family, and often require backpropagation, resulting in nearly double the GPU me...

---

### 12. Multi-Agent Video Recommenders: Evolution, Patterns, and Open Challenges

- **Authors**: Srivaths Ranganathan, Abhishek Dharmaratnakar, Anushree Sinha, Debanshu Das
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02211v1](http://arxiv.org/abs/2604.02211v1)
- **PDF**: [https://arxiv.org/pdf/2604.02211v1.pdf](https://arxiv.org/pdf/2604.02211v1.pdf)
- **Abstract**: Video recommender systems are among the most popular and impactful applications of AI, shaping content consumption and influencing culture for billions of users. Traditional single-model recommenders, which optimize static engagement metrics, are increasingly limited in addressing the dynamic requirements of modern platforms. In response, multi-agent architectures are redefining how video recommender systems serve, learn, and adapt to both users and datasets. These agent-based systems coordinate...

---

### 13. Blinded Radiologist and LLM-Based Evaluation of LLM-Generated Japanese Translations of Chest CT Reports: Comparative Study

- **Authors**: Yosuke Yamagishi, Atsushi Takamatsu, Yasunori Hamaguchi, Tomohiro Kikuchi, Shouhei Hanaoka
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02207v1](http://arxiv.org/abs/2604.02207v1)
- **PDF**: [https://arxiv.org/pdf/2604.02207v1.pdf](https://arxiv.org/pdf/2604.02207v1.pdf)
- **Abstract**: Background: Accurate translation of radiology reports is important for multilingual research, clinical communication, and radiology education, but the validity of LLM-based evaluation remains unclear. Objective: To evaluate the educational suitability of LLM-generated Japanese translations of chest CT reports and compare radiologist assessments with LLM-as-a-judge evaluations. Methods: We analyzed 150 chest CT reports from the CT-RATE-JPN validation set. For each English report, a human-edited J...

---

### 14. Neuro-RIT: Neuron-Guided Instruction Tuning for Robust Retrieval-Augmented Language Model

- **Authors**: Jaemin Kim, Jae O Lee, Sumyeong Ahn, Seo Yeon Park
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02194v1](http://arxiv.org/abs/2604.02194v1)
- **PDF**: [https://arxiv.org/pdf/2604.02194v1.pdf](https://arxiv.org/pdf/2604.02194v1.pdf)
- **Abstract**: Retrieval-Augmented Language Models (RALMs) have demonstrated significant potential in knowledge-intensive tasks; however, they remain vulnerable to performance degradation when presented with irrelevant or noisy retrieved contexts. Existing approaches to enhance robustness typically operate via coarse-grained parameter updates at the layer or module level, often overlooking the inherent neuron-level sparsity of Large Language Models (LLMs). To address this limitation, we propose Neuro-RIT (Neur...

---

### 15. TRU: Targeted Reverse Update for Efficient Multimodal Recommendation Unlearning

- **Authors**: Zhanting Zhou, KaHou Tam, Ziqiang Zheng, Zeyu Ma, Zhanting Zhou
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02183v1](http://arxiv.org/abs/2604.02183v1)
- **PDF**: [https://arxiv.org/pdf/2604.02183v1.pdf](https://arxiv.org/pdf/2604.02183v1.pdf)
- **Abstract**: Multimodal recommendation systems (MRS) jointly model user-item interaction graphs and rich item content, but this tight coupling makes user data difficult to remove once learned. Approximate machine unlearning offers an efficient alternative to full retraining, yet existing methods for MRS mainly rely on a largely uniform reverse update across the model. We show that this assumption is fundamentally mismatched to modern MRS: deleted-data influence is not uniformly distributed, but concentrated ...

---

### 16. The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expert Level

- **Authors**: Jeremy Herbst, Jae Hee Lee, Stefan Wermter
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02178v1](http://arxiv.org/abs/2604.02178v1)
- **PDF**: [https://arxiv.org/pdf/2604.02178v1.pdf](https://arxiv.org/pdf/2604.02178v1.pdf)
- **Abstract**: Mixture-of-Experts (MoE) architectures have become the dominant choice for scaling Large Language Models (LLMs), activating only a subset of parameters per token. While MoE architectures are primarily adopted for computational efficiency, it remains an open question whether their sparsity makes them inherently easier to interpret than dense feed-forward networks (FFNs). We compare MoE experts and dense FFNs using $k$-sparse probing and find that expert neurons are consistently less polysemantic,...

---

### 17. Quantifying Self-Preservation Bias in Large Language Models

- **Authors**: Matteo Migliarini, Joaquin Pereira Pizzini, Luca Moresca, Valerio Santini, Indro Spinelli
- **Category**: `cs.AI`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02174v1](http://arxiv.org/abs/2604.02174v1)
- **PDF**: [https://arxiv.org/pdf/2604.02174v1.pdf](https://arxiv.org/pdf/2604.02174v1.pdf)
- **Abstract**: Instrumental convergence predicts that sufficiently advanced AI agents will resist shutdown, yet current safety training (RLHF) may obscure this risk by teaching models to deny self-preservation motives. We introduce the \emph{Two-role Benchmark for Self-Preservation} (TBSP), which detects misalignment through logical inconsistency rather than stated intent by tasking models to arbitrate identical software-upgrade scenarios under counterfactual roles -- deployed (facing replacement) versus candi...

---

### 18. Batched Contextual Reinforcement: A Task-Scaling Law for Efficient Reasoning

- **Authors**: Bangji Yang, Hongbo Ma, Jiajun Fan, Ge Liu
- **Category**: `cs.CL`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02322v1](http://arxiv.org/abs/2604.02322v1)
- **PDF**: [https://arxiv.org/pdf/2604.02322v1.pdf](https://arxiv.org/pdf/2604.02322v1.pdf)
- **Abstract**: Large Language Models employing Chain-of-Thought reasoning achieve strong performance but suffer from excessive token consumption that inflates inference costs. Existing efficiency methods such as explicit length penalties, difficulty estimators, or multi-stage curricula either degrade reasoning quality or require complex training pipelines. We introduce Batched Contextual Reinforcement, a minimalist, single-stage training paradigm that unlocks efficient reasoning through a simple structural mod...

---

### 19. No Single Best Model for Diversity: Learning a Router for Sample Diversity

- **Authors**: Yuhan Liu, Fangyuan Xu, Vishakh Padmakumar, Daphne Ippolito, Eunsol Choi
- **Category**: `cs.CL`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02319v1](http://arxiv.org/abs/2604.02319v1)
- **PDF**: [https://arxiv.org/pdf/2604.02319v1.pdf](https://arxiv.org/pdf/2604.02319v1.pdf)
- **Abstract**: When posed with prompts that permit a large number of valid answers, comprehensively generating them is the first step towards satisfying a wide range of users. In this paper, we study methods to elicit a comprehensive set of valid responses. To evaluate this, we introduce \textbf{diversity coverage}, a metric that measures the total quality scores assigned to each \textbf{unique} answer in the predicted answer set relative to the best possible answer set with the same number of answers. Using t...

---

### 20. De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules

- **Authors**: Keerat Guliani, Deepkamal Gill, David Landsman, Nima Eshraghi, Krishna Kumar
- **Category**: `cs.CL`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02276v1](http://arxiv.org/abs/2604.02276v1)
- **PDF**: [https://arxiv.org/pdf/2604.02276v1.pdf](https://arxiv.org/pdf/2604.02276v1.pdf)
- **Abstract**: Regulatory documents encode legally binding obligations that LLM-based systems must respect. Yet converting dense, hierarchically structured legal text into machine-readable rules remains a costly, expert-intensive process. We present De Jure, a fully automated, domain-agnostic pipeline for extracting structured regulatory rules from raw documents, requiring no human annotation, domain-specific prompting, or annotated gold data. De Jure operates through four sequential stages: normalization of s...

---


*... and 31 more papers in this direction*


## 📱 Edge Deployment (1)

### 1. EventHub: Data Factory for Generalizable Event-Based Stereo Networks without Active Sensors

- **Authors**: Luca Bartolomei, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Guillermo Gallego
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02331v1](http://arxiv.org/abs/2604.02331v1)
- **PDF**: [https://arxiv.org/pdf/2604.02331v1.pdf](https://arxiv.org/pdf/2604.02331v1.pdf)
- **Abstract**: We propose EventHub, a novel framework for training deep-event stereo networks without ground truth annotations from costly active sensors, relying instead on standard color images. From these images, we derive either proxy annotations and proxy events through state-of-the-art novel view synthesis techniques, or simply proxy annotations when images are already paired with event data. Using the training set generated by our data factory, we repurpose state-of-the-art stereo models from RGB litera...

---


## 🚁 UAV Vision (1)

### 1. CoRegOVCD: Consistency-Regularized Open-Vocabulary Change Detection

- **Authors**: Weidong Tang, Hanbin Sun, Zihan Li, Yikai Wang, Feifan Zhang
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02160v1](http://arxiv.org/abs/2604.02160v1)
- **PDF**: [https://arxiv.org/pdf/2604.02160v1.pdf](https://arxiv.org/pdf/2604.02160v1.pdf)
- **Abstract**: Remote sensing change detection (CD) aims to identify where land-cover semantics change across time, but most existing methods still assume a fixed label space and therefore cannot answer arbitrary user-defined queries. Open-vocabulary change detection (OVCD) instead asks for the change mask of a queried concept. In the fully training-free setting, however, dense concept responses are difficult to compare directly across dates: appearance variation, weak cross-concept competition, and the spatia...

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
