from .base import Base


class Message(Base):

    def __init__(self, id=None, **kwargs):
 
        super().__init__(**kwargs)

        self.type = None
        self.id = id


class TextMessage(Message):

    def __init__(self, id=None, text=None, **kwargs):

        super().__init__(id=id, **kwargs)

        self.type = 'text'
        self.text = text


class ImageMessage(Message):

    def __init__(self, id=None, content_provider=None, **kwargs):

        super(ImageMessage, self).__init__(id=id, **kwargs)

        self.type = 'image'
        self.content_provider = self.get_or_new_from_json_dict(
            content_provider, ContentProvider
        )


class VideoMessage(Message):

    def __init__(self, id=None, duration=None, content_provider=None, **kwargs):

        super(VideoMessage, self).__init__(id=id, **kwargs)

        self.type = 'video'
        self.duration = duration
        self.content_provider = self.get_or_new_from_json_dict(
            content_provider, ContentProvider
        )
