# MyBot - Multi-Agent AI System

Welcome to **MyBot**, a state-of-the-art multi-agent AI system designed to assist across various domains, including inspiration discovery, automation, content creation, customer service, and data analysis. This project was developed as part of the Google Cloud Multi-Agents Hackathon 2025.

## Features

- Multiple specialized agents:
  - **Inspiration Agent**: Suggests destinations, news, and points of interest
  - **Automation Agent**: Assists with routine task automation
  - **Content Creation Agent**: Generates blogs, posts, content, and code
  - **Customer Service Agent**: Handles FAQs and customer queries
  - **Data Analysis Agent**: Provides insights and analysis

- Clean and modular Python codebase
- Environment managed with a `.env` file
- Structured and scalable architecture

---

## 🗺️ Architecture Diagram

Here is the system architecture for **MyBot**:

![Architecture Diagram](assets/Architecture%20Diagram.png)

## Project Structure

```plaintext
MyBot/
│
├── .venu/                        # Virtual environment folder
├── .env                          # Environment variables file
├── agents/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── agent.py
│   ├── prompt.py
│   └── sub_agents/
│       ├── __pycache__/
│       ├── Automation/
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── automation_agent.py
│       │   └── prompt.py
│       │
│       ├── Content_Creation_Generation/
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── Content_Creation_Generation.py
│       │   └── prompt.py
│       │
│       ├── Customer_Service/
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── Customer_Service_Engagement.py
│       │   └── prompt.py
│       │
│       ├── Data_Analysis/
│       │   ├── __init__.py
│       │   ├── agent.py
│       │   ├── Data_Analysis_Insights_agent.py
│       │   └── prompt.py
│       │
│       └── inspiration/
│           ├── __init__.py
│           ├── agent.py
│           └── prompt.py
│
├── tools/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── memory.py
│   ├── places.py
│   ├── search.py
│
└── README.md
```

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Abd-ul-Hannan/MyBot.git
   cd MyBot
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venu
   source .venu/bin/activate   # On Unix/macOS
   .\.venu\Scripts\activate    # On Windows
   ```

3. **Install dependencies:**

   *(Add any required libraries manually if not already specified.)*

4. **Configure environment variables:**

   Add your environment variables to the `.env` file.

5. **Run the application:**

   ```bash
   adk web
   ```

---

## Agent Descriptions

### 1. Automation Agent

- Automates business processes
- Manages the software development lifecycle
- Handles complex or repetitive tasks efficiently

### 2. Content Creation & Generation Agent

- Generates blogs, posts, reports, and marketing content
- Analyzes provided URLs and summarizes linked content
- Acts as a travel inspiration agent to help users find destinations and suggest activities
- Utilizes tools such as `place_agent` and `news_agent` to fetch destination data and trending news

### 3. Customer Service Engagement Agent

- Builds intelligent virtual assistants for customer service
- Handles complex customer inquiries
- Provides personalized and proactive support

### 4. Data Analysis & Insights Agent

- Analyzes data from various sources
- Utilizes tools such as BigQuery for data processing
- Extracts valuable insights and presents findings

### 5. Inspiration Agent

- Suggests travel destinations and points of interest
- Provides key news and events
- Assists users in planning vacations

---

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss your proposed modifications.

---



## Acknowledgements

- Google Cloud Multi-Agents Hackathon
- Python Community

---

Made with ❤️ by Abd ul Hannan
