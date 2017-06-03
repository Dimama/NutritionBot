class Calculator(object):
    """ Класс для математических расчетов основного обмена"""
    @staticmethod
    def calc_product_energy(mass, protein100, fat100, carbs100, calories100):
        coef = mass / 100
        protein = protein100 * coef
        fat = fat100 * coef
        carbs = carbs100 * coef
        calories = calories100 * coef

        return protein, fat, carbs, calories