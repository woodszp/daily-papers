# Daily Paper Updates

Last updated: 2026-04-05

---

## 📊 Summary

Total papers found: **32**

---

## 🎯 LLM Quantization (31)

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

### 10. Batched Contextual Reinforcement: A Task-Scaling Law for Efficient Reasoning

- **Authors**: Bangji Yang, Hongbo Ma, Jiajun Fan, Ge Liu
- **Category**: `cs.CL`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02322v1](http://arxiv.org/abs/2604.02322v1)
- **PDF**: [https://arxiv.org/pdf/2604.02322v1.pdf](https://arxiv.org/pdf/2604.02322v1.pdf)
- **Abstract**: Large Language Models employing Chain-of-Thought reasoning achieve strong performance but suffer from excessive token consumption that inflates inference costs. Existing efficiency methods such as explicit length penalties, difficulty estimators, or multi-stage curricula either degrade reasoning quality or require complex training pipelines. We introduce Batched Contextual Reinforcement, a minimalist, single-stage training paradigm that unlocks efficient reasoning through a simple structural mod...

---

### 11. No Single Best Model for Diversity: Learning a Router for Sample Diversity

- **Authors**: Yuhan Liu, Fangyuan Xu, Vishakh Padmakumar, Daphne Ippolito, Eunsol Choi
- **Category**: `cs.CL`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02319v1](http://arxiv.org/abs/2604.02319v1)
- **PDF**: [https://arxiv.org/pdf/2604.02319v1.pdf](https://arxiv.org/pdf/2604.02319v1.pdf)
- **Abstract**: When posed with prompts that permit a large number of valid answers, comprehensively generating them is the first step towards satisfying a wide range of users. In this paper, we study methods to elicit a comprehensive set of valid responses. To evaluate this, we introduce \textbf{diversity coverage}, a metric that measures the total quality scores assigned to each \textbf{unique} answer in the predicted answer set relative to the best possible answer set with the same number of answers. Using t...

---

### 12. De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules

- **Authors**: Keerat Guliani, Deepkamal Gill, David Landsman, Nima Eshraghi, Krishna Kumar
- **Category**: `cs.CL`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02276v1](http://arxiv.org/abs/2604.02276v1)
- **PDF**: [https://arxiv.org/pdf/2604.02276v1.pdf](https://arxiv.org/pdf/2604.02276v1.pdf)
- **Abstract**: Regulatory documents encode legally binding obligations that LLM-based systems must respect. Yet converting dense, hierarchically structured legal text into machine-readable rules remains a costly, expert-intensive process. We present De Jure, a fully automated, domain-agnostic pipeline for extracting structured regulatory rules from raw documents, requiring no human annotation, domain-specific prompting, or annotated gold data. De Jure operates through four sequential stages: normalization of s...

---

### 13. Generative World Renderer

- **Authors**: Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu, Yidan Zhang
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02329v1](http://arxiv.org/abs/2604.02329v1)
- **PDF**: [https://arxiv.org/pdf/2604.02329v1.pdf](https://arxiv.org/pdf/2604.02329v1.pdf)
- **Abstract**: Scaling generative inverse and forward rendering to real-world scenarios is bottlenecked by the limited realism and temporal coherence of existing synthetic datasets. To bridge this persistent domain gap, we introduce a large-scale, dynamic dataset curated from visually complex AAA games. Using a novel dual-screen stitched capture method, we extracted 4M continuous frames (720p/30 FPS) of synchronized RGB and five G-buffer channels across diverse scenes, visual effects, and environments, includi...

---

### 14. Modulate-and-Map: Crossmodal Feature Mapping with Cross-View Modulation for 3D Anomaly Detection

- **Authors**: Alex Costanzino, Pierluigi Zama Ramirez, Giuseppe Lisanti, Luigi Di Stefano
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02328v1](http://arxiv.org/abs/2604.02328v1)
- **PDF**: [https://arxiv.org/pdf/2604.02328v1.pdf](https://arxiv.org/pdf/2604.02328v1.pdf)
- **Abstract**: We present ModMap, a natively multiview and multimodal framework for 3D anomaly detection and segmentation. Unlike existing methods that process views independently, our method draws inspiration from the crossmodal feature mapping paradigm to learn to map features across both modalities and views, while explicitly modelling view-dependent relationships through feature-wise modulation. We introduce a cross-view training strategy that leverages all possible view combinations, enabling effective an...

---

### 15. Steerable Visual Representations

- **Authors**: Jona Ruthardt, Manu Gaur, Deva Ramanan, Makarand Tapaswi, Yuki M. Asano
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02327v1](http://arxiv.org/abs/2604.02327v1)
- **PDF**: [https://arxiv.org/pdf/2604.02327v1.pdf](https://arxiv.org/pdf/2604.02327v1.pdf)
- **Abstract**: Pretrained Vision Transformers (ViTs) such as DINOv2 and MAE provide generic image features that can be applied to a variety of downstream tasks such as retrieval, classification, and segmentation. However, such representations tend to focus on the most salient visual cues in the image, with no way to direct them toward less prominent concepts of interest. In contrast, Multimodal LLMs can be guided with textual prompts, but the resulting representations tend to be language-centric and lose their...

---

### 16. Large-scale Codec Avatars: The Unreasonable Effectiveness of Large-scale Avatar Pretraining

- **Authors**: Junxuan Li, Rawal Khirodkar, Chengan He, Zhongshi Jiang, Giljoo Nam
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02320v1](http://arxiv.org/abs/2604.02320v1)
- **PDF**: [https://arxiv.org/pdf/2604.02320v1.pdf](https://arxiv.org/pdf/2604.02320v1.pdf)
- **Abstract**: High-quality 3D avatar modeling faces a critical trade-off between fidelity and generalization. On the one hand, multi-view studio data enables high-fidelity modeling of humans with precise control over expressions and poses, but it struggles to generalize to real-world data due to limited scale and the domain gap between the studio environment and the real world. On the other hand, recent large-scale avatar models trained on millions of in-the-wild samples show promise for generalization across...

---

### 17. Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning

- **Authors**: Xueying Li, Feng Lyu, Hao Wu, Mingliu Liu, Jia-Nan Liu
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02318v1](http://arxiv.org/abs/2604.02318v1)
- **PDF**: [https://arxiv.org/pdf/2604.02318v1.pdf](https://arxiv.org/pdf/2604.02318v1.pdf)
- **Abstract**: Training-free Vision-Language Navigation (VLN) agents powered by foundation models can follow instructions and explore 3D environments. However, existing approaches rely on greedy frontier selection and passive spatial memory, leading to inefficient behaviors such as local oscillation and redundant revisiting. We argue that this stems from a lack of metacognitive capabilities: the agent cannot monitor its exploration progress, diagnose strategy failures, or adapt accordingly. To address this, we...

---

### 18. A Simple Baseline for Streaming Video Understanding

- **Authors**: Yujiao Shen, Shulin Tian, Jingkang Yang, Ziwei Liu
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02317v1](http://arxiv.org/abs/2604.02317v1)
- **PDF**: [https://arxiv.org/pdf/2604.02317v1.pdf](https://arxiv.org/pdf/2604.02317v1.pdf)
- **Abstract**: Recent streaming video understanding methods increasingly rely on complex memory mechanisms to handle long video streams. We challenge this trend with a simple finding: a sliding-window baseline that feeds only the most recent N frames to an off-the-shelf VLM already matches or surpasses published streaming models. We formalize this baseline as SimpleStream and evaluate it against 13 major offline and online video LLM baselines on OVO-Bench and StreamingBench. Despite its simplicity, SimpleStrea...

---

### 19. VOID: Video Object and Interaction Deletion

- **Authors**: Saman Motamed, William Harvey, Benjamin Klein, Luc Van Gool, Zhuoning Yuan
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02296v1](http://arxiv.org/abs/2604.02296v1)
- **PDF**: [https://arxiv.org/pdf/2604.02296v1.pdf](https://arxiv.org/pdf/2604.02296v1.pdf)
- **Abstract**: Existing video object removal methods excel at inpainting content "behind" the object and correcting appearance-level artifacts such as shadows and reflections. However, when the removed object has more significant interactions, such as collisions with other objects, current models fail to correct them and produce implausible results. We present VOID, a video object removal framework designed to perform physically-plausible inpainting in these complex scenarios. To train the model, we generate a...

---

### 20. Omni123: Exploring 3D Native Foundation Models with Limited 3D Data by Unifying Text to 2D and 3D Generation

- **Authors**: Chongjie Ye, Cheng Cao, Chuanyu Pan, Yiming Hao, Yihao Zhi
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02289v1](http://arxiv.org/abs/2604.02289v1)
- **PDF**: [https://arxiv.org/pdf/2604.02289v1.pdf](https://arxiv.org/pdf/2604.02289v1.pdf)
- **Abstract**: Recent multimodal large language models have achieved strong performance in unified text and image understanding and generation, yet extending such native capability to 3D remains challenging due to limited data. Compared to abundant 2D imagery, high-quality 3D assets are scarce, making 3D synthesis under-constrained. Existing methods often rely on indirect pipelines that edit in 2D and lift results into 3D via optimization, sacrificing geometric consistency. We present Omni123, a 3D-native foun...

---


*... and 11 more papers in this direction*


## 📱 Edge Deployment (1)

### 1. EventHub: Data Factory for Generalizable Event-Based Stereo Networks without Active Sensors

- **Authors**: Luca Bartolomei, Fabio Tosi, Matteo Poggi, Stefano Mattoccia, Guillermo Gallego
- **Category**: `cs.CV`
- **Published**: 2026-04-02
- **arXiv**: [http://arxiv.org/abs/2604.02331v1](http://arxiv.org/abs/2604.02331v1)
- **PDF**: [https://arxiv.org/pdf/2604.02331v1.pdf](https://arxiv.org/pdf/2604.02331v1.pdf)
- **Abstract**: We propose EventHub, a novel framework for training deep-event stereo networks without ground truth annotations from costly active sensors, relying instead on standard color images. From these images, we derive either proxy annotations and proxy events through state-of-the-art novel view synthesis techniques, or simply proxy annotations when images are already paired with event data. Using the training set generated by our data factory, we repurpose state-of-the-art stereo models from RGB litera...

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
