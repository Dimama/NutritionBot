from handler import Handler

info_dict = {
    "Статистика за день": Handler.stat_by_day_info,
    "за период": Handler.stat_by_period_info,
    "Добавить продукт": Handler.add_product_info,
    "Ввести/Обновить личные данные": Handler.set_update_data_info,
    "Помощь": Handler.instruction_info,
}
