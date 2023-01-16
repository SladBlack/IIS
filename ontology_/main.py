# импорт библиотеки
import pathlib

from owlready2 import *

root_path = pathlib.Path(__file__).parent.resolve()
# указываем локольный репозитарий хранения онтологии (путь к файлу) изагружаем ее
onto = get_ontology(f'{root_path}/ont.owl').load()
# получаем список классов онтологии
print(list(onto.classes()))
# получаем список индивидов онтологии
print(list(onto.individuals()))
# получаем список объектных свойств онтологии
print(list(onto.object_properties()))
# получаем список объектных свойств онтологии
print(list(onto.object_properties()))
# получаем список дата-свойств онтологии
print(list(onto.data_properties()))

with onto:
    class Compilator(Thing):
        pass

# создаем новый класс и выводим сообщение
with onto:
    class VSCode(onto.Compilator):
        print("Класс VSCode наследник Компилятора")

print('Classes: ', list(onto.classes()))


# создаем новый класс и указываем пространство имен
class Developer(Thing):
    namespace = onto


# создание дата-свойства с указанием типа значений
with onto:
    class LevelOfUnderstanding(DataProperty):
        range = [str]

print(list(onto.data_properties()))

with onto:
    class Libraries(DataProperty):
        domain = [VSCode]
        range = [int]

print(list(onto.data_properties()))

# создаем индивид
ind3 = onto.VSCode("Java")
print('Individuals:', list(onto.individuals()))


with onto:
    class OOP(Thing):
        pass
    class HaveDebug(ObjectProperty):
        domain = [VSCode]
        range = [onto.OOP]


ind3.HaveDebug = [onto.Java]
ind3.LevelOfUnderstanding = ['3']

iri = IRIS["http://www.semanticweb.org/alex/ontologies/2022/8/inf-ontology"]

# # ищем объекты онтологии по шаблону его идентификатора
print('Search (по шаблону его идентификатора)', onto.search(iri="*V*"))
# # ищем объекты онтологии по шаблону для значения свойства объекта
print('Search (по шаблону для значения свойства объекта)', onto.search(LevelOfUnderstanding="*"))
# # ищем объекты онтологии по конкретному значению дата-свойства объекта
print('Search (по конкретному значению дата-свойства объект)', onto.search(LevelOfUnderstanding=3))


# # строим запрос к онтологии на SPARQL
print(list(default_world.sparql(
    """
        SELECT ?subject ?object
    WHERE { ?subject rdfs:subClassOf ?object } limit 1
    """
)))

onto.save(file=f'{root_path}/ont.owl', format='rdfxml')