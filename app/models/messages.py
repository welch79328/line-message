from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Message(with_metaclass(ABCMeta, Base)):
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

    def __init__():
        print(1111)


class VideoMessage(Message):

    def __init__():
        print(1111)

class AudioMessage(Message):

    def __init__():
        print(1111)


class LocationMessage(Message):

    def __init__():
        print(1111)


class StickerMessage(Message):
    
    def __init__():
        print(1111)


class FileMessage(Message):
    
    def __init__():
        print(1111)
