---
title: Crew Ai
emoji: 🤖
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 5.25.0
app_file: app.py
pinned: false
---

# 🤖 CrewAI YouTube Blog Generator

> An AI-powered multi-agent system that automatically finds a YouTube video, fetches its transcript, and generates a professional SEO-optimized blog post — **completely free, no OpenAI key required!**

---

## 📌 What Does This Project Do?

This project uses **CrewAI** to orchestrate two AI agents that work together sequentially:

1. 🔍 **Researcher Agent** — Searches YouTube for a video by title and channel name, fetches the full transcript
2. ✍️ **Blogger Agent** — Reads the research and writes a complete, SEO-friendly blog post in Markdown

---

## 🗂️ Project Structure

```
CrewAI_multi_agents/
│
├── crew.py          # Entry point — assembles agents, tasks and runs the crew
├── agents.py        # Defines Researcher and Blogger agents with Gemini LLM
├── tasks.py         # Defines Research and Blog Writing tasks
├── tools.py         # Custom YouTube search and transcript tools (no OpenAI needed)
├── app.py           # Gradio UI for HuggingFace Spaces
├── .env             # API keys — never push this to GitHub!
├── .gitignore       # Ignores .env, cache, and system files
└── README.md        # You're reading it!
```

---

## ⚙️ Tech Stack

| Technology | Purpose | Cost |
|------------|---------|------|
| [CrewAI](https://github.com/joaomdmoura/crewAI) | Multi-agent orchestration | Free |
| [Google Gemini](https://aistudio.google.com) | LLM for both agents | Free |
| [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) | Fetch video transcripts | Free |
| [LiteLLM](https://github.com/BerriAI/litellm) | LLM provider abstraction | Free |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Manage environment variables | Free |
| [requests](https://pypi.org/project/requests/) | Scrape YouTube search results | Free |
| [Gradio](https://gradio.app) | Web UI on HuggingFace Spaces | Free |

> ✅ **No OpenAI API key required anywhere in this project!**

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/devendrayadav21/Crew_multi_AI_Agent.git
cd Crew_multi_AI_Agent
```

### 2. Create a Virtual Environment

```bash
conda create -n crewAI python=3.11
conda activate crewAI
```

### 3. Install Dependencies

```bash
pip install crewai crewai-tools youtube-transcript-api python-dotenv google-generativeai litellm requests gradio
pip install "crewai[google-genai]"
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your-gemini-api-key-here
```

> 🔑 Get your **free** Gemini API key at [aistudio.google.com](https://aistudio.google.com) → **Get API Key** → **Create API Key**

### 5. Run the Project

```bash
python crew.py
```

---

## ✏️ How to Use

Update the video title and channel name in `crew.py`:

```python
VIDEO_TITLE = "How to build AI Agents with CrewAI"
CHANNEL_NAME = "TechWithTim"
```

Then run:
```bash
python crew.py
```

The crew will:
1. Search YouTube for the video
2. Fetch the full transcript
3. Write and print a complete blog post in Markdown

---

## 🛠️ How It Works

```
crew.py (kickoff)
    │
    ├── Task 1: Research  ──►  Researcher Agent
    │                               ├── YoutubeSearchTool     → finds video URL
    │                               └── YoutubeTranscriptTool → fetches transcript
    │
    └── Task 2: Blog      ──►  Blogger Agent
                                    └── Uses Task 1 output → writes blog post
```

The tasks run **sequentially** — the blogger only starts after the researcher finishes, and automatically receives the research output as context.

---

## 🔧 Custom Tools (No OpenAI or ChromaDB!)

We built two fully custom tools that replace the broken `YoutubeVideoSearchTool` and `YoutubeChannelSearchTool` from `crewai-tools` (which require OpenAI embeddings and ChromaDB):

### `YoutubeSearchTool`
- Scrapes YouTube search results using `requests`
- Returns top 3 video URLs for the given title and channel
- No API key needed

### `YoutubeTranscriptTool`
- Searches YouTube for the video
- Uses `youtube-transcript-api` to fetch the full transcript
- Returns video ID, URL, and complete transcript text
- No API key needed

---

## ⚡ Performance Tips

| Setting | Value | Why |
|---------|-------|-----|
| `model` | `gemini-2.0-flash-lite` | Fastest and lightest Gemini model |
| `temperature` | `0.3` | Lower = faster, more focused responses |
| `max_iter` | `3` (researcher), `2` (blogger) | Prevents unnecessary loops |
| `allow_delegation` | `False` | Delegation adds extra LLM calls |

---

## 🐛 Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `OPENAI_API_KEY is required` | Using `YoutubeChannelSearchTool` from crewai-tools | Use custom tools from `tools.py` |
| `tool_use_failed` | Groq model doesn't support tool calling well | Switch to Gemini |
| `model_decommissioned` | Groq deprecated the model | Use `llama-3.1-70b-versatile` |
| `429 RESOURCE_EXHAUSTED` | Gemini free quota exceeded | Wait or create a new API key |
| `ChromaDB PanicException` | Corrupted ChromaDB files | Run `rm -rf ~/.local/share/chroma` |
| `Fallback to LiteLLM not available` | LiteLLM not installed | Run `pip install litellm` |
| `non-fast-forward` git error | Remote has commits local doesn't | Run `git pull origin main --allow-unrelated-histories` |
| `context=[create_research_task]` error | Passing function instead of task object | Pass the task object: `context=[research_task]` |
| `CONFLICT in README.md` | HuggingFace auto-generates README metadata | Keep the `---` metadata block at the top of README |

---

## 🔑 Free API Keys

| Service | Free Tier Limits | Sign Up |
|---------|-----------------|---------|
| Google Gemini | 15 RPM, 1M tokens/day | [aistudio.google.com](https://aistudio.google.com) |
| Groq (alternative) | 14,400 req/day | [console.groq.com](https://console.groq.com) |

---

## 📋 Requirements

- Python 3.11+
- Internet connection (for YouTube search and transcript fetching)
- Free Gemini API key
- ~500MB disk space (for model dependencies)

---

## 🔮 Future Improvements

- [ ] Save blog post output to a `.md` file automatically
- [ ] Add support for multiple videos in one run
- [ ] Add a third agent for SEO keyword optimization
- [ ] Build a Streamlit UI for easier input
- [ ] Support for YouTube playlists

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI) — for the amazing multi-agent framework
- [Google Gemini](https://aistudio.google.com) — for the free and powerful LLM
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) — for easy transcript fetching

---

<p align="center">Built with ❤️ using CrewAI and Google Gemini</p>
