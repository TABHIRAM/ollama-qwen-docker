# 🚀 Local AI Chat: Qwen2.5 Coder with Docker + Ollama

Run a powerful local coding AI model (Qwen2.5-Coder 7B) using Docker and Ollama.

No cloud APIs required. Everything runs locally on your machine.

---

# 🧠 Tech Stack

- Docker
- Ollama
- Qwen2.5-Coder 7B

Docker Hub:
https://hub.docker.com/r/abhiramthimmaraju/docker-ollama-qwen2.5-coder

---

# ⚡ What This Project Does

- Runs local AI model inside Docker
- Uses Ollama backend
- Accepts terminal input
- Returns AI-generated responses
- Works fully offline after setup

---

# 🛠️ Setup Instructions

## 1. Install Docker
https://www.docker.com/

Check:
```bash
docker --version
```

---

## 2. Install Ollama
https://ollama.com

Check:
```bash
ollama --version
```

---

## 3. Download AI Model (IMPORTANT)

```bash
ollama pull qwen2.5-coder:7b
```

---

# 🚀 Run Project

## Pull Docker Image

```bash
docker pull abhiramthimmaraju/docker-ollama-qwen2.5-coder
```

---

## Start Container

```bash
docker run -it --rm abhiramthimmaraju/docker-ollama-qwen2.5-coder
```

---

# 💬 Use It

Inside container:

write prompts like:
- write python fibonacci
- explain docker
- build flask api
- debug code

---

# ⛔ Stop

Type:
```bash
exit
```

or press:
```bash
Ctrl + C
```

---

# 🔁 Run Again

```bash
docker run -it --rm abhiramthimmaraju/docker-ollama-qwen2.5-coder
```

---

# 🧹 Cleanup

```bash
docker container prune
docker system prune -a
```

---

# ⚠️ Important Notes

- First run downloads model (slow)
- Internet needed only once
- Works offline after setup

If Ollama not running:
```bash
ollama serve
```

---

# 👨‍💻 Author

Abhiram Thimmaraju  
GitHub: https://github.com/TABHIRAM  
Docker Hub: https://hub.docker.com/u/abhiramthimmaraju

---

# ⭐ Goal

Help beginners run local AI models easily using Docker + Ollama