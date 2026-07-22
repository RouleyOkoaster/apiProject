import pytest
from utils.api import Google_maps_api

"""Создание, изменение и удаление новой локации"""
class TestCreatePlace():

    def test_create_new_place(self):
        print("Метод POST")
        result_post = Google_maps_api.create_new_place() # Вызов метода по созданию новой локации

        check_post = result_post.json()
        place_id = check_post.get('place_id')

        print("Method GET to check POST")
        result_get = Google_maps_api.get_new_place(place_id)

        print("Method PUT")
        result_put = Google_maps_api.put_new_place(place_id)

        print("Method GET to check PUT")
        result_get = Google_maps_api.get_new_place(place_id)

        print("Method DELETE")
        result_delete = Google_maps_api.delete_place(place_id)

        print("Method GET to check DELETE")
        result_get = Google_maps_api.get_new_place(place_id)

