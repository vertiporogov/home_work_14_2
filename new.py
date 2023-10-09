import json


class Raf9:

    def __init__(self):
        self.ingredients = ['lemon', 'mint', 'ice', 'soda', 'orange', 'tomato']
        self.get_coctail_from_db()

    def __call__(self, *args, **kwargs):
        while True:
            self.__help_text()
            command = input('Введите команду')
            if command == '0':
                print('Всего хорошего. Приходите еще')
                break
            elif command == '1':
                current_ings = self.choose_ingredient()
                chose_coctail = self.find_coctail(current_ings)
                if chose_coctail is None:
                    self.save_coctail(current_ings)
                else:
                    print(f'you chose {chose_coctail} coctail')
            else:
                print('Не знаю такой команды')

    def __help_text(self):
        print('Доступны команды:')
        print('1 - выберите ингридиенты')
        print('0 - выход')

    def save_coctail(self, current_ings):
        self.coctails.append({
            'name': 'unname',
            'ingredients': current_ings
        })

        with open('coctail.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.coctails, json_file)

    def get_coctail_from_db(self):
        with open('coctail.json', 'r', encoding='utf-8') as json_file:
            self.coctails = json.load(json_file)

    def find_coctail(self, current_ings):
        for c in self.coctails:
            if c.get('ingredients') == current_ings:
                return c.get('name')

        return None

    def choose_ingredient(self):
        chose_ing = []
        print('Список ингредиентов:')

        count = 0
        for ing in self.ingredients:
            count += 1
            print(f'{count}. {ing}')

        print('0 - для выхода')

        while True:
            command = input('Введите команду')
            if command == '0':
                return chose_ing
            else:
                if command.isdigit():
                    number = int(command)
                    if number > len(self.ingredients):
                        print('Такого ингредиента нет')
                    else:
                        chose_ing.append(self.ingredients[number - 1])
                else:
                    print('Введите номер ингредиента')


raf9 = Raf9()
# raf9()

assert 'mojito' == raf9.find_coctail(["ice", "soda", "mint"])
