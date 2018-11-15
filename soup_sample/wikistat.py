from bs4 import BeautifulSoup
import re
import os

# # Вспомогательная функция, её наличие не обязательно и не будет проверяться
# def build_tree(start, end, path):
#     link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
#     files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
#     # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
#     return files
#
#
# # Вспомогательная функция, её наличие не обязательно и не будет проверяться
# def build_bridge(start, end, path):
#     files = build_tree(start, end, path)
#     bridge = []
#     # TODO Добавить нужные страницы в bridge
#     return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # TODO посчитать реальные значения
        imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
        headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
        linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        lists = 20  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]

    return out



# TODO отдельная процедура для поиска ссылок по заранее скомпилированной регулярке для файла
# TODO Улучшить производительность
def find_connected_links(path, base_link):
    file_text = open(path + base_link, encoding='utf-8').read()
    soup = BeautifulSoup(file_text)
    bs_links = soup.find_all('a', {'href': re.compile(r'^/wiki/')})
    bs_hrefs = [re.sub(r'/wiki/', '', link['href']) for link in bs_links]
    return bs_hrefs
    # return dict.fromkeys(bs_hrefs, base_link)


def build_tree(path, base_link):
    tree = {}
    find_connected_links(path, base_link)

def find_route(path, start_link, end_link):
    tree_head = ['start_link', 'route', 'end_link', 'status']
    tree = [start_link, start_link, start_link, 1]
    while True:
        build_tree
        if end_link in tree:
            break


# TODO сделать проверку что в найденых destinations нет самого себя
# node_dict = {}
nodes_passed = set()
nodes = set()
edges = []
files = set(os.listdir(path))
possible_nodes = len(list(files))
start = 'Stone_Age'
end = 'Python_(programming_language)'
path = './soup_sample/wiki/'
# node_dict_part = dict.fromkeys(find_connected_links(path, start), 1)
# node_dict = {**node_dict, **node_dict_part}
# print(len(node_dict))

path_length = 0
start_edge = [None, start, 0]


def show_path(start, end, edges):
  #  starter = None
    ender = end
    result = []
    while start != ender:
        result.append(min([e for e in edges if e[1] == ender], key=lambda x: x[2]))
        ender = result[-1][0]
    return result



while True:
    # TODO проходить сперва ближайшие ноды к старту, потом перемещаться далее
    start = start_edge[1]
    cum_dist = start_edge[2]
    new_paths = set(find_connected_links(path, start)).intersection(files)
    nodes = new_paths.union(nodes)
    nodes_passed = nodes_passed.union([start])
    edges += [[start, r, cum_dist + 1] for r in new_paths.difference(start)]
    nodes_left = nodes.difference(nodes_passed)
    print('Nodes passed:{}; Nodes left:{}; Possible nodes:{}'.format(len(nodes_passed), len(nodes_left), possible_nodes))

    if end in nodes:
        print('НАШЛИ!!!')
        print(show_path(start, end, edges))
      #  [e for e in edges if e[1]==end]
        break
    elif nodes_left:
        edges_left = [e for e in edges if e[1] not in nodes_passed]
        start_edge = min(edges_left, key=lambda x: x[2])
        print(start_edge)
    else:
        break