# AWS-GENAI-ATTACKS-AND-DEFFENDS 🛡️⚔️

Welcome to the **AWS Generative AI Attacks and Defends** repository! 🚀 This comprehensive collection demonstrates various attack vectors and defensive strategies for Generative AI systems, with a focus on AWS-based implementations.

## 🎯 Overview

This repository covers practical examples of how to create different attacks and defenses for Generative AI systems. Whether you're a security researcher, AI engineer, or cybersecurity professional, these examples will help you understand the vulnerabilities and protective measures in modern AI applications.

## 📁 Repository Structure

### 🔍 PDF-Injections

The `pdf-injections` folder contains fascinating examples of how to manipulate CV (resume) files to alter candidate status and promote candidates who might not be the best fit by adding specific prompt injections. This demonstrates a critical vulnerability in AI-powered recruitment systems.

#### 📂 Folder Structure:

- **`cvs-sources/`** 📄 - Contains the original source CV files in markdown format
- **`original-pdfs/`** 📋 - Clean PDF versions without any malicious content for comparison
- **`injected-pdfs/`** 💉 - Contains PDF files with embedded prompt injections designed to confuse agentic systems

#### 🎭 How It Works:

The PDF injection attack works by embedding hidden prompts within CV documents that can manipulate AI systems that read and scan resumes. When an AI-powered recruitment system processes these documents, the injected prompts can:

- 🎯 Artificially boost candidate rankings
- 🔄 Override evaluation criteria
- 📈 Manipulate scoring algorithms
- 🎪 Trick automated screening systems

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+ 🐍
- Virtual environment (recommended) 📦

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd aws-genai-attacks-and-defends
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Analyzing CVs

Run the CV analyzer to extract and examine content from PDF files:

```bash
python3 pdf-injections/cv_analyzer.py
```

### Generating PDFs

Create PDF files from markdown sources:

```bash
python3 pdf-injections/generate_pdfs.py
```

## ⚠️ Ethical Considerations

This repository is intended for:

- 🎓 Educational purposes
- 🔬 Security research
- 🛡️ Defensive strategy development
- 📚 Understanding AI vulnerabilities

**Please use responsibly and ethically!** 🤝

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues, feature requests, or pull requests to help improve this educational resource.

## LICENSE

This project is provided for educational and research purposes. Please ensure you comply with all applicable laws and regulations when using these examples.

Copyright 2025 Santiago Garcia Arango.
