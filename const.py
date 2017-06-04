from answerer import Answerer

info_dict = {
    "Статистика за день": Answerer.stat_by_day_info,
    "за период": Answerer.stat_by_period_info,
    "Добавить продукт": Answerer.add_product_info,
    "Ввести/Обновить личные данные": Answerer.set_update_data_info,
    "Помощь": Answerer.bot_info,
}

reg_exp_dict = {
    "user data": r'\s*[мМжЖ],\s*[1-9]{1}[0-9]{,2},\s*[1-9]{1}[0-9]{,2},\s*[1-9]{1}[0-9]{,2}\s*$',
    "product_by_name": r'\s*[\w,\s,\-,\.,(,),\',%]+\s*:\s*[1-9]{1}[0-9]{,5}\s*$',
    "product_by_id": r'\s*\*[0-9]+\s*:\s*[1-9]{1}[0-9]{,5}\s*$',
    "day": r'\s*[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s*$',
    "period": r'\s*[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s*-'
              r'\s*[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s*$',
}

MAX_AGE = 100
MAX_HEIGHT = 230
MAX_WEIGHT = 300
MAX_PRODUCT_MASS = 10000

error_emoji = u'\U00002757'
sad_emoji = u'\U0001F614'
success_emoji = u'\U00002705'
pencil_emoji = u'\U0000270F'
warning_emoji = u'\U000026A0'

study_emoji = u'\U0001F393'
computer_emoji = u'\U0001F4BB'
policeman_emoji = u'\U0001F46E'
haircut_emoji = u'\U0001F487'
tractor_emoji = u'\U0001F69C'
wrench_emoji = u'\U0001F527'
biceps_emoji = u'\U0001F4AA'
bycyclist_emoji = u'\U0001F6B4'
sleep_emoji = u'\U0001F4A4'
moon_emoji = u'\U0001F319'
diagram_emoji = u'\U0001F4CA'
calendar_emoji = u'\U0001F4C5'
