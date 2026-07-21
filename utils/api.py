from utils.http_method import HttpMethods

base_url = "https://rahulshettyacademy.com" # Базовая URL
key = '?key=qaclick123'  # Ключ для авторизации

"""Методы для тестирования Google maps api"""
class Google_maps_api():

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():

        json_create_new_place = {

                "location": {

                    "lat": -38.383494,

                    "lng": 33.427362

                }, "accuracy": 50,

                "name": "Frontline house",

                "phone_number": "(+91) 983 893 3937",

                "address": "29, side layout, cohen 09",

                "types": [

                    "shoe park",

                    "shop"

                ],

                "website": "http://google.com",

                "language": "French-IN"

        }

        post_resource = "/maps/api/place/add/json" # Ресурс метода POST
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки существования локации"""
    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json" # Ресурс метода GET
        get_url = base_url + get_resource + key + "&place_id="+place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для изменения новой локации"""
    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json" # Ресурс метода PUT

        put_url = base_url + put_resource + key
        print(put_url)
        json_for_udpate_location = {
            "place_id": place_id,
            'address': "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_for_udpate_location)
        print(result_put.text)
        return result_put









