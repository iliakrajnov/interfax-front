import pymorphy2


#Удаление из набора найденных слов мусорных
def rubbish_deleter(data):
    with open('rubbish.txt') as file:
        to_delete = set(file.read().split('\n'))
    return set(data) - to_delete


#Чистка от лишних символов, предварительная подготовка
def clear(string):
    string = string.lower()
    for i in list('''!#$%&'()*+,—./:;<=>?@[\]^_`{|}~'''):
        string = string.replace(i, ' ')

    return string.replace('   ', ' ').replace('  ', ' ')



#Извлечение ключевых слов
def get_key_words(text):
    morph = pymorphy2.MorphAnalyzer()

    data = []
    for word in clear(text).split():
        pm_word = morph.parse(word)[0]
        if pm_word.tag.POS in ['NOUN', 'VERB', 'ADJS', 'ADJF', 'INFN', 'NUMR']:     #Нам нужны только сущ., гл., пр., числ.
            data.append(pm_word.normal_form)        #В начальной форме добавляем в список

    return rubbish_deleter(data)        #чистим от мусорных слов



#Получение статистики по ключевым словам по статьям одного сюжета
def train(data):
    not_sorted_res = {}

    for i in data:     #Отдельные новости разделены ---
        for j in get_key_words(i):      # Получаем ключевые слова и учитываем
            try:
                not_sorted_res[j] += 1
            except KeyError:
                not_sorted_res[j] = 1

    res = {}    #Получаем сортированый словарь с процентами встречающихся слов
    for i in sorted(not_sorted_res, key=not_sorted_res.get, reverse=True):
        percent = not_sorted_res[i] / len(data)        #Количество встреч на количество статей
        if percent >= 0.75:       #Редкие данные не интересуют - мешают картине
            res[i] = percent
    return res


#Определение подходит ли текст к сюжету
def text_filter(text, tr):
    summ = 0
    for i in get_key_words(text):   #Проходим по ключевым словам в тексте
        if i in tr:     #Если слово в выборке - добавляем баллы
            summ += tr[i]

    return summ / sum(tr.values())      #Полученные баллы делим на максимум

