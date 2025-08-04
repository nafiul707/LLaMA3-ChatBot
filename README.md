# 🦙 LLaMA3 Chatbot (Groq API + Streamlit)

A lightweight chatbot web app powered by **Groq’s ultra-fast LLaMA3-70B model** and built with **Streamlit**. No OpenAI subscription required — just a free Groq API key.

## 🚀 Features
- Clean Streamlit interface
- Powered by Groq’s LLaMA3-70B via API
- No dependency on OpenAI or Pro plans
- Session-based chat memory
- Easily extendable to support other models

## 📦 Installation

### Install dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Configuration

Create a file called `config.json` inside the `src/` directory with the following content:

```json
{
  "GROQ_API_KEY": "your_groq_api_key_here"
}
```

You can get a free API key from: [https://console.groq.com/keys](https://console.groq.com/keys)

## ▶️ Running the App

```bash
python -m streamlit run src/main.py
```

Open your browser to: [http://localhost:8501](http://localhost:8501)

## 📁 Project Structure

```
LLaMA3-ChatBot/
│
├── src/
│   ├── main.py           # Streamlit app code
│   └── config.json       # Your Groq API key (keep this private!)
│
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

Just make sure to securely handle your API key using **secrets management** on the chosen platform.

