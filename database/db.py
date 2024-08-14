import asyncio
import sqlite3


def create():
    product = [
        ('Product1', 522.89, 'This is an example product1.', 'database/images/product1.jpg'),
        ('Product2', 742.73, 'This is an example product2.', 'database/images/product2.jpg'),
        ('Product3', 437.51, 'This is an example product3.', 'database/images/product3.jpg'),
        ('Product4', 832.53, 'This is an example product4.', 'database/images/product4.jpg')
    ]

    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY,
                name_product TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT NOT NULL,
                image_path TEXT NOT NULL
            )
            ''')

        cursor.executemany('''
            INSERT INTO product (name_product, price, description, image_path)
            VALUES (?, ?, ?, ?)
            ''', product)


async def get_all():
    with sqlite3.connect("database/database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name_product, price, description, image_path FROM product")
        return cursor.fetchall()


if __name__ == '__main__':
    # create()
    result = asyncio.run(get_all())
    for i in result:
        print(i)
