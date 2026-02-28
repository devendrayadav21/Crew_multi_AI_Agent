from youtube_transcript_api import YouTubeTranscriptApi
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
import re


# ─────────────────────────────────────────────
# Tool 1: Search YouTube and Get Video URL
# ─────────────────────────────────────────────
class YoutubeSearchInput(BaseModel):
    video_title: str = Field(..., description="Title of the YouTube video to search for")
    channel_name: str = Field(..., description="Name of the YouTube channel")


class YoutubeSearchTool(BaseTool):
    name: str = "YouTube Video Searcher"
    description: str = """Searches YouTube for a video by title and channel name.
    Returns the video URL and video ID."""
    args_schema: type[BaseModel] = YoutubeSearchInput

    def _run(self, video_title: str, channel_name: str) -> str:
        try:
            search_query = f"{video_title} {channel_name}"
            search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"

            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(search_url, headers=headers)

            video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', response.text)

            if not video_ids:
                return "No videos found for the given title and channel."

            # Return top 3 results
            results = []
            for video_id in video_ids[:3]:
                results.append(f"https://www.youtube.com/watch?v={video_id}")

            return f"Found videos:\n" + "\n".join(results)

        except Exception as e:
            return f"Error searching YouTube: {str(e)}"


# ─────────────────────────────────────────────
# Tool 2: Fetch Full Transcript
# ─────────────────────────────────────────────
class YoutubeTranscriptInput(BaseModel):
    video_title: str = Field(..., description="Title of the YouTube video to search for")
    channel_name: str = Field(..., description="Name of the YouTube channel")


class YoutubeTranscriptTool(BaseTool):
    name: str = "YouTube Transcript Fetcher"
    description: str = """Fetches the full transcript of a YouTube video given its title and channel name.
    Use this tool to get the complete spoken content/dialogue of a YouTube video."""
    args_schema: type[BaseModel] = YoutubeTranscriptInput

    def _run(self, video_title: str, channel_name: str) -> str:
        try:
            search_query = f"{video_title} {channel_name}"
            search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"

            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(search_url, headers=headers)

            video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', response.text)

            if not video_ids:
                return "No videos found for the given title and channel."

            for video_id in video_ids[:5]:
                try:
                    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
                    transcript_text = " ".join([entry["text"] for entry in transcript_list])

                    return f"""
Video ID: {video_id}
Video URL: https://www.youtube.com/watch?v={video_id}

Full Transcript:
{transcript_text}
                    """
                except Exception:
                    continue

            return "Could not fetch transcript. The video may not have captions enabled."

        except Exception as e:
            return f"Error fetching transcript: {str(e)}"


# ─────────────────────────────────────────────
# Export Tools (No OpenAI needed)
# ─────────────────────────────────────────────
youtube_search_tool = YoutubeSearchTool()
youtube_transcript_tool = YoutubeTranscriptTool()