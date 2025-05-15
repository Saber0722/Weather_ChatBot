# 🌦️ Weather ChatBot

A conversational AI assistant built with Rasa that provides real-time weather information for any city. It utilizes the `uv` package manager for efficient dependency management and leverages environment variables for secure API key handling.

---

## 🚀 Features

* Provides current weather details for any city.
* Handles natural language queries like:

  * "What's the weather in Paris?"
  * "Is it raining in Tokyo?"
  * "Tell me the temperature in New York."
* Utilizes environment variables to manage sensitive information securely.
* Employs the `uv` package manager for rapid and reliable dependency installation.

---

## 🛠️ Tech Stack

* Python 3.10+
* Rasa (NLU and Core)
* `uv` (Python package and project manager)
* OpenWeatherMap API
* `python-dotenv` for environment variable management([YouTube][1])

---

## 📦 Installation

### Prerequisites

* Python 3.10 or higher
* `uv` package manager([Rasa][2])

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Saber0722/Weather_ChatBot.git
   cd Weather_ChatBot
   ```



2. **Install `uv`**

   Follow the official installation guide for `uv`: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

3. **Create a Virtual Environment**

   ```bash
   uv venv
   source .venv/bin/activate  # On Windows:. \.venv\Scripts\activate
   ```



4. **Install Dependencies**

   ```bash
   uv pip install -r requirements.txt
   ```



5. **Set Up Environment Variables**

   In the `.env` file in the project root directory, add your OpenWeatherMap API key:

   ```env
   OPENWEATHER_API_KEY=your_api_key_here
   ```



Replace `your_api_key_here` with your actual API key.

---

## 🧪 Running the Bot

1. **Train the Rasa Model**

   ```bash
   rasa train
   ```



3. **Start the Rasa Action Server**

   In the first terminal:
   
   ```bash
   rasa run actions
   ```



4. **Run the Rasa Server**

   In a new terminal window:

   ```bash
   rasa shell
   ```

5. **Interact with the Bot**

   You can now interact with the bot via the command line.

---

## 🗂️ Project Structure

```plaintext
.
├── actions/              # Custom action to fetch weather
├── data/                 # NLU training data and stories
├── models/               # Trained Rasa models
├── .env                  # Environment variables
├── config.yml            # NLU pipeline and policies
├── credentials.yml       # Rasa credentials
├── domain.yml            # Bot domain (intents, entities, responses)
├── endpoints.yml         # Action server endpoints
├── main.py               # Entry point to run the bot
├── pyproject.toml        # Project metadata and dependencies
├── requirements.txt      # Python dependencies
└── uv.lock               # Lock file for uv
```



---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---
