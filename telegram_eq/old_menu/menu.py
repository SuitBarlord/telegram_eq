from email import message
from telebot import types # для указание типов
from transliterate import translit
import mysql_query as query


async def build_inline_menu(arr_menu, id, message, bot):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    



    markup = types.InlineKeyboardMarkup()
    for item in arr_menu:
        data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
        print(data, 44444444444444444444444)
        markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    res_message = await bot.send_message(id, message, reply_markup=markup)
    # query.sql_init.update_last_id_menu(id, res_message.message_id)

    return markup, res_message

async def build_inline_menu_edit(arr_menu, id, bot, message_id, text_message):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    



    markup = types.InlineKeyboardMarkup()
    for item in arr_menu:
        if item == 'Назад':
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))

        data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
        print(data, 44444444444444444444444)
        markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    res_message = await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
    await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)





    return markup, res_message















import math

ITEMS_PER_PAGE = 8  # Количество элементов на одной странице



async def build_inline_menu_edit_t_p(arr_menu, id, bot, message_id, text_message, page=1):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    


    markup = types.InlineKeyboardMarkup()
    total_pages = math.ceil(len(arr_menu) / ITEMS_PER_PAGE)
    start_index = (page - 1) * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE

    
    for item in arr_menu[start_index:end_index]:
        if item == 'Назад':
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))

        data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
        print(data, 44444444444444444444444)
        markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))

    if total_pages > 1:
        text_message = text_message + f" (Страница {page}/{total_pages})"
        if page > 1:
            markup.row(types.InlineKeyboardButton("⬅️ Предыдущая", callback_data=f"paget_{page - 1}"))
        if page < total_pages:
            markup.row(types.InlineKeyboardButton("Следующая ➡️", callback_data=f"paget_{page + 1}"))
        markup.row(types.InlineKeyboardButton("Вернуться в главное меню", callback_data="Vernut'sja_v_glavnoe_menju"))

    res_message = await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
    await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)





    return markup, res_message
















async def build_inline_menu_edit_date(arr_menu, id, bot, message_id, text_message):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    



    markup = types.InlineKeyboardMarkup()
    for item in arr_menu:
        if item == 'Назад':
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        
        if item == "Вернуться в главное меню":
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        else:

            from datetime import datetime
            date_obj = datetime.strptime(str(item).replace("На дату ", ""), "%Y-%m-%d")
            new_date_str = date_obj.strftime("%d.%m.%Y")


            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str("На дату " + new_date_str), callback_data=data))
        # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    res_message = await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
    await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)





    return markup, res_message







import math

ITEMS_PER_PAGE = 8  # Количество элементов на одной странице

async def build_inline_menu_edit_date_p(arr_menu, id, bot, message_id, text_message, page=1):
    markup = types.InlineKeyboardMarkup()
    total_pages = math.ceil(len(arr_menu) / ITEMS_PER_PAGE)
    start_index = (page - 1) * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE

    for item in arr_menu[start_index:end_index]:
        if item == 'Назад':
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True)).split('_(')[0]
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))

        if item == "Вернуться в главное меню":
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True)).split('_(')[0]
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))

        else:
            from datetime import datetime
            date_obj = datetime.strptime(str(item).replace("На дату ", ""), "%Y-%m-%d")
            new_date_str = date_obj.strftime("%d.%m.%Y")

            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True)).split('_(')[0]
            markup.row(types.InlineKeyboardButton(text=str("На дату " + new_date_str), callback_data=data))

    # Добавляем кнопки для навигации по страницам
    if total_pages > 1:
        text_message = text_message + f" (Страница {page}/{total_pages})"
        if page > 1:
            markup.row(types.InlineKeyboardButton("⬅️ Предыдущая", callback_data=f"paged_{page - 1}"))
        if page < total_pages:
            markup.row(types.InlineKeyboardButton("Следующая ➡️", callback_data=f"paged_{page + 1}"))
        markup.row(types.InlineKeyboardButton("Вернуться в главное меню", callback_data="Vernut'sja_v_glavnoe_menju"))

    res_message = await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
    await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)

    return markup, res_message










# ITEMS_PER_PAGE = 5  # Количество элементов на одной странице

# async def build_inline_menu_talons_edit(arr_menu, id, message_id, bot, text_message, page=1):
#     markup = types.InlineKeyboardMarkup()
#     total_pages = math.ceil(len(arr_menu) / ITEMS_PER_PAGE)
#     start_index = (page - 1) * ITEMS_PER_PAGE
#     end_index = start_index + ITEMS_PER_PAGE

#     for item in arr_menu[start_index:end_index]:
#         data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True)).split(',_')[-1]
#         markup.row(types.InlineKeyboardButton(text=str(item).split(', ПИН - ')[0], callback_data=data))

#     # Добавляем кнопки для навигации по страницам
#     if total_pages > 1:
#         text_message = text_message + str(page)
#         if page > 1:
#             # text_message = text_message + str(page)
#             markup.row(types.InlineKeyboardButton("⬅️ Предыдущая", callback_data=f"page_{page - 1}"))
#         if page < total_pages:
#             # text_message = text_message + str(page)
#             markup.row(types.InlineKeyboardButton("Следующая ➡️", callback_data=f"page_{page + 1}"))
#             markup.row(types.InlineKeyboardButton("Вернуться в главное меню", callback_data=f"Vernut'sja_v_glavnoe_menju"))

#     await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
#     await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)

#     return markup




























async def build_inline_menu_edit_filials(arr_menu, id, bot, message_id, text_message, filials_adress):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    



    markup = types.InlineKeyboardMarkup()
    for item in arr_menu:
        if item == 'Назад':
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))

        if item == "Вернуться в главное меню":
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        else:
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 44444444444444444444444)
            import string
            markup.row(types.InlineKeyboardButton(text=str(filials_adress[data]).lstrip(string.digits).replace("Забайкальский край,", ""), callback_data=data))
            # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    res_message = await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
    await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)





    return markup, res_message





async def build_inline_menu_edit_col(arr_menu, id, group, bot, message_id, text_message):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    



    markup = types.InlineKeyboardMarkup()
    print(arr_menu, 'aaaaaaaaaaaaaaaaaaaarrrrrrrrrrrrrrrrrrr')
    for item in arr_menu:
        if item == 'Назад':
            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 888888888888888888888888888888888888888)
            if group == 'Социальная поддержка населения':

                data = "Perejti_k_" + "Sotsial'naja_podderzhka_naselenija"
            elif group == 'Налоги и предпринимательская деятельность':
                data = "Perejti_k_" + "Nalogi_i_predprinimatel'skaja_dejatel'nost'"
            else:
                data = "Perejti_k_" + group
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        else:

            data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
            # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
    await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)

    # return markup

async def build_inline_menu_edit_usluga(arr_menu, dict, id, bot, message_id, text_message):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    



    markup = types.InlineKeyboardMarkup()
    # for item in arr_menu:
    #     data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
    #     print(data, 44444444444444444444444)
    #     markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    for key, value in dict.items():
        if key == 'Назад':
            data = str(translit(str(value).replace(' ', '_'), 'ru', reversed=True ))
            markup.row(types.InlineKeyboardButton(text=str(key), callback_data=data))
            # print(data, 888888888888888888888888888888888888888888)
        else:
            data = "Usluga_" + str(value)
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(key), callback_data=data))
            # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
    await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)

    # return markup

async def build_inline_menu_edit_group(arr_menu, dict, id, bot, message_id, text_message):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    



    markup = types.InlineKeyboardMarkup()
    for item in arr_menu:
        data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
        print(data, 44444444444444444444444)
        markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    for key, value in dict.items():
        if key == 'Назад':
            data = str(translit(str(value).replace(' ', '_'), 'ru', reversed=True ))
            markup.row(types.InlineKeyboardButton(text=str(key), callback_data=data))
            print(data, 888888888888888888888888888888888888888888)
        else:
            data = "Usluga_" + str(value)
            print(data, 44444444444444444444444)
            markup.row(types.InlineKeyboardButton(text=str(key), callback_data=data))
            # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
    await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)


async def build_inline_menu_usluga(arr_menu, dict, id, message, bot):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    



    markup = types.InlineKeyboardMarkup()
    for item in arr_menu:
        data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split('_(')[0]
        print(data, 44444444444444444444444)
        markup.row(types.InlineKeyboardButton(text=str(item), callback_data=data))
        # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    for key, value in dict.items():
        data = "Usluga_" + str(value)
        print(data, 44444444444444444444444)
        markup.row(types.InlineKeyboardButton(text=str(key), callback_data=data))
    await bot.send_message(id, message, reply_markup=markup)


    return markup

async def build_inline_menu_talons(arr_menu, id, message, bot):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    



    markup = types.InlineKeyboardMarkup()
    for item in arr_menu:
        data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split(',_')[-1]
        # print(data, 44444444444444444444444)
        markup.row(types.InlineKeyboardButton(text=str(item).split(', ПИН - ')[0], callback_data=data))
        # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
    await bot.send_message(id, message, reply_markup=markup)


    return markup

# async def build_inline_menu_talons_edit(arr_menu, id, message_id, bot, text_message):
#     # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     # keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
#     # await bot.send_message(id, message,
#     #     reply_markup=keyboard)
    



#     markup = types.InlineKeyboardMarkup()
#     for item in arr_menu:
#         data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True )).split(',_')[-1]
#         # print(data, 44444444444444444444444)
#         markup.row(types.InlineKeyboardButton(text=str(item).split(', ПИН - ')[0], callback_data=data))
#         # print(translit(str(item).replace(' ', '_').split("(Konsul'tatsija)")[0], 'ru', reversed=True))
#     await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
#     await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)

#     return markup



import math

ITEMS_PER_PAGE = 8  # Количество элементов на одной странице

async def build_inline_menu_talons_edit(arr_menu, id, message_id, bot, text_message, page=1):
    markup = types.InlineKeyboardMarkup()
    total_pages = math.ceil(len(arr_menu) / ITEMS_PER_PAGE)
    start_index = (page - 1) * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE

    for item in arr_menu[start_index:end_index]:
        data = str(translit(str(item).replace(' ', '_'), 'ru', reversed=True)).split(',_')[-1]
        markup.row(types.InlineKeyboardButton(text=str(item).split(', ПИН - ')[0], callback_data=data))

    # Добавляем кнопки для навигации по страницам
    if total_pages > 1:
        text_message = text_message + str(page)
        if page > 1:
            # text_message = text_message + str(page)
            markup.row(types.InlineKeyboardButton("⬅️ Предыдущая", callback_data=f"page_{page - 1}"))
        if page < total_pages:
            # text_message = text_message + str(page)
            markup.row(types.InlineKeyboardButton("Следующая ➡️", callback_data=f"page_{page + 1}"))
            markup.row(types.InlineKeyboardButton("Вернуться в главное меню", callback_data=f"Vernut'sja_v_glavnoe_menju"))

    await bot.edit_message_reply_markup(chat_id=id, message_id=message_id, reply_markup=markup)
    await bot.edit_message_text(chat_id=id, message_id=message_id, text=text_message, reply_markup=markup)

    return markup



async def build_menu(arr_menu, id, message, bot):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    await bot.send_message(id, message,
        reply_markup=keyboard)
    return keyboard

async def build_menu_2_coll(arr_menu, id, message, bot):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[types.KeyboardButton(name) for name in arr_menu])
    await bot.send_message(id, message,
        reply_markup=keyboard)
    return keyboard

async def remove_menu(id, message, bot):
    keyboard = types.ReplyKeyboardRemove()
    # await bot.send_message(id, message,
    #     reply_markup=keyboard)
    
async def request_phone(id, bot):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reg_button = types.KeyboardButton(text="Отправить номер телефона", 
    request_contact=True)
    keyboard.add(reg_button)
    await bot.send_message(id, 'Оставьте ваш контактный номер чтобы наш менеджер смог связаться с вами. ', reply_markup=keyboard)