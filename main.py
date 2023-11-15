from WordCounter import WordCounter
from TaxMan import TaxMan
from Calculator import Calculator
from CarCollector import CarCollector
from Character import Character
from pprint import pprint

#1
def sort_people(x, y, z):
   if z == 'desc':
    x.sort(key=lambda x: x[y], reverse = True)
   if z == 'asc':
    x.sort(key=lambda x: x[y], reverse = False)
def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)
#ex1()

#2
def filter_males(x):
    return list(filter(lambda a: a['sex'] == 'male', x))
def ex2():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_males(people_list)
    print(filtered_list)
#ex2()

#3
def calc_bmi(people_list):
    retval = {
        'id': people_list['id'],
        'name': people_list['name'],
        'weight_kg': people_list['weight_kg'],
        'height_meters': people_list['height_meters'],
        'bmi': round(people_list['weight_kg']/people_list['height_meters'] ** 2,1)
    }
    return retval
def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = list(map(calc_bmi, people_list))
    print(new_people_list)
#ex3()

#4
def get_people(x):
    return [p['name'] for p in x if p['age'] >= 15 ]
def ex4():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))
#ex4()

#5 refer to WordCounter.py file for WordCounter class
def ex5():
    sentence = "This is a test of the emergency broadcast system"
    myList = sentence.split(" ")
    word_counter = WordCounter(sentence, myList)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.
#ex5()

#6 refer to TaxMan.py for TaxMan class
def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())
#ex6()

#7 refer to Calculator.py for Calculator class
def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())
#ex7()

#8
def ex8():
    pprint(CarCollector.get_data())
#ex8()

#9
def ex9():
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)
#ex9()

#10
def ex10():
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]
    invoices = []
    for item in data:
        invoice_daat = item.split(', ')
        invoice = Invoice(*invoice_data)
        invoices.append(invoice)
    pprint(invoices)


