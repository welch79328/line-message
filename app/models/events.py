

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base
from .messages import (
    TextMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    StickerMessage,
    FileMessage
)
from .sources import SourceUser, SourceGroup, SourceRoom


class Event(with_metaclass(ABCMeta, Base)):
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
                'audio': AudioMessage,
                'location': LocationMessage,
                'sticker': StickerMessage,
                'file': FileMessage
            }
        )



class FollowEvent(Event):
    """Webhook FollowEvent.

    https://devdocs.line.me/en/#follow-event

    Event object for when your account is added as a friend (or unblocked).
    You can reply to follow events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'follow'
        self.reply_token = reply_token


class UnfollowEvent(Event):
    """Webhook UnfollowEvent.

    https://devdocs.line.me/en/#unfollow-event

    Event object for when your account is blocked.
    """

    def __init__(self, timestamp=None, source=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'unfollow'


class JoinEvent(Event):
    """Webhook JoinEvent.

    https://devdocs.line.me/en/#join-event

    Event object for when your account joins a group or talk room.
    You can reply to join events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'join'
        self.reply_token = reply_token


class LeaveEvent(Event):
    """Webhook LeaveEvent.

    https://devdocs.line.me/en/#leave-event

    Event object for when your account leaves a group.
    """

    def __init__(self, timestamp=None, source=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'leave'


class PostbackEvent(Event):
    """Webhook PostbackEvent.

    https://devdocs.line.me/en/#postback-event

    Event object for when a user performs an action on
    a template message which initiates a postback.
    You can reply to postback events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, postback=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param postback: Postback object
        :type postback: :py:class:`linebot.models.events.Postback`
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'postback'
        self.reply_token = reply_token
        self.postback = self.get_or_new_from_json_dict(
            postback, Postback
        )


class BeaconEvent(Event):
    """Webhook BeaconEvent.

    https://devdocs.line.me/en/#beacon-event

    Event object for when a user detects a LINE Beacon. You can reply to beacon events.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None,
                 beacon=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param beacon: Beacon object
        :type beacon: :py:class:`linebot.models.events.Beacon`
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'beacon'
        self.reply_token = reply_token
        self.beacon = self.get_or_new_from_json_dict(
            beacon, Beacon
        )


class MemberJoinedEvent(Event):
    """Webhook MemberJoinedEvent.

    https://developers.line.biz/en/reference/messaging-api/#member-joined-event

    Event object for when a user joins a group or room that the bot is in.

    """

    def __init__(self, timestamp=None, source=None, reply_token=None,
                 joined=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param joined: Joined object
        :type joined: :py:class:`linebot.models.events.Joined`
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'memberJoined'
        self.reply_token = reply_token
        self.joined = self.get_or_new_from_json_dict(
            joined, Joined
        )


class MemberLeftEvent(Event):
    """Webhook MemberLeftEvent.

    https://developers.line.biz/en/reference/messaging-api/#member-left-event

    Event object for when a user leaves a group or room that the bot is in.

    """

    def __init__(self, timestamp=None, source=None,
                 left=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param left: Left object
        :type left: :py:class:`linebot.models.events.Left`
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'memberLeft'
        self.left = self.get_or_new_from_json_dict(
            left, Left
        )


class AccountLinkEvent(Event):
    """Webhook AccountLinkEvent.

    https://developers.line.me/en/docs/messaging-api/reference/#account-link-event

    Event object for when a user has linked his/her LINE account with a provider's service account.
    You can reply to account link events.
    If the link token has expired or has already been used,
    no webhook event will be sent and the user will be shown an error.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, link=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param link: Link object
        :type link: :py:class:`linebot.models.events.Link`
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'accountLink'
        self.reply_token = reply_token
        self.link = self.get_or_new_from_json_dict(
            link, Link
        )


class ThingsEvent(Event):
    """Webhook ThingsEvent.

    https://developers.line.biz/en/reference/messaging-api/#device-link-event

    Indicates that a LINE Things-compatible device has been linked with LINE by
    a user operation.
    """

    def __init__(self, timestamp=None, source=None, reply_token=None, things=None, **kwargs):
        """__init__ method.

        :param long timestamp: Time of the event in milliseconds
        :param source: Source object
        :type source: T <= :py:class:`linebot.models.sources.Source`
        :param str reply_token: Reply token
        :param things: Things object
        :type things: :py:class:`linebot.models.events.Things`
        :param kwargs:
        """
        super().__init__(
            timestamp=timestamp, source=source, **kwargs
        )

        self.type = 'things'
        self.reply_token = reply_token
        self.things = self.get_or_new_from_json_dict(
            things, Things
        )


class Postback(Base):
    """Postback.

    https://devdocs.line.me/en/#postback-event
    """

    def __init__(self, data=None, params=None, **kwargs):
        """__init__ method.

        :param str data: Postback data
        :param dict params: JSON object with the date and time
            selected by a user through a datetime picker action.
            Only returned for postback actions via the datetime picker.
        :param kwargs:
        """
        super().__init__(**kwargs)

        self.data = data
        self.params = params


class Beacon(Base):
    """Beacon.

    https://devdocs.line.me/en/#beacon-event
    """

    def __init__(self, type=None, hwid=None, dm=None, **kwargs):
        """__init__ method.

        :param str type: Type of beacon event
        :param str hwid: Hardware ID of the beacon that was detected
        :param str dm: Optional. Device message of beacon which is hex string
        :param kwargs:
        """
        super().__init__(**kwargs)

        self.type = type
        self.hwid = hwid
        self.dm = dm

    @property
    def device_message(self):
        """Get dm(device_message) as bytearray.

        :rtype: bytearray
        :return:
        """
        return bytearray.fromhex(self.dm) if self.dm is not None else None


class Joined(Base):
    """Joined.

    https://developers.line.biz/en/reference/messaging-api/#member-joined-event
    """

    def __init__(self, members=None, **kwargs):
        """__init__ method.

        :param dict members: Member of users who joined
        :param kwargs:
        """
        super().__init__(**kwargs)

        self._members = members

    @property
    def members(self):
        """Get members as list of SourceUser."""
        return [SourceUser(user_id=x['userId']) for x in self._members]


class Left(Base):
    """Left.

    https://developers.line.biz/en/reference/messaging-api/#member-left-event
    """

    def __init__(self, members=None, **kwargs):
        """__init__ method.

        :param dict members: Member of users who joined
        :param kwargs:
        """
        super().__init__(**kwargs)

        self._members = members

    @property
    def members(self):
        """Get members as list of SourceUser."""
        return [SourceUser(user_id=x['userId']) for x in self._members]


class Link(Base):
    """Link.

    https://developers.line.me/en/docs/messaging-api/reference/#link-object
    """

    def __init__(self, result=None, nonce=None, **kwargs):
        """__init__ method.

        :param str result: Indicate whether the link was successful or not.
        :param str nonce: Specified nonce when verifying the user ID.
        """
        super().__init__(**kwargs)

        self.result = result
        self.nonce = nonce


class Things(Base):
    """Things.

    https://developers.line.biz/en/docs/line-things/develop-bot/#link-event
    """

    def __init__(self, device_id=None, type=None, **kwargs):
        """__init__ method.

        :param str device_id: Device ID of the device that was linked with LINE.
        :param str type: link or unlink
        """
        super().__init__(**kwargs)

        self.device_id = device_id
        self.type = type
