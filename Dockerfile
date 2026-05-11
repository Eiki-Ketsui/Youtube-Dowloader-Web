FROM python:3.9-slim
WORKDIR /NOMORE_YOUTUBE
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



COPY ../flask_app /NOMORE_YOUTUBE/Code
COPY ../Media/Video /NOMORE_YOUTUBE/Media/Video
COPY ../Media/Musique /NOMORE_YOUTUBE/Media/Musique

WORKDIR /NOMORE_YOUTUBE/Code

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0","--debug"]