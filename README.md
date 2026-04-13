# 🎨 Flask Portfolio Web App

This repository contains a modern, responsive **Flask-based web portfolio** project by [Shubham Gour Tech](https://www.youtube.com/shubhamgourtech).  
It is built to showcase Flask web development with a professional DevOps-themed UI.

---

<img width="1440" height="751" alt="Screenshot 2025-11-04 at 8 56 56 PM" src="https://github.com/user-attachments/assets/92bfa45f-0d2a-42b3-8767-24bdec967184" />

## 🚀 Features
- Flask-powered backend
- Beautiful responsive dark neon UI
- Sections: Hero, Who I Am, Life at Shubham Gour Tech, Playlists
- Smooth animations and glowing theme
- CI/CD ready with Docker and Jenkins

---

## 🧠 Tech Stack
- **Flask (Python)** — Backend Framework  
- **HTML, CSS** — Frontend Design  
- **Docker** — Containerization  
- **Jenkins** — CI/CD Pipeline

---

## ⚙️ Run Locally
```bash
pip install -r requirements.txt
python app.py
```

Then open [http://localhost:5000](http://localhost:5000)

---

<img width="1440" height="809" alt="Screenshot 2025-11-04 at 8 59 37 PM" src="https://github.com/user-attachments/assets/18c958b8-e4b3-45ef-875b-75eccfe2f646" />


## 🐳 Run with Docker
```bash
docker build -t theshubhamgour/flask-portfolio .
docker run -p 5000:5000 theshubhamgour/flask-portfolio
```

---
<img width="1440" height="813" alt="Screenshot 2025-11-04 at 9 00 03 PM" src="https://github.com/user-attachments/assets/fbc73e3e-5141-4984-8820-d4be0848d536" />

## 📁 Folder Structure
```
flask-portfolio/
│
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── playlist.html
│
└── static/
    ├── style.css
    ├── favicon.ico
    └── img/    # Add your photos here
```

---

## 👨‍💻 Author
**Shubham Gour**  
Release Engineer | DevOps | Cloud | YouTuber  
🔗 [LinkedIn](https://www.linkedin.com/in/theshubhamgour/)  
🎥 [YouTube](https://www.youtube.com/shubhamgourtech)

---

## 📜 License
MIT License © 2025 Shubham Gour Tech
