from sys import platform
from sqlite3 import IntegrityError
from datetime import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from colorama import Fore, init
from loader import dp
from data.config import admins
from states.video_upload_state import UploadVideoState
from utils.db_api import video_db

import yt_dlp

from utils.db_api.video_db import get_categories

init()

call_back = CallbackData("button", "action")

@dp.message_handler()
async def choose_category_func(message: types.Message, state: FSMContext):
    if message.text.startswith("https"):
        link = message.text
        await state.set_data(link)
        choose_category_markup = InlineKeyboardMarkup(row_width=1)
        categories = get_categories()
        for category in categories:
            choose_category_markup.add(InlineKeyboardButton(text=category[0],
                                                            callback_data=call_back.new(f"category={category[0]}")))
        choose_category_markup.add(InlineKeyboardButton(text="Новая категория", callback_data=call_back.new('newcategory')))
        choose_category_markup.add(InlineKeyboardButton(text="Отмена", callback_data=call_back.new("cancel")))
        await message.answer(text=f"{link}\nВыберите категорию видео которое хотите опубликовать", disable_web_page_preview=True, reply_markup=choose_category_markup)


@dp.callback_query_handler(lambda x: x.data.startswith("button:newcategory"))
async def new_category(call: types.CallbackQuery):
    await call.message.answer(text="Пришлите название категории(Английскими буквами без пробелов)", disable_web_page_preview=True)
    await UploadVideoState.add_category.set()


@dp.message_handler(state=UploadVideoState.add_category)
async def upload_video_with_new_category(message: types.Message, state: FSMContext):
    category = message.text
    confirm_new_category = InlineKeyboardMarkup(row_width=2)
    confirm_new_category.add(InlineKeyboardButton(text=f"Подтвердить {category}", callback_data=call_back.new(f"category={category}")))
    confirm_new_category.add(InlineKeyboardButton(text="Отмена", callback_data=call_back.new("cancel")))
    link = await state.get_data()
    await message.answer(f"{link}\nПодтвердите создание новой категории", reply_markup=confirm_new_category)
    await state.reset_state()


@dp.callback_query_handler(lambda x: x.data.startswith("button:category="))
async def upload_video_func(call: types.CallbackQuery):
    if call.message.chat.id in admins:
        video_link = call.message.text.split("\n")[0]
        category = call.data.split("=")[1]
        print(video_link)
        if video_link.startswith("https://vk.com"):
            file_name = video_link.replace("-", "").replace("%", "")
        else:
            file_name = video_link.split("=")[1].replace("-", "").replace("%", "")
        if platform == "linux" or platform == "linux2":
            params = {
                "format": "bestvideo[width=1920][fps=30][ext=mp4]+bestaudio[ext=m4a]/best[width=1920][fps=30][ext=mp4]",
                'fps': 30,
                'outtmpl': f'/usr/local/bin/botwithclips/clips/{file_name}.mp4'
        }
        elif platform == "win32":
            params = {
                "format": "bestvideo[width=1920][fps=30][ext=mp4]+bestaudio[ext=m4a]/best[width=1920][fps=30][ext=mp4]",
                'fps': 30,
                'outtmpl': f'C:\\Users\\KENT SZ\\PycharmProjects\\botwithclips\\clips\\{file_name}.mp4'
        }
        try:
            with yt_dlp.YoutubeDL(params) as ydl:
                ydl.download(video_link)
                video_db.add_video(category=category,
                                   link=video_link,
                                   upload_date=datetime.now(),
                                   path=f'clips/{file_name}.mp4')
                await call.message.reply("Готово!")
                await call.message.edit_reply_markup()
        except yt_dlp.utils.DownloadError as e:
            print(Fore.RED, e, Fore.RESET)
            await call.message.answer("Данный формат не поддерживается :(")
        except IntegrityError as e:
            print(Fore.RED, e, Fore.RESET)
            await call.message.answer("Такой клип уже есть :(")


@dp.callback_query_handler(lambda x: x.data.startswith("button:cancel"))
async def cancel(call: types.CallbackQuery):
    await call.message.delete()
