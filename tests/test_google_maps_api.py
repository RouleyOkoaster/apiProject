import json
import allure
import pytest
from utils.api import Google_maps_api
from utils.checking import Checking

"""Создание, изменение и удаление новой локации"""
@allure.epic("Test create place")
class TestCreatePlace():

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("Метод POST")
        result_post = Google_maps_api.create_new_place() # Вызов метода по созданию новой локации

        check_post = result_post.json()
        place_id = check_post.get('place_id')

        token = {

            "status": "OK",

            "place_id": "dea036e58d6773b3f8bfb256249a1593",

            "scope": "APP",

            "reference": "1f71a23b1374071eecbb70eed1054cf91f71a23b1374071eecbb70eed1054cf9",

            "id": "1f71a23b1374071eecbb70eed1054cf9"
        }

        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, list(token))
        Checking.check_json_value(result_post, "status", "OK")


        print("Method GET to check POST")
        result_get = Google_maps_api.get_new_place(place_id)

        token = {

                "location": {
            
                    "latitude": "-38.383494",
            
                    "longitude": "33.427362"
            
                },
            
                "accuracy": "50",
            
                "name": "Frontline house",
            
                "phone_number": "(+91) 983 893 3937",
            
                "address": "29, side layout, cohen 09",
            
                "types": "shoe park,shop",
            
                "website": "http://google.com",

                "language": "French-IN"

        }

        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, list(token))
        Checking.check_json_value(result_get, "address", token["address"])

        print("Method PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ["msg"])
        Checking.check_json_value(result_put, "msg", "Address successfully updated")

        print("Method GET to check PUT")
        result_get = Google_maps_api.get_new_place(place_id)

        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, list(token))
        Checking.check_json_value(result_get, "address", "100 Lenina street, RU")

        print("Method DELETE")
        result_delete = Google_maps_api.delete_place(place_id)

        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ["status"])
        Checking.check_json_value(result_delete, "status", "OK")

        print("Method GET to check DELETE")
        result_get = Google_maps_api.get_new_place(place_id)

        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ["msg"])
        Checking.check_json_value(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")


