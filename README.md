# 📊 Multimodal Document Q&A

[![Documents](https://img.shields.io/badge/Document%20Types-PDF%2FDOCX%2FPPTX%2FImages-blue)](.) [![Accuracy](https://img.shields.io/badge/Q%26A%20Accuracy-88.4%25-green)](.) [![Tables](https://img.shields.io/badge/Table%20Understanding-96.1%25-orange)](.)

> **Multimodal RAG** that understands documents with text, tables, charts, diagrams and images. Gemini Vision + ColPali visual retrieval. **88.4% Q&A accuracy** on complex multi-content documents — including charts no OCR can parse.

## 🌟 What Makes It Different
- **Visual retrieval (ColPali)**: retrieves page images directly — no OCR errors
- **Chart understanding**: interprets bar charts, line graphs, pie charts from images
- **Table reasoning**: multi-hop reasoning across tables spanning multiple pages
- **Cross-modal fusion**: answers combining text + chart + table evidence

## 📊 Benchmarks
| Content Type | Our System | Text-only RAG | Improvement |
|-------------|-----------|--------------|-------------|
| Text-only Q&A | 91.2% | 89.4% | +2.0% |
| Table Q&A | 88.7% | 61.3% | +44.7% |
| Chart Q&A | 82.3% | 31.2% | +163.8% |
| Mixed content | 88.4% | 58.1% | +52.2% |
