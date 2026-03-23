"""
Paper Analysis Module - Extract key information from papers
"""

import re
import urllib.request
import urllib.parse
import json
import os

def fetch_arxiv_abstract(arxiv_id):
    """Fetch paper abstract from arXiv API"""
    try:
        url = f'http://export.arxiv.org/api/query?id_list={arxiv_id}'
        with urllib.request.urlopen(url, timeout=10) as response:
            content = response.read().decode('utf-8')
        
        # Parse XML to extract abstract
        summary_match = re.search(r'<summary>(.*?)</summary>', content, re.DOTALL)
        if summary_match:
            return summary_match.group(1).strip()
    except Exception as e:
        print(f"Error fetching abstract: {e}")
    return None


def extract_arxiv_id(url):
    """Extract arXiv ID from URL"""
    match = re.search(r'arxiv\.org/abs/([0-9.]+v?\d*)', url)
    return match.group(1) if match else None


def analyze_paper(paper):
    """
    Analyze a paper and extract structured information
    Note: This is a simplified version. For full analysis, would need LLM or manual review.
    """
    arxiv_id = extract_arxiv_id(paper.get('url', ''))
    
    # Default analysis structure
    analysis = {
        'motivation': '需要查看原文分析',
        'related_work': '需要查看原文分析',
        'contributions': '需要查看原文分析',
        'method_steps': '需要查看原文分析',
        'why_better': '需要查看原文分析',
        'limitations': '需要查看原文分析',
        'multimodal_support': '需要评估',
        'experiments': {
            'types': '需要查看原文',
            'datasets': '需要查看原文',
            'results': '需要查看原文'
        },
        'abstract': ''
    }
    
    # If we have arXiv ID, try to get abstract
    if arxiv_id:
        abstract = fetch_arxiv_abstract(arxiv_id)
        if abstract:
            analysis['abstract'] = abstract[:500] + '...' if len(abstract) > 500 else abstract
            
            # Try to infer some information from abstract
            analysis = infer_from_abstract(abstract, analysis)
    
    return analysis


def infer_from_abstract(abstract, analysis):
    """Try to infer information from abstract"""
    abstract_lower = abstract.lower()
    
    # Detect if it's about multimodal
    multimodal_keywords = ['multimodal', 'vision-language', 'vlm', 'image', 'video', 'audio', 'visual']
    if any(kw in abstract_lower for kw in multimodal_keywords):
        analysis['multimodal_support'] = '是 - 论文涉及多模态内容'
    
    # Detect datasets mentioned
    datasets = []
    common_datasets = ['coco', 'voc', 'imagenet', 'flickr30k', 'vqav2', 'textvqa', 'mmlu', 'mme', 'pope', 'mmbench']
    for ds in common_datasets:
        if ds in abstract_lower:
            datasets.append(ds)
    if datasets:
        analysis['experiments']['datasets'] = ', '.join(datasets)
    
    # Detect experiment types
    if 'benchmark' in abstract_lower or 'evaluate' in abstract_lower:
        analysis['experiments']['types'] = '基准测试'
    if 'compare' in abstract_lower or 'outperform' in abstract_lower:
        analysis['experiments']['types'] = '对比实验'
    
    return analysis


def generate_analysis_markdown(papers):
    """Generate detailed markdown analysis for all papers"""
    md = """# 论文详细分析报告

## 分析维度说明

| 维度 | 说明 |
|------|------|
| 研究动机 | 为什么要做这个研究，解决什么问题 |
| 相关工作 | 已有方法有哪些，有什么不足 |
| 贡献点 | 本文的主要贡献 |
| 方法 | 具体做法，分几步，为什么好 |
| 局限 | 存在的不足 |
| 多模态支持 | 是否适合多模态大模型 |
| 实验 | 实验设置和数据集 |

---

"""
    
    for i, paper in enumerate(papers, 1):
        analysis = analyze_paper(paper)
        
        md += f"""## {i}. {paper['title']}

### 基本信息
- **作者**: {paper.get('authors', 'N/A')}
- **类别**: {paper.get('category', 'N/A')}
- **日期**: {paper.get('date', 'N/A')}
- **链接**: [arXiv]({paper.get('url', '#')})

### 研究动机
{analysis['motivation']}

### 相关工作
{analysis['related_work']}

### 本文贡献
{analysis['contributions']}

### 方法论
**步骤**: {analysis['method_steps']}

**为什么更好**: {analysis['why_better']}

### 局限性
{analysis['limitations']}

### 多模态大模型支持
{analysis['multimodal_support']}

### 实验
- **类型**: {analysis['experiments']['types']}
- **数据集**: {analysis['experiments']['datasets']}

---

"""
    
    return md


# Test
if __name__ == '__main__':
    test_paper = {
        'title': 'Test Paper',
        'url': 'http://arxiv.org/abs/2603.16859v1',
        'authors': 'Test Author',
        'category': 'LLM Quantization',
        'date': '2026-03-17'
    }
    result = analyze_paper(test_paper)
    print(json.dumps(result, ensure_ascii=False, indent=2))