from .base import Base


class Message(Base):
    """Abstract Base Class of Message."""

    def __init__(self, id=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param kwargs:
        """
        super().__init__(**kwargs)

        self.type = None
        self.id = id


class TextMessage(Message):
    """TextMessage.

    https://devdocs.line.me/en/#text-message

    Message object which contains the text sent from the source.
    """

    def __init__(self, id=None, text=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param str text: Message text
        :param kwargs:
        """
        super().__init__(id=id, **kwargs)

        self.type = 'text'
        self.text = text


class ImageMessage(Message):
    """ImageMessage.

    https://developers.line.biz/en/reference/messaging-api/#wh-image

    Message object which contains the image content sent from the source.
    The binary image data can be retrieved with the Content API.
    """

    def __init__(self, id=None, content_provider=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param content_provider: ContentProvider object
        :type content_provider:
            :py:class:`linebot.models.messages.ContentProvider`
        :param kwargs:
        """
        super(ImageMessage, self).__init__(id=id, **kwargs)

        self.type = 'image'
        self.content_provider = self.get_or_new_from_json_dict(
            content_provider, ContentProvider
        )


class VideoMessage(Message):
    """VideoMessage.

    https://developers.line.biz/en/reference/messaging-api/#wh-video

    Message object which contains the video content sent from the source.
    The binary video data can be retrieved with the Content API.
    """

    def __init__(self, id=None, duration=None, content_provider=None, **kwargs):
        """__init__ method.

        :param str id: Message ID
        :param long duration: Length of video file (milliseconds)
        :param content_provider: ContentProvider object
        :type content_provider:
            :py:class:`linebot.models.messages.ContentProvider`
        :param kwargs:
        """
        super(VideoMessage, self).__init__(id=id, **kwargs)

        self.type = 'video'
        self.duration = duration
        self.content_provider = self.get_or_new_from_json_dict(
            content_provider, ContentProvider
        )
