import sqlite3
import random

db = sqlite3.connect('books_sales.db')
c = db.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS author (
    author_id INTEGER PRIMARY KEY,
    name_author TEXT,
    surname_author TEXT,
    birthday DATE,
    book_count INTEGER
)""")


c.execute("""CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    author_id INTEGER, 
    title TEXT,
    price FLOAT
)""")

c.execute("""CREATE TABLE IF NOT EXISTS buy (
    buy_id INTEGER PRIMARY KEY,
    book_id INTEGER, 
    amount INTEGER, 
    buy_description TEXT,
    buy_date DATE
)""")

name_author = {'Николай', 'Руслан', 'Алексей', 'Юрий', 'Ярослав', 'Семен', 'Евгений', 'Олег', 'Артур', 'Петр', 'Степан', 'Илья', 'Вячеслав', 'Сергей', 'Василий'}
surname_author = {'Смирнов', 'Сидоров', 'Кузнецов', 'Петров', 'Козлов', 'Цой', 'Котов', 'Соловьев', 'Уткин', 'Тихонов'}
birthday = {'1960-10-02', '1960-12-02', '1960-10-21', '1960-08-05', '1960-11-14', '1960-07-08', '1960-01-02', '1960-04-05', '1960-06-11', '1960-12-15', '1960-11-11'}
date_buy = {'2020-10-02', '2020-12-02', '2020-10-21', '2020-08-05', '2020-11-14', '2020-07-08', '2020-01-02', '2020-04-05', '2020-06-11', '2020-12-15', '2020-11-11'}
title = {'Кошка и собака', 'Как стать футболистом?', 'Джек победитель', 'Таблетки от болезней', 'Программист - это чудо', 'Рандомное название', 'Фантазия не работает', 'Но нужно еще зарандомить', 'Ночь - не время для сна', 'Девочка без персиков'}
buy_description = {'Никто не покупает', 'Очень высокая оценка', 'Только для мужчин', 'Детям очень нравится', 'Годнота', 'СПБГУ оценили', 'Про коней', 'Ужастик', 'Программистам заходит', 'Очень популярна в Германии', 'Есть электронная версия', 'Говорят, не очень'}


for i in range(10):
    c.execute("""INSERT INTO author VALUES(?,?,?,?,?)""",
              (i,
               name_author.pop(),
               surname_author.pop(),
               birthday.pop(),
               random.randint(50, 125)
              ))

for i in range(10):
    c.execute("""INSERT INTO books VALUES(?,?,?,?)""",
              (i,
               random.randint(0,10),
               title.pop(),
               random.uniform(150.5, 800.5)
              ))

for i in range(10):
    c.execute("""INSERT INTO buy VALUES(?,?,?,?,?)""",
              (i,
               random.randint(0,10),
               random.randint(1,5),
               buy_description.pop(),
               date_buy.pop()
              ))

query = '''SELECT title, price*amount AS cost
    FROM buy JOIN books USING(book_id)
    WHERE buy_date > '2020-06-01';

'''

c.execute(query)
print(c.fetchall())

db.commit()
db.close()