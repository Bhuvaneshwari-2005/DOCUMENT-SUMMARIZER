# 📄 DOCUMENT SUMMARIZER (RAG AI)

A state-of-the-art **Retrieval-Augmented Generation (RAG)** system designed for intelligent document interaction. Upload your files and engage in context-aware conversations powered by **Groq (Llama-3.3-70b)**, **ChromaDB**, and **Sentence-Transformers**.

---

## 🚀 Key Features

- **Multi-Format Extraction**: Native support for **PDF**, **DOCX**, **PPTX**, and **TXT**.
- **Advanced OCR & Handwriting Recognition**: Integrated **Tesseract OCR** with custom image pre-processing to extract text from images and handwritten notes in PDFs.
- **Semantic Search**: Powered by **ChromaDB** and `all-MiniLM-L6-v2` embeddings for highly accurate context retrieval.
- **Intelligent Chat Interface**: Context-aware AI assistant that remembers conversation history and cites sources.
- **Visual Intelligence**:
    - **Mermaid.js Integration**: Automatically generates and renders flowcharts, diagrams, and graphs.
    - **AI Image Generation**: Built-in support for generating visual aids via **Pollinations.ai**.
- **Professional Dashboard**: 3-column layout featuring a navigation sidebar, central document workspace, and an expansive AI interaction panel.
- **Interactive Voice**: Full Text-to-Speech (TTS) and Speech-to-Text (STT) capabilities with playback controls.
- **Local Network Access**: Automatically detects and displays local IP for access across your network.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **LLM**: Groq (Llama-3.3-70b-versatile)
- **Vector Database**: ChromaDB (Persistent)
- **Embeddings**: Sentence-Transformers (`all-MiniLM-L6-v2`)
- **OCR Engine**: Tesseract OCR & Poppler
- **Frontend**: HTML5, CSS3, Vanilla JavaScript, Mermaid.js

---

## 📂 Project Structure

```text
DOCUMENT-SUMMARIZER/
├── chroma_db/          # Persistent Vector storage
├── static/             # Assets (CSS, JS)
├── templates/          # Jinja2 HTML templates
├── app.py              # Core RAG logic & API routes
├── run_app.py          # Production entry point
├── chats.json          # Persistent chat history
├── requirements.txt    # Dependencies
└── .env                # Configuration
```

---

## ⚙️ Quick Start

### 1. Prerequisites
- **Tesseract OCR**: Install on your system (Default path: `C:\Program Files\Tesseract-OCR`)
- **Poppler**: Required for PDF-to-Image conversion (Extract to `C:\poppler`)

### 2. Installation
```bash
git clone https://github.com/Bhuvaneshwari-2005/DOCUMENT-SUMMARIZER.git
cd DOCUMENT-SUMMARIZER
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key
PORT=8080
```

### 4. Run
```bash
python run_app.py
```

---

## 💡 Usage

1. **Upload**: Drag and drop or browse files to index them into the Knowledge Base.
2. **Interact**: Ask questions about your documents in the chat panel.
3. **Visualize**: Ask for "diagrams" or "images" to see Mermaid and AI generation in action.
4. **Voice**: Use the microphone for hands-free queries or the volume icon for audio responses.

---

## ⚖️ License

Copyright (c) 2025 **BHUVANESHWARI PASHAM**. All Rights Reserved.

This software is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 📧 Contact & Collaboration

If you are interested in accessing the full system, discussing professional collaborations, or contributing to the project, please feel free to reach out.

📩 **bhuvanamudhiraj20@gmail.com**

---
&copy; 2025 AI Assistant. Developed by **BHUVANESHWARI PASHAM**.
