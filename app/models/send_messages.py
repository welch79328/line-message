

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class SendMessage(with_metaclass(ABCMeta, Base)):
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
        super(TextSendMessage, self).__init__(quick_reply=quick_reply, **kwargs)

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
        super(ImageSendMessage, self).__init__(quick_reply=quick_reply, **kwargs)

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
        super(VideoSendMessage, self).__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'video'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class AudioSendMessage(SendMessage):
    """AudioSendMessage.

    https://devdocs.line.me/en/#audio
    """

    def __init__(self, original_content_url=None, duration=None, quick_reply=None, **kwargs):
        """__init__ method.

        :param str original_content_url: URL of audio file.
            HTTPS
            m4a
            Less than 1 minute
            Max 10 MB
        :param long duration: Length of audio file (milliseconds).
        :param quick_reply: QuickReply object
        :type quick_reply: T <= :py:class:`linebot.models.send_messages.QuickReply`
        :param kwargs:
        """
        super(AudioSendMessage, self).__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'audio'
        self.original_content_url = original_content_url
        self.duration = duration


class LocationSendMessage(SendMessage):
    """LocationSendMessage.

    https://devdocs.line.me/en/#location
    """

    def __init__(self, title=None, address=None, latitude=None, longitude=None,
                 quick_reply=None, **kwargs):
        """__init__ method.

        :param str title: Title
        :param str address: Address
        :param float latitude: Latitude
        :param float longitude: Longitude
        :param quick_reply: QuickReply object
        :type quick_reply: T <= :py:class:`linebot.models.send_messages.QuickReply`
        :param kwargs:
        """
        super(LocationSendMessage, self).__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'location'
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude


class StickerSendMessage(SendMessage):
    """StickerSendMessage.

    https://devdocs.line.me/en/#sticker
    """

    def __init__(self, package_id=None, sticker_id=None, quick_reply=None, **kwargs):
        """__init__ method.

        :param str package_id: Package ID
        :param str sticker_id: Sticker ID
        :param quick_reply: QuickReply object
        :type quick_reply: T <= :py:class:`linebot.models.send_messages.QuickReply`
        :param kwargs:
        """
        super(StickerSendMessage, self).__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'sticker'
        self.package_id = package_id
        self.sticker_id = sticker_id


class QuickReply(with_metaclass(ABCMeta, Base)):
    """QuickReply.

    https://developers.line.me/en/docs/messaging-api/using-quick-reply/
    """

    def __init__(self, items=None, **kwargs):
        """__init__ method.

        :param items: Quick reply button objects
        :type items: list[T <= :py:class:`linebot.models.send_messages.QuickReplyButton`]
        :param kwargs:
        """
        super(QuickReply, self).__init__(**kwargs)

        new_items = []
        if items:
            for item in items:
                new_items.append(self.get_or_new_from_json_dict(
                    item, QuickReplyButton
                ))
        self.items = new_items
