from urllib.parse import urlparse, parse_qs

def get_video_id(url: str) -> str:
    parsed = urlparse(url)
    hostname = parsed.hostname

    if hostname in ["www.youtube.com", "youtube.com"]:
        video_id = parse_qs(parsed.query).get("v", [None])[0]

        if not video_id:
            raise ValueError("Could not find YouTube video ID.")

        return video_id

    if hostname == "youtu.be":
        video_id = parsed.path.lstrip("/")

        if not video_id:
            raise ValueError("Could not find YouTube video ID.")

        return video_id

    raise ValueError("Invalid YouTube URL.")