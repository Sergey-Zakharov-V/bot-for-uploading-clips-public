from aiogram.dispatcher.filters.state import StatesGroup, State


class UploadVideoState(StatesGroup):
    add_category = State()
    upload_video = State()
