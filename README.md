# 🤖 TalentScout – AI-Powered Interview Assistant

TalentScout is a smart, AI-powered interview assistant built using **Streamlit** and **Hugging Face’s Zephyr model**. It collects candidate information, analyzes tech stacks, and generates personalized technical interview questions based on the user's experience — all through a clean, multi-step interface.

---

## 🚀 Features

- ✅ Multi-step Streamlit UI  
- ✅ Candidate info form (name, email, phone, experience, role)  
- ✅ Free-form tech stack input with intelligent parsing  
- ✅ Uses Hugging Face LLM (`zephyr-7b-beta`) to generate 3 questions per tech skill  
- ✅ Adapts difficulty based on experience level  
- ✅ Candidate writes responses, reviews them, and downloads a summary  
- ✅ `.txt` summary file for easy submission or storage  

---

## 🧠 Tech Stack

| Technology        | Purpose                             |
|------------------|-------------------------------------|
| `Streamlit`      | Frontend web interface              |
| `Hugging Face`   | LLM model API (`zephyr-7b-beta`)    |
| `transformers`   | Model utilities (optional)          |
| `python-dotenv`  | Secure token loading via `.env`     |
| `requests`       | For API calls if used               |
| `torch`          | Backend engine (used by LLM)        |

---

## 📁 Project Structure

```
.
├── app.py              # Streamlit app (UI and logic)
├── llm.py              # Tech stack parser and question generator using Hugging Face
├── .env                # Hugging Face API credentials (not shared)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/talent-scout.git
cd talent-scout
```

### 2. Create `.env` File

In the root directory, create a `.env` file:

```
HF_TOKEN=hf_your_token_here
HF_MODEL=HuggingFaceH4/zephyr-7b-beta
```

> 🔐 Create a free Hugging Face token from: https://huggingface.co/settings/tokens

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📦 Requirements

These are listed in `requirements.txt`:

```
streamlit
python-dotenv
requests
huggingface_hub
transformers
torch
```

---

## 💡 How It Works

1. Candidate fills in their basic info.  
2. Lists technologies they're confident with.  
3. App parses tech stack.  
4. Questions are generated per tech via Hugging Face model.  
5. Candidate answers each one interactively.  
6. Final review → Download `.txt` summary.  

---

## 🧪 Sample Prompt to LLM

```
Generate exactly 3 technical questions about Django for a candidate with 3 years of experience.
Difficulty level: intermediate
Format each question clearly numbered like:
1. [Question]
2. [Question]
3. [Question]
```

---

## ✅ Ideal For

- AI-based tech screening prototypes  
- Internship or college AI/ML submission  
- Demonstrating LLM and prompt integration  
- Streamlit multi-step UI apps  

---

## 👤 Author

**Momin Riyazahmed N.**  
Built as part of an internship project to showcase AI integration for technical hiring assistants.

---

## 📄 License

This project is intended for educational and demonstration purposes only. Not production-ready without human oversight.
