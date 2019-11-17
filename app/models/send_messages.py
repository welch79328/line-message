from .base import Base


class SendMessage(Base):
    """Abstract Base Class of SendMessage."""

    def __init__(self, quick_reply=None, **kwargs):
        """__init__ method.

        :param quick_reply: QuickReply object
        :type quick_reply: T <= :py:class:`linebot.models.send_messages.QuickReply`
        :param kwargs:
        """
        super(SendMessage, self).__init__(**kwargs)

        self.type = None
        self.quick_reply = self.get_or_new_from_json_dict(quick_reply, QuickReply)


class TextSendMessage(SendMessage):
    """TextSendMessage.

    https://devdocs.line.me/en/#text
    """

    def __init__(self, text=None, quick_reply=None, **kwargs):
        """__init__ method.

        :param str text: Message text
        :param quick_reply: QuickReply object
        :type quick_reply: T <= :py:class:`linebot.models.send_messages.QuickReply`
        :param kwargs:
        """
        super().__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'text'
        self.text = text


class ImageSendMessage(SendMessage):
    """ImageSendMessage.

    https://devdocs.line.me/en/#image
    """

    def __init__(self, original_content_url=None, preview_image_url=None,
                 quick_reply=None, **kwargs):
        """__init__ method.

        :param str original_content_url: Image URL.
            HTTPS
            JPEG
            Max: 1024 x 1024
            Max: 1 MB
        :param str preview_image_url: Preview image URL
            HTTPS
            JPEG
            Max: 240 x 240
            Max: 1 MB
        :param quick_reply: QuickReply object
        :type quick_reply: T <= :py:class:`linebot.models.send_messages.QuickReply`
        :param kwargs:
        """
        super().__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'image'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class VideoSendMessage(SendMessage):
    """VideoSendMessage.

    https://devdocs.line.me/en/#video
    """

    def __init__(self, original_content_url=None, preview_image_url=None,
                 quick_reply=None, **kwargs):
        """__init__ method.

        :param str original_content_url: URL of video file.
            HTTPS
            mp4
            Less than 1 minute
            Max: 10 MB
        :param str preview_image_url: URL of preview image.
            HTTPS
            JPEG
            Max: 240 x 240
            Max: 1 MB
        :param quick_reply: QuickReply object
        :type quick_reply: T <= :py:class:`linebot.models.send_messages.QuickReply`
        :param kwargs:
        """
        super().__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'video'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class QuickReply(Base):
    """QuickReply.

    https://developers.line.me/en/docs/messaging-api/using-quick-reply/
    """

    def __init__(self, items=None, **kwargs):
        """__init__ method.

        :param items: Quick reply button objects
        :type items: list[T <= :py:class:`linebot.models.send_messages.QuickReplyButton`]
        :param kwargs:
        """
        super().__init__(**kwargs)

        new_items = []
        if items:
            for item in items:
                new_items.append(self.get_or_new_from_json_dict(
                    item, QuickReplyButton
                ))
        self.items = new_items
