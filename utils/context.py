class Context:
    def __init__(
            self
    ):

        self._user_data = dict()
        self._user_lang = dict()
        self._conv_stage = dict()
        self._updates_ids = list()

    def user_data(self, user_id):
        return self._user_data.get(user_id)

    def user_data_setter(self, user_id, data):
        self._user_data[user_id] = data

    def user_lang(self, user_id):
        return self._user_lang.get(user_id)

    def user_lang_setter(self, user_id, lang):
        self._user_lang[user_id] = lang

    def user_conv_stage(self, user_id):
        return self._conv_stage.get(user_id)

    def user_conv_stage_setter(self, user_id, stage):
        self._conv_stage[user_id] = stage

    def update_id_is_used(self, update_id):
        if update_id in self._updates_ids:
            if len(self._updates_ids) == 10:
                self._updates_ids.clear()
            return True
        else:
            self._updates_ids.append(update_id)
            return False
