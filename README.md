# Express.js Model Generator 🧠⚙️

a cli tool that uses AI to generate mongoose models for express.js for both javascript or typescript based on your inputs
<br />
you provide a model names and attributes and the script with AI generates a folder containing your models 

---

## Features

- Choose between JavaScript or TypeScript
- Prompt-based input for model names and attributes
- AI-generated Mongoose model files
- Saves generated models in a custom directory

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sofyanBoukir/express.js-model-gen.git
cd express.js-model-gen
```

### 2. Get your api-key from together.ai
 - Go to https://together.ai
 - sign up or sign in to get your API_KEY
 - COPY it
 - run this
   ```
    cp .env.example .env
   ```
 - PAST your API key their

### 3. configure & install requirements
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Run the script
```
python3 src/main.py
```



Developed with ❤️ by sofyan

