# Prompt Scorer Playground 🎯

Quick demo app to practice Prompt Engineering and see how well your prompts perform.

---

## 🚀 Tech Stack
- FastAPI (Backend)
- Streamlit (Frontend)
- Mistral AI (via API)
- Docker & Docker Compose

---

## ⚙️ Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/BalajiArighant/prompt-engineering.git
    cd prompt-engineering
    ```

2. **Create a `.env` file**
    ```env
    API_URL=http://localhost:8000/evaluate
    MISTRAL_API_KEY=your_mistral_api_key_here
    ```

3. **Run using Docker Compose**
    ```bash
    docker-compose up --build
    ```

4. **Access the apps**
    - API: [http://localhost:8000](http://localhost:8000)
    - Frontend: [http://localhost:8501](http://localhost:8501)

---

## 🎯 Features
- Score your prompts based on basic good practices
- Get an actual AI's generated response from Mistral AI
- Visual feedback and improvement suggestions

---

Enjoy prompting! 🚀
