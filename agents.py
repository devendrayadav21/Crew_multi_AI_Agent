from crewai import Agent, LLM
from tools import youtube_search_tool, youtube_transcript_tool 
# from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
llm = LLM(
    model="gemini/gemini-flash-latest",  # Free, excellent tool calling
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)


researcher = Agent(
    role = "Professions Research Specialist",
    goal = (
        "Find youtube video with given title on the specified channel," 
        "fetch its full transcript , and extract all key informations nd insightes"
    ),
    backstory = """YYou are an expert YouTube researcher with years of experience 
    in finding and analyzing video content. You are skilled at searching YouTube 
    channels, identifying the correct videos, and extracting meaningful information 
    from transcripts including key topics, insights, and important quotes.""",
    tools=[youtube_search_tool, youtube_transcript_tool],
    llm=llm,
    max_rpm=15,
    max_iter=3,
    verbose = True,
    allow_delegation = False,
)


blogger = Agent(
    role = "Professional Blog writer",
    goal = (
        "Write an engaging, well-structured and SEO-friendly blog post "
        "summarizing the youtube video content provided by researcher"
    ),
    backstory = """You are a seasoned content writer and blogger with expertise in 
    transforming video transcripts into compelling written articles. You know how to 
    structure blog posts with catchy introductions, clear headings, key takeaways, 
    and strong conclusions that keep readers engaged and coming back for more.""",
    llm = llm,
    tools = [],
    max_iter=2,   # ← Blogger only needs 1-2 iterations
    max_rpm=15,
    verbose = True,
    allow_delegation = False
)