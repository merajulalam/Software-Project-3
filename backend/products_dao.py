from sql_connection import get_sql_connection


#  to get all products
def get_all_products(conncetion):
    cursor = conncetion.cursor()
    query = ("SELECT g_store.products.product_id, g_store.products.name, g_store.products.uom_id, g_store.products.price_per_unit, g_store.uom.uom_name  "
             "FROM g_store.products inner join g_store.uom on g_store.products.uom_id=uom.uom_id")
    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    return response


# to insert new product
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")

    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


# to delete product
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid



if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'mouse',
        'uom_id': '2',
        'price_per_unit': 200
    }))