from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource) : 
    def get(self):
        return {"hoteis": [hotel.json() for hotel in HotelModel.find_all()] }
        

class Hotel(Resource) : 
    agrumentos = reqparse.RequestParser()
    agrumentos.add_argument("nome", type = str, required= True, help="Nome obrigatorio")
    agrumentos.add_argument("estrelas", type = float, required= True, help="Estrelas obrigatorio")
    agrumentos.add_argument("diaria", type = float, required= True, help="diaria obrigatorio")
    agrumentos.add_argument("cidade", type = str, required= True, help="cidade obrigatorio")

    def get(self, id_hotel):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            return hotel.json(),200
        return {"message": "Hotel not found"} , 404

    def post(self, id_Hotel):
        dados = Hotel.argumentos.parse_args()
        hotel = Hotel.find_hotel(id_hotel)
        if hotel:
            return {"message": "Hotel with this id already exists"} 
        try:
            novo_hotel = HotelModel(hotel_id=id_Hotel, **dados)
            novo_hotel.save_hotel()
            return novo_hotel.json(),200
        except:
            return {"message": "interal error ...."}, 500

    def put(self, id_Hotel):
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel.find_hotel(id_Hotel)
        if hotel:
            try:
                hotel.update_hotel(dados["nome"], dados["estrelas"], dados["diaria"], dados["cidade"])
                hotel.save_hotel()
                return hotel.json(),200
            except:
                return {"message": "internal error ...."}, 500
        try:
            novo_hotel = HotelModel(hotel_id=id_Hotel, **dados)
            novo_hotel.save_hotel()
            return novo_hotel.json(),201
        except:
            return {"message": "interal error ...."}, 500

    def delete(self, id_Hotel):
        hotel = HotelModel.find_hotel(id_Hotel)
        if hotel:
            try:
                hotel.delete_hotel()
                return {"message": "Hotel deleted"}, 200
            except: 
                return {"message": "internal error ...."}, 500
        return {"message": "Hotel not found"}, 404
