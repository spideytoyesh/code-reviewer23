# 🤖 AI Code Reviewer

An AI-powered code review assistant that analyzes your code, detects issues, and suggests improvements instantly.

---

## 🚀 Features

* 🔍 Detects bugs and logical errors
* ⚡ Suggests performance optimizations
* 📖 Improves code readability
* 🧠 Provides AI-powered insights
* 🌐 Supports multiple programming languages

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenAI API

---

## 📸 Demo

Paste your code → Click **Review Code** → Get instant feedback from AI 🚀

---

## 🧪 Example Use Case

Input:

```python
def is_prime(n):
    if n <= 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

Output:

* ❌ Incorrect logic for prime check
* ⚡ Suggests optimization using √n
* 📖 Improves readability

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Replace in `app.py`:

```python
openai.api_key = "YOUR_API_KEY"
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 🌍 Deployment

You can deploy this app easily using:

* Streamlit Cloud
* Hugging Face Spaces

---

## 💡 Future Improvements

* 🔥 Code quality scoring system
* 📊 Visualization of complexity
* 🗂️ Multi-file support
* 🧑‍💻 GitHub repository integration

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by **[Your Name]**

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
