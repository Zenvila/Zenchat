# Zenchat
This repo contain chatting app project that is fully Dockerize.


# 💬 ZenChat - Dockerized Flask Chat App

ZenChat is a simple and lightweight real-time chat application built with **Flask** and **SQLite3**, fully containerized using **Docker**.  
The purpose of this project is to learn how to dockerize a full-stack Python web app (frontend + backend + database) and run it easily anywhere.

---

## 📦 Features

- 🧱 Built using Flask (Python micro web framework)
- 🗂 Uses SQLite3 (no setup needed)
- 📥 Add, delete, and manage chat messages
- 🕒 Shows timestamp with each message
- 🎨 Simple and clean chat UI
- 🐳 Fully Dockerized for deployment

---

## 🧰 Folder Structure

```
zenchat/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── db.py
│   └── templates/
│       └── index.html
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🐍 Local Setup (Without Docker)

> Only if you want to test it without Docker.

### Step 1: Create a Virtual Environment

```bash
python -m venv flaskenv
source flaskenv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python app.py
```

Visit: http://localhost:5000

---

## 🐳 Dockerized Setup (Recommended)

> Run your full application in a container!

### 🔨 Step 1: Build Docker Image

```bash
docker build -t zenchat-full .
```

### 🚀 Step 2: Run Docker Container

```bash
docker run -d -p 5000:5000 zenchat-full
```

Now visit: [http://localhost:5000](http://localhost:5000)

---

## ⬇️ Clone and Run from GitHub

```bash
git clone https://github.com/zenvila/zenchat.git
cd zenchat
docker build -t zenchat-full .
docker run -d -p 5000:5000 zenchat-full
```

---

## 👤 Author

**Haris (aka Zenvila)**  
📧 arainharis151@gmail.com  
🎓 BS Computer Science @ FAST  
💻 Passionate about Linux, SystemProgramming and Automation. 
🔗 GitHub: [github.com/zenvila](https://github.com/zenvila)

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and share!
