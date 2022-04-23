from enum import Enum, unique


@unique
class Switch(Enum):
    Current = 'switch_inline_query_current_chat'
    Other = 'switch_inline_query'


def reply_markup(
        keyboard,
        resize_keyboard,
        one_time_keyboard,
        input_field_placeholder,
        selective
):
    markup = {
        'keyboard': keyboard,
    }
    if resize_keyboard:
        markup['resize_keyboard'] = resize_keyboard
    if one_time_keyboard:
        markup['one_time_keyboard'] = one_time_keyboard
    if input_field_placeholder:
        markup['input_field_placeholder'] = input_field_placeholder
    if selective:
        markup['selective'] = selective
    return markup


def inline_markup(
        inline_keyboard: list
):
    markup = {
        'inline_keyboard': inline_keyboard
    }
    return markup


def keyboard_button(
        text: str,
        request_contact: bool = None,
        request_location: bool = None,
):
    button = {
        'text': text,
    }
    if request_contact:
        button['request_contact'] = request_contact
    if request_location:
        button['request_location'] = request_location
    return button


def inline_button(
        text: str,
        url: str = None,
        callback_data: str = None
):
    button = {
        'text': text
    }
    if url:
        button['url'] = url
    if callback_data:
        button['callback_data'] = callback_data
    return button


def switch_inline(
        text: str,
        switch_str: str = '',
        switch: Switch = Switch.Current,
):
    button = {
        'text': text,
        switch.value: switch_str,
    }
    return button
