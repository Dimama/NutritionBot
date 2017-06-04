class Calculator(object):
    """ Класс для математических расчетов основного обмена"""
    def __init__(self, sex, age, height, weight):
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight

    @staticmethod
    def calc_product_energy(mass, protein100, fat100, carbs100, calories100):
        coef = mass / 100
        protein = protein100 * coef
        fat = fat100 * coef
        carbs = carbs100 * coef
        calories = calories100 * coef

        return protein, fat, carbs, calories

    def calc_BX(self):
        """ Расчет основного обмена и обмен для групп физ. активности"""
        calories = [0] * 5

        if self.sex == "м":
            calories[0] = 66.5 + 13.7 * self.weight + 5 * self.height - 6.8 * self.age
        else:
            calories[0] = 665 + 9.5 * self.weight + 1.8 * self.height - 4.7 * self.age
        calories[1] = calories[0] * 1.4
        calories[2] = calories[0] * 1.6
        calories[3] = calories[0] * 1.9
        calories[4] = calories[0] * 2.2

        protein = [self.weight * 0.83] * 5
        carbs = [0] * 5
        fat = [0] * 5
        for i in range(0, 5):
            carbs[i] = calories[i] * 0.55 / 4.1
            fat[i] = (calories[i] - calories[i] * 0.55 - protein[i] * 4.1) / 9.0

        result = {"calories": calories,
                  "protein": protein,
                  "carbs": carbs,
                  "fat": fat}

        return result





