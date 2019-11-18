import warnings
from .base import Base

class Source(Base):

    def __init__(self, **kwargs):

        super(Source, self).__init__(**kwargs)
        self.type = None

    def sender_id(self):

        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        raise NotImplementedError


class SourceUser(Source):

    def __init__(self, user_id=None, **kwargs):

        super(SourceUser, self).__init__(**kwargs)

        self.type = 'user'
        self.user_id = user_id

    @property
    def sender_id(self):

        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        return self.user_id


class SourceGroup(Source):

    def __init__(self, group_id=None, user_id=None, **kwargs):

        super(SourceGroup, self).__init__(**kwargs)

        self.type = 'group'
        self.group_id = group_id
        self.user_id = user_id

    @property
    def sender_id(self):

        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        return self.group_id


class SourceRoom(Source):

    def __init__(self, room_id=None, user_id=None, **kwargs):

        super(SourceRoom, self).__init__(**kwargs)

        self.type = 'room'
        self.room_id = room_id
        self.user_id = user_id

    @property
    def sender_id(self):

        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        return self.room_id
