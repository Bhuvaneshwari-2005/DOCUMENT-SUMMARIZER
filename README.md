# DOCUMENT-SUMMARIZER
A sophisticated Retrieval-Augmented Generation (RAG) system that allows users to upload documents and interact with them using advanced AI. Built with Flask, ChromaDB, and Groq's Llama-3 models.

## Key Features

- **Advanced 3-Column Dashboard**: A professional, rebalanced layout featuring navigation, a central workspace for document management, and an expansive AI assistant panel.
- **Multi-Format Support**: Upload and index PDF, DOCX, PPTX, and TXT files seamlessly.
- **Real-Time KB Search**: Quickly filter through your indexed Knowledge Base with a dedicated document search bar.
- **Intelligent Retrieval**: Utilizes ChromaDB and Sentence-Transformers for highly accurate semantic search.
- **AI-Powered Chat**: Ask questions and receive detailed answers based strictly on your document context.
- **Visual Feedback**: Real-time animations for voice input and processing states.
- **Interactive Voice**: Full Text-to-Speech (TTS) integration with Play, Pause, and Stop controls.
- **Comprehensive Summaries**: Generate detailed document summaries with a single click.
- **Professional UI**: Polished Dark and Light themes with optimized contrast and modern depth effects.

## Tech Stack

- **Backend**: Python, Flask
- **Vector Database**: ChromaDB
- **LLM API**: Groq (Llama-3-70b)
- **Embeddings**: Sentence-Transformers (all-MiniLM-L6-v2)
- **Frontend**: HTML5, CSS3 (Modern Flexbox/Grid), Vanilla JavaScript

## Installation

1. **Clone the repository**:
   ```bash
   git https://github.com/Bhuvaneshwari-2005/DOCUMENT-SUMMARIZER.git
   cd DOCUMENT-SUMMARIZER
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**:
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   PORT=8080
   ```

4. **Run the application**:
   ```bash
   python run_app.py
   ```

## Usage

1. **Upload**: Use the compact upload zone to add documents to your Knowledge Base.
2. **Search**: Filter through your document list using the search bar in the center workspace.
3. **Chat**: Interact with the AI Assistant in the large right-side panel for context-aware insights.
4. **Voice**: Click the microphone icon to ask questions verbally, or use the volume icon to listen to AI responses.
5. **Summarize**: Generate and view document summaries directly from the sidebar.

---
&copy; 2026 AI Assistant.  
All rights reserved by **BHUVANESHWARI PASHAM**.
