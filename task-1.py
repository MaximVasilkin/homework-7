# Задача-1.

def file_to_pydict(file):
	with open(file, encoding='utf-8') as text:
		cook_book = {}
		dish = ''
		for line in text:
			line = line.strip('\n')
			if line and '|' not in line and not line.isdigit():
				dish = line
				cook_book[dish] = []
			elif '|' in line:
				ingridients = line.split(' | ')
				cook_book[dish].append({'ingredient_name': ingridients[0],
										'quantity': int(ingridients[1]),
										'measure': ingridients[2]})
		return cook_book


print(file_to_pydict('recipes.txt'))

# Задача-2.

def get_shop_list_by_dishes(dishes, person_count):
	cook_book = file_to_pydict('recipes.txt')
	shop_list = {}
	for dish in dishes:
		if dish in cook_book:
			for dict in cook_book[dish]:
				if dict['ingredient_name'] in shop_list:
					shop_list[dict['ingredient_name']]['quantity'] += dict['quantity'] * person_count
				else:
					shop_list[dict['ingredient_name']] = {'measure': dict['measure'],
															'quantity': dict['quantity'] * person_count}
		else:
			return f'Блюдо "{dish}" в книге не найдено!'
	return shop_list


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

# Задача-3.

import os


def all_in_one(folder):
	files = os.listdir(path=folder)
	txts = {}
	for file in files:
		with open(f'sorted/{file}', encoding='utf-8') as txt:
			files_content = txt.readlines()
			txts[file] = [len(files_content), ''.join(files_content).strip('\n')]
	txts = dict(sorted(txts.items(), key=lambda item: item[1][0]))
	for k, v in txts.items():
		with open('new.txt', 'a', encoding='utf-8') as result:
			result.write(f'{k}\n{v[0]}\n{v[1]}\n')


all_in_one('sorted')
