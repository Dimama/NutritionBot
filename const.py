from handler import Handler

info_dict = {
    "Статистика за день": Handler.stat_by_day_info,
    "за период": Handler.stat_by_period_info,
    "Добавить продукт": Handler.add_product_info,
    "Ввести/Обновить личные данные": Handler.set_update_data_info,
    "Помощь": Handler.instruction_info,
}

reg_exp_dict = {
    "user data": r'\s*[мМжЖ], [1-9]{1}[0-9]{,1}, [1-9]{1}[0-9]{,2}, [1-9]{1}[0-9]{,2}\s*$',
    "product": r'\s*[\w,\s]+\s+-\s+[1-9]{1}[0-9]{,3}\s*$',
    "day": r'\s*[0-3][0-9]\.[0-1][0-9]\.[2][0-1][0-9][0-9]\s*$',
    "period": r'\s*[0-3][0-9]\.[0-1][0-9]\.[2][0-1][0-9][0-9]\s*-'
              r'\s*[0-3][0-9]\.[0-1][0-9]\.[2][0-1][0-9][0-9]\s*$',
}
