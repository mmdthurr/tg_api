from enum import Enum, unique
from .utils.utils import Url


@unique
class Methods(Enum):
    sendVideo = 'sendVideo'
    sendMessage = 'sendMessage'
    copyMessage = 'copyMessage'
    answerCallbackQuery = 'answerCallbackQuery'
    answerInlineQuery = 'answerInlineQuery'
    deleteMessage = 'deleteMessage'
    editMessageText = 'editMessageText'
    editMessageReplyMarkup = 'editMessageReplyMarkup'
    getChat = 'getChat'


class Bot:
    def __init__(
            self,
            token,
            session,
            context,
            update
    ):
        self.token = token
        self.session = session
        self.context = context
        self.update = update

    def request_(self, method: Methods, param: dict):
        url = Url('https://api.telegram.org/bot').url_join(f'{self.token}/{method.value}')
        return self.session.post(url, json=param)

    def send_message(
            self,
            chat_id,
            text,
            parse_mode=None,
            entities=None,
            disable_web_page_preview=True,
            reply_to_message_id=None,
            allow_sending_without_reply=True,
            reply_markup=None
    ):

        param = {
            'chat_id': chat_id,
            'text': text
        }
        if parse_mode:
            param['parse_mode'] = parse_mode
        if entities:
            param['entities'] = entities
        if disable_web_page_preview:
            param['disable_web_page_preview'] = disable_web_page_preview
        if reply_to_message_id:
            param['reply_to_message_id'] = reply_to_message_id
            param['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup:
            param['reply_markup'] = reply_markup
        return self.request_(Methods.sendMessage, param)

    def send_video(
            self,
            chat_id,
            video,
            caption=None,
            parse_mode=None,
            caption_entities=None,
            reply_to_message_id=None,
            allow_sending_without_reply=True,
            reply_markup=None
    ):
        param = {
            'chat_id': chat_id,
            'video': video,
        }
        if caption:
            param['caption'] = caption
        if parse_mode:
            param['parse_mode'] = parse_mode
        if caption_entities:
            param['caption_entities'] = caption_entities
        if reply_to_message_id:
            param['reply_to_message_id'] = reply_to_message_id
            param['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup:
            param['reply_markup'] = reply_markup
        return self.request_(Methods.sendVideo, param)

    def copy_message(
            self,
            chat_id,
            from_chat_id,
            message_id: int,
            reply_to_message_id: int,
            allow_sending_without_reply: True,
            reply_markup
    ):
        param = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id,
            'allow_sending_without_reply': allow_sending_without_reply
        }
        if reply_to_message_id:
            param['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            param['reply_markup'] = reply_markup

        return self.request_(Methods.copyMessage, param)

    def answer_callback_query(
            self,
            callback_query_id: str,
            text: str = None,
            show_alert: bool = None,
            url: str = None,
            cache_time: int = None
    ):
        param = {
            'callback_query_id': callback_query_id,
        }
        if text:
            param['text'] = text
        if show_alert:
            param['show_alert'] = show_alert
        if url:
            param['url'] = url
        if cache_time:
            param['cache_time'] = cache_time
        return self.request_(Methods.answerCallbackQuery, param)

    def answer_inline_query(
            self,
            inline_query_id: str,
            results: list,
            cache_time: int = 0,
            is_personal: bool = None,
            next_offset: str = None,
            switch_pm_text: str = None,
            switch_pm_parameter: str = None
    ):
        param = {
            'inline_query_id': inline_query_id,
            'results': results,
        }
        if cache_time:
            param['cache_time'] = cache_time
        if is_personal:
            param['is_personal'] = is_personal
        if next_offset:
            param['next_offset'] = next_offset
        if switch_pm_text:
            param['switch_pm_text'] = switch_pm_text
            param['switch_pm_parameter'] = switch_pm_parameter
        return self.request_(Methods.answerInlineQuery, param)

    def delete_message(
            self,
            chat_id,
            message_id
    ):
        param = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        return self.request_(Methods.deleteMessage, param)

    def edit_message_text(
            self,
            chat_id,
            message_id,
            inline_message_id,
            text,
            parse_mode,
            entities,
            reply_markup
    ):
        param = {
            'text': text,
        }
        if chat_id:
            param['chat_id'] = chat_id
        if message_id:
            param['message_id'] = message_id
        if inline_message_id:
            param['inline_message_id'] = inline_message_id
        if parse_mode:
            param['parse_mode'] = parse_mode
        if entities:
            param['entities'] = entities
        if reply_markup:
            param['reply_markup'] = reply_markup
        return self.request_(Methods.editMessageText, param)

    def edit_message_reply_markup(
            self,
            chat_id,
            message_id=None,
            inline_message_id=None,
            reply_markup=None
    ):
        param = {
            'chat_id': chat_id
        }
        if message_id:
            param['message_id'] = message_id
        if inline_message_id:
            param['inline_message_id'] = inline_message_id
        if reply_markup:
            param['reply_markup'] = reply_markup
        return self.request_(Methods.editMessageReplyMarkup, param)

    def get_chat(
            self,
            chat_id
    ):
        param = {
            'chat_id': chat_id
        }
        return self.request_(Methods.getChat, param)

    @property
    def user_data(self):
        return self.context.user_data(
            self.update.current_user.user_id
        )

    @user_data.setter
    def user_data(self, data):
        self.context.user_data_setter(
            user_id=self.update.current_user.user_id,
            data=data
        )

    def remove_user_data(self):
        self.context.user_data_remover(user_id=self.update.current_user.user_id)
