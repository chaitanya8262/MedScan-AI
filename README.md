# 🏥 Medical Report Analyser

An AI-powered web application that analyses medical reports and explains them in simple, easy-to-understand language using **Google Gemini**.

---

## 🎯 What It Does

Upload any medical report (Blood test, X-Ray, MRI, etc.) and get:
- ✅ Simple explanation of medical terms
- ✅ Key findings highlighted
- ✅ Normal vs abnormal values identified
- ✅ Easy-to-understand health summary

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend logic |
| Google Gemini API | AI analysis & explanation |
| Streamlit | Web UI |
| Pillow / PyPDF2 | Image & PDF processing |

---

## 📁 Project Structure

```
MedicalReportAnalyser/
│
├── app.py              # Main application
├── api_key.py          # Gemini API key (don't push to GitHub!)
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/MedicalReportAnalyser.git
cd MedicalReportAnalyser
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API Key
```python
# api_key.py
GOOGLE_API_KEY = "your_api_key_here"
```
Get your free API key → [Google AI Studio](https://makersuite.google.com/app/apikey)

### 4. Run the app
```bash
streamlit run app.py
```

---

## 💡 How to Use

1. Open the app in your browser
2. Upload your medical report (PDF or Image)
3. Click **"Analyse Report"**
4. Get instant AI-powered explanation!

---

## 📊 Supported Report Types

- 🩸 Blood Test Reports (CBC, LFT, KFT, etc.)
- 🫁 X-Ray & Scan Reports
- 🧪 Pathology Reports
- 💊 Prescription Analysis
- 🏥 Discharge Summaries

---

## ⚙️ Requirements

```
streamlit
google-generativeai
Pillow
PyPDF2
python-dotenv
```

---

## 🔒 Security Note

**Never push your API key to GitHub!**

Add this to `.gitignore`:
```
api_key.py
.env
__pycache__/
```

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues for bugs or feature requests.

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Built with ❤️ using Google Gemini & Python 
