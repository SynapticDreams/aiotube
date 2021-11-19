import re
from .threads import _Thread
from .auxiliary import _duration, _src


class Video:

    def __init__(self, videoId: str):
        """
        :param videoId: video id or the url of the video
        """
        if 'watch?v=' in videoId:
            self._url = videoId
            self._id = re.findall(r"v=(.*)", videoId)[0]

        elif 'youtu.be/' in videoId:
            idL = re.findall(r"youtu\.be/(.*)", videoId)
            self._url = f'https://www.youtube.com/watch?v={idL[0]}'
            self._id = re.findall(r"/(.*)", videoId)[0]
        else:
            self._url = f'https://www.youtube.com/watch?v={videoId}'
            self._id = videoId

    @property
    def url(self):
        return self._url

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        """
        :return: the title of the video
        """
        raw = _src(self._url)
        data = re.findall(r"\"title\":\"(.*?)\"", raw)
        return data[0] if len(data) > 0 else None

    @property
    def views(self):
        """
        :return: total views the video got so far
        """
        raw = _src(self._url)
        data = re.findall(
            r"\"videoViewCountRenderer\":{\"viewCount\":{\"simpleText\":\"(.*?)\"",
            raw
        )
        return data[0][:-6] if len(data) > 0 else None

    @property
    def likes(self):
        """
        :return: total likes the video got so far
        """
        raw = _src(self._url)
        data = re.findall(
            r"toggledText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.*?) ",
            raw
        )
        return data[0] if len(data) > 0 else None

    @property
    def dislikes(self):
        raise DeprecationWarning("This property is deprecated as YouTube depreciated public dislike counts.")

    @property
    def duration(self):
        """
        :return: total duration of  the video in 00h 00m 00s
        """
        raw = _src(self._url)
        data = re.findall(r"approxDurationMs\":\"(.*?)\"", raw)
        return _duration(int(int(data[0]) / 1000)) if data else None

    @property
    def date(self):
        """
        :return: the date on which the video has been uploaded
        """
        raw = _src(self._url)
        data = re.findall(r"uploadDate\":\"(.*?)\"", raw)
        return data[0] if len(data) > 0 else None

    @property
    def author(self):
        """
        :return: the id of the channel from which the video belongs
        """
        raw = _src(self._url)
        data = re.findall(r"channelIds\":\[\"(.*?)\"", raw)
        return data[0] if len(data) > 0 else None

    @property
    def description(self):
        """
        :return: description provided with the video
        """
        raw = _src(self._url)
        data = re.findall(r"shortDescription\":\"(.*)\",\"isCrawlable", raw)
        return data[0].replace('\\n', '') if len(data) > 0 else None

    @property
    def thumbnail(self):
        """
        :return: _url of the thumbnail of the video
        """
        raw = _src(self._url)
        data = re.findall(
            r"playerMicroformatRenderer\":{\"thumbnail\":{\"thumbnails\":\[{\"url\":\"(.*?)\"",
            raw
        )
        return data[0] if len(data) > 0 else None

    @property
    def tags(self):
        """
        :return: list of tags used in video meta-data
        """
        raw = _src(self._url)
        data = re.findall(r"<meta name=\"keywords\" content=\"(.*?)\">", raw)
        return data[0].split(',') if len(data) > 0 else None

    @property
    def info(self):
        """
        :return: dict containing the the whole info of the video
        dict = {

            'title': -> str,
            'id': -> str,
            'views': -> str,
            'likes': -> str,
            'dislikes': -> str,
            'duration': -> str,
            'author': -> str,
            'uploaded': -> str,
            'url': -> str,
            'thumbnail': -> str,
            'tags': -> list,
        }
        """
        raw = _src(self._url)

        def _get_data(pattern):
            data = re.findall(pattern, raw)
            return data[0] if len(data) > 0 else None

        patterns = [

            r"\"title\":\"(.*?)\"",
            r"\"videoViewCountRenderer\":{\"viewCount\":{\"simpleText\":\"(.*?)\"",
            r"toggledText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.*?) ",
            r"approxDurationMs\":\"(.*?)\"",
            r"channelIds\":\[\"(.*?)\"",
            r"uploadDate\":\"(.*?)\"",
            r"playerMicroformatRenderer\":{\"thumbnail\":{\"thumbnails\":\[{\"url\":\"(.*?)\"",
            r"<meta name=\"keywords\" content=\"(.*?)\">"

        ]

        ls = _Thread.run(_get_data, patterns)

        return {

            'title': ls[0],
            'id': self._id,
            'views': ls[1][:-6],
            'likes': ls[2],
            'duration': _duration(int(int(ls[4]) / 1000)),
            'author': ls[5],
            'uploaded': ls[6],
            'url': self._url,
            'thumbnail': ls[7],
            'tags': ls[8].split(','),
        }
