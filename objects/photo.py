class PhotoSize:
    def __init__(
            self,
            file_id,
            file_unique_id,
            file_size
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size

    @classmethod
    def photo_size_dec(cls, photo_array: list):
        photo_array_dec = list()
        for photo in photo_array:
            photo_array_dec.append(
                cls(
                    file_id=photo.get('file_id'),
                    file_unique_id=photo.get('file_unique_id'),
                    file_size=photo.get('file_size'),
                )
            )
        return photo_array_dec
