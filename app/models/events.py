from .base import Base
from .messages import (
    TextMessage,
    ImageMessage,
    VideoMessage
)
from .sources import SourceUser, SourceGroup, SourceRoom


class Event(Base):

    def __init__(self, timestamp=None, source=None, **kwargs):

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

    def __init__(self, timestamp=None, source=None, reply_token=None, message=None, **kwargs):

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
