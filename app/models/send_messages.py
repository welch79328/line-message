from .base import Base


class SendMessage(Base):

    def __init__(self, quick_reply=None, **kwargs):

        super(SendMessage, self).__init__(**kwargs)

        self.type = None
        self.quick_reply = self.get_or_new_from_json_dict(quick_reply, QuickReply)


class TextSendMessage(SendMessage):

    def __init__(self, text=None, quick_reply=None, **kwargs):

        super().__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'text'
        self.text = text


class ImageSendMessage(SendMessage):

    def __init__(self, original_content_url=None, preview_image_url=None,
                 quick_reply=None, **kwargs):

        super().__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'image'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class VideoSendMessage(SendMessage):

    def __init__(self, original_content_url=None, preview_image_url=None,
                 quick_reply=None, **kwargs):

        super().__init__(quick_reply=quick_reply, **kwargs)

        self.type = 'video'
        self.original_content_url = original_content_url
        self.preview_image_url = preview_image_url


class QuickReply(Base):

    def __init__(self, items=None, **kwargs):
 
        super().__init__(**kwargs)

        new_items = []
        if items:
            for item in items:
                new_items.append(self.get_or_new_from_json_dict(
                    item, QuickReplyButton
                ))
        self.items = new_items
