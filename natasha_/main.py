# Импортируем модули
import pprint

from translate import TRANSLATE_DICT

from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    NamesExtractor,
    DatesExtractor,
    Doc
)

# Считываем текст в переменную
file_path = 'text.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Инициализация модулей
segmenter = Segmenter()
morph_vocab = MorphVocab()
dates_extractor = DatesExtractor(morph_vocab)
names_extractor = NamesExtractor(morph_vocab)
embedding = NewsEmbedding()
ner_tagger = NewsNERTagger(embedding)
morph_tagger = NewsMorphTagger(embedding)
syntax_parser = NewsSyntaxParser(embedding)

doc = Doc(text)
doc.segment(segmenter)
doc.tag_ner(ner_tagger)
doc.tag_morph(morph_tagger)


# Бизнес логика
data = {}
for token in doc.tokens:
    word_class = token.pos
    if word_class not in data:
        data[word_class] = set()

    data[word_class].add(token.text)

pprint.pprint({TRANSLATE_DICT.get(w): len(s) for w, s in data.items()})
