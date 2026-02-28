import os
from crewai import Crew, Process
from agents import researcher, blogger
from tasks import create_research_task, create_blog_task
from dotenv import load_dotenv

load_dotenv()


def run_youtube_blog_crew(video_title: str, channel_name: str) -> str:

    # Pass agent objects directly into task functions
    research_task = create_research_task(video_title, channel_name, researcher)
    blog_task = create_blog_task(video_title, research_task, blogger)

    crew = Crew(
        agents=[researcher, blogger],
        tasks=[research_task, blog_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result


if __name__ == "__main__":
    VIDEO_TITLE = "How to build AI Agents with CrewAI"
    CHANNEL_NAME = "TechWithTim"

    print(f"\n🔍 Searching for: '{VIDEO_TITLE}' on channel: '{CHANNEL_NAME}'\n")

    result = run_youtube_blog_crew(VIDEO_TITLE, CHANNEL_NAME)

    print("\n" + "=" * 60)
    print("📝 FINAL BLOG POST")
    print("=" * 60)
    print(result)

# tools.py  ←  agents.py  ←  crew.py  →  tasks.py