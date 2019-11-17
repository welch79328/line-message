from .base import Base
from .messages import (
    TextMessage,
    ImageMessage,
    VideoMessage
)
from .sources import SourceUser, SourceGroup, SourceRoom


class Event(Base):
    """Abstract Base Class of Webhook Event.

    https://devdocs.line.me/en/#webhook-event-object
    """

    def __init__(self, timestamp=None, source=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param kwargs:
        """
        super().__init__(**kwargs)

        self.type = None
        self.timestamp = timestamp
        self.source = self.get_or_new_from_json_dict_with_types(
            source, {
                'user': SourceUser,
                'group': SourceGroup,
                'room': SourceRoom,
            }
        )


class MessageEvent(Event):
    """Webhook MessageEvent.

    https://devdocs.line.me/en/#message-event

    Event object which contains the sent message.
    The message field contains a message object which corresponds with the message type.
    You can reply to message events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, message=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param message: Message object
        :type message: T <= :py:class:`linebot.models.messages.Message`
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'message'
        self.reply_token = reply_token
        self.message = self.get_or_new_from_json_dict_with_types(
            message, {
                'text': TextMessage,
                'image': ImageMessage,
                'video': VideoMessage,
            }
        )
