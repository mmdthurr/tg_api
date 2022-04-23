def result_article(
        inline_id,
        title,
        input_message_content,
        reply_markup=None,
        url=None,
        hide_url=None,
        description=None,
        thumb_url=None,
):
    result = {
        'type': 'article',
        'id': inline_id,
        'title': title,
        'input_message_content': input_message_content
    }
    if reply_markup:
        result['reply_markup'] = reply_markup
    if url:
        result['url'] = url
    if hide_url:
        result['hide_url'] = hide_url
    if description:
        result['description'] = description
    if thumb_url:
        result['thumb_url'] = thumb_url
    return result


def result_photo(
        inline_id,
        photo_url,
        thumb_url,
        photo_width=512,
        photo_height=512,
        title=None,
        description=None,
        caption=None,
        parse_mode=None,
        reply_markup=None,
        input_message_content=None
):
    result = {
        'type': 'photo',
        'id': inline_id,
        'photo_url': photo_url,
        'thumb_url': thumb_url,
        'photo_width': photo_width,
        'photo_height': photo_height
    }
    if title:
        result['title'] = title
    if description:
        result['description'] = description
    if caption:
        result['caption'] = caption
    if parse_mode:
        result['parse_mode'] = parse_mode
    if reply_markup:
        result['reply_markup'] = reply_markup
    if input_message_content:
        result['input_message_content'] = input_message_content
    return result


def result_cached_voice(
        inline_id,
        voice_file_id,
        title,
        caption=None,
        parse_mode=None,
        caption_entities=None,
        reply_markup=None,
        input_message_content=None
):
    result = {
        'type': 'voice',
        'id': inline_id,
        'voice_file_id': voice_file_id,
        'title': title,
    }
    if caption:
        result['caption'] = caption
    if parse_mode:
        result['parse_mode'] = parse_mode
    if caption_entities:
        result['caption_entities'] = caption_entities
    if reply_markup:
        result['reply_markup'] = reply_markup
    if input_message_content:
        result['input_message_content'] = input_message_content


def result_gif(
        inline_id,
        gif_url,
        thumb_url,
        gif_width=512,
        gif_height=512,
        title=None,
        caption=None,
        parse_mode=None,
        reply_markup=None,
):
    result = {
        'type': 'gif',
        'id': inline_id,
        'gif_url': gif_url,
        'thumb_url': thumb_url,
        'gif_width': gif_width,
        'gif_height': gif_height
    }
    if title:
        result['title'] = title

    if caption:
        result['caption'] = caption
    if parse_mode:
        result['parse_mode'] = parse_mode
    if reply_markup:
        result['reply_markup'] = reply_markup
    return result
