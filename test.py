import requests

import config
import json
import data

#Мария Иванова, 1-я когорта — Финальный проект. Инженер по тестированию плюс
# Выполнить запрос на создание заказа.
# Сохранить номер трека заказа.
# Выполнить запрос на получения заказа по треку заказа.
# Проверить, что код ответа равен 200.

def createOrder ():
    response = requests.post(config.URL + config.CREATE_ORDERS,
                             json=data.order,
                             headers={
                                 "Content-Type": "application/json"
                             }
                             )
    return json.loads(response.text).get("track")

def checkOrder(order):
    response = requests.get(
        config.URL + config.GET_ORDER + str(order),
        headers={
            "Content-Type": "application/json"
        }
    )
    assert response.status_code == 200

def test():
    # authToken = get_new_user_token()
    track = createOrder()
    checkOrder(track)

test()


