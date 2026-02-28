from crewai import Task


def create_research_task(video_title: str, channel_name: str, researcher) -> Task:
    return Task(
        description=f"""
        Your goal is to find and analyze the YouTube video titled '{video_title}' 
        from the '{channel_name}' channel.

        Follow these steps:
        1. Search for the video titled '{video_title}' on the '{channel_name}' channel
        2. Use the YouTube Transcript Fetcher tool to get the full transcript of the video
        3. Carefully read through the entire transcript
        4. Extract and organize the following:
            - Video URL and metadata
            - A high-level summary of what the video covers
            - At least 7 key points or insights discussed
            - Any tools, frameworks, or resources mentioned
            - Notable quotes or important statements
            - Step-by-step processes or tutorials explained (if any)
        5. Present all findings in a clean, structured research report
        """,
        agent=researcher,  # ← passed as argument
        expected_output="""
        A structured research report containing:
        - Video title, URL, and channel name
        - High-level video summary (2-3 paragraphs)
        - 7+ key points and insights from the transcript
        - Tools, resources, or references mentioned
        - Notable quotes or highlights
        """
    )


def create_blog_task(video_title: str, research_task: Task, blogger) -> Task:
    return Task(
        description=f"""
        Using the research report provided about the YouTube video '{video_title}',
        write a comprehensive, engaging, and SEO-optimized blog post.

        Your blog post MUST include:
        1. A catchy, SEO-friendly blog title
        2. An engaging introduction that hooks the reader
        3. Well-structured body sections with clear H2 and H3 headings
        4. Detailed explanation of each key point from the research
        5. A 'Key Takeaways' section with bullet points
        6. A strong conclusion with a clear call-to-action
        7. A credit section linking back to the original YouTube video

        Blog requirements:
        - Length: 900-1200 words
        - Tone: Conversational yet professional
        - Format: Markdown
        """,
        agent=blogger,  # ← passed as argument
        expected_output="""
        A complete blog post in Markdown format with:
        - SEO-friendly title
        - Engaging introduction
        - Structured body with H2/H3 headings
        - Key Takeaways section
        - Strong conclusion with CTA
        - Credit to original YouTube video
        """,
        context=[research_task]
    )