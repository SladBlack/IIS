# coding:utf-8
import gensim
from gensim.models import word2vec
import gensim.downloader as api

model_path = 'model.txt'
model_ru = api.load("word2vec-ruscorpora-300")

# массив слов
words = ['огурец_NOUN', 'арбуз_NOUN', 'жареная курица_NOUN', 'кровать_NOUN', 'сон_NOUN']
for word in words:
    # есть ли слово в модели?
    if word in model_ru:
        print(word)
        # смотрим на вектор слова (его размерность 300, смотрим на первые 10 чисел)
        print(model_ru[word][:10])
        # выдаем 10 ближайших соседей слова:
        for word, sim in model_ru.most_similar(positive=[word], topn=10):
            # слово + коэффициент косинусной близости
            print(word, ': ', sim)
            print('\n')
    else:
        print('Слова "%s" нет в модели!' % word)
# степень схожести слов по смыслу
print(model_ru.similarity('диван_NOUN', 'кресло_NOUN'))
# "складываем" слова
print(model_ru.most_similar(positive=['кровать_NOUN', 'сон_NOUN'])[0][0])
# "вычитаем" слова
print(model_ru.most_similar(negative=['мясо_NOUN', 'тарелка_NOUN'])[0][0])
print(model_ru.most_similar(positive=['банан_NOUN', 'песок_NOUN'], negative=['уксус_NOUN'])[0][0])
# ищет "лишнии" слова
print(model_ru.doesnt_match('коза_NOUN рыба_NOUN гречка_NOUN осел_NOUN'.split()))
