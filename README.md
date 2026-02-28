# CrewAI YouTube Blog Generator

An AI-powered multi-agent system built with **CrewAI** that automatically finds a YouTube video, fetches its transcript, and generates a professional blog post — all without any paid API keys.

---

## 📌 Project Overview

This project uses two AI agents working sequentially:

- **Researcher Agent** — Searches YouTube for a video by title and channel, fetches the full transcript using `youtube-transcript-api`
- **Blogger Agent** — Takes the research output and writes a complete, SEO-optimized blog post in Markdown format

---

## 🗂️ Project Structure

```
CrewAI_multi_agents/
│
├── crew.py          # Entry point — assembles and runs the crew
├── agents.py        # Defines the Researcher and Blogger agents
├── tasks.py         # Defines the Research and Blog Writing tasks
├── tools.py         # Custom YouTube search and transcript tools
├── .env             # API keys (not pushed to GitHub)
├── .gitignore       # Ignores .env and cache files
└── README.md        # Project documentation
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| [CrewAI](https://github.com/joaomdmoura/crewAI) | Multi-agent orchestration framework |
| [Google Gemini](https://aistudio.google.com) | Free LLM for both agents |
| [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) | Fetch YouTube video transcripts |
| [LiteLLM](https://github.com/BerriAI/litellm) | LLM provider abstraction used by CrewAI |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Load environment variables from `.env` |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/devendrayadav21/Crew_multi_AI_Agent.git
cd Crew_multi_AI_Agent
```

### 2. Create and activate a virtual environment

```bash
conda create -n crewAI python=3.11
conda activate crewAI
```

### 3. Install dependencies

```bash
pip install crewai crewai-tools langchain-groq youtube-transcript-api python-dotenv google-generativeai litellm requests
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your-gemini-api-key
```

> 🔑 Get your **free** Gemini API key at [aistudio.google.com](https://aistudio.google.com)

### 5. Run the project

```bash
python crew.py
```

---

## 🛠️ How It Works

```
crew.py
  │
  ├── research_task  →  Researcher Agent
  │                         ├── YoutubeSearchTool      (finds video URL)
  │                         └── YoutubeTranscriptTool  (fetches transcript)
  │
  └── blog_task      →  Blogger Agent
                            └── Uses research output to write blog post
```

1. `crew.py` kicks off the crew with a video title and channel name
2. The **Researcher** searches YouTube, finds the video, and fetches its full transcript
3. The **Blogger** reads the research report and writes a complete blog post in Markdown
4. The final blog post is printed to the console

---

## ✏️ Customization

To search for a different video, update these variables in `crew.py`:

```python
VIDEO_TITLE = "How to build AI Agents with CrewAI"
CHANNEL_NAME = "TechWithTim"
```

---

## 🔑 Free API Keys Used

| Service | Free Tier | Link |
|---------|-----------|------|
| Google Gemini | 15 RPM, 1M tokens/day | [aistudio.google.com](https://aistudio.google.com) |
| Groq (optional) | 14,400 req/day | [console.groq.com](https://console.groq.com) |

> ✅ No OpenAI API key required!

---

## 📋 Requirements

- Python 3.11+
- Internet connection (for YouTube search and transcript fetching)
- Free Gemini API key

---

## 🐛 Common Issues

| Error | Fix |
|-------|-----|
| `OPENAI_API_KEY is required` | Make sure you're using `gemini/gemini-1.5-flash` as the model |
| `tool_use_failed` | Switch to Gemini — Groq has issues with tool calling |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- [Google Gemini](https://aistudio.google.com) for the free LLM
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) for transcript fetching
