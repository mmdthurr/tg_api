from .objects.user import User
from .objects.voice import Voice
from .objects.chat import Chat


class Message:
    def __init__(
            self,
            message_id: int,
            from_user: User,
            sender_chat: Chat,
            reply_to_message: 'Message',
            text: str,
            audio,
            photo,
            video,
            voice,
            caption,
            caption_entities,
            entities: list
    ):
        self.message_id = message_id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.reply_to_message = reply_to_message
        self.text = text
        self.audio = audio
        self.photo = photo
        self.video = video
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.entities = entities

    @property
    def arg(self):
        if self.text:
            if self.entities:
                if self.text.startswith('/'):
                    arg = self.text.split(' ')
                    del arg[0]
                    return arg

    @classmethod
    def message_dec(cls, message: dict):
        if message:
            return cls(
                message_id=message.get('message_id'),
                from_user=User.user_dec(message.get('from')),
                sender_chat=Chat.chat_dec(message.get('sender_chat')),
                reply_to_message=Message.message_dec(message.get('reply_to_message')),
                text=message.get('text'),
                audio=message.get('audio'),
                photo=message.get('photo'),
                video=message.get('video'),
                voice=Voice.voice_dec(message.get('voice')),
                caption=message.get('caption'),
                caption_entities=message.get('caption_entities'),
                entities=message.get('entities')
            )
