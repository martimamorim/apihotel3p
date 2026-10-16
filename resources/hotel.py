from flask_restful import Resource, reqparse


lista_hoteis = [
    { "hotel_id": "sky", "nome": "Hotel Sky", "estrelas": 4.8, "diaria": 195.99 , "cidade": "Porto"},
    { "hotel_id": "sky1", "nome": "Hotel Sky", "estrelas": 4.8, "diaria": 195.99 , "cidade": "Braga"},
    { "hotel_id": "sky2", "nome": "Hotel Sky", "estrelas": 4.8, "diaria": 195.99 , "cidade": "Freamunde"}
]

class Hoteis(Resource) : 
    def get(self):
        return {"hoteis": lista_hoteis }
        

class Hotel(Resource) : 
    agrumentos = reqparse.RequestParser()
    agrumentos.add_argument("nome", type = str, required= True, help="Nome obrigatorio")
    agrumentos.add_argument("estrelas", type = float, required= True, help="Estrelas obrigatorio")
    agrumentos.add_argument("diaria", type = float, required= True, help="diaria obrigatorio")
    agrumentos.add_argument("cidade", type = str, required= True, help="cidade obrigatorio")
    def get(self, id_hotel):
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return hotel,200
            return {"message": "Hotel not found"} , 404


    def post(self, id_Hotel):
        dados = Hotel.argumentos.parse_args()
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return {"message": "Hotel with this id already exists"} 
        novo_hotel = {"hotel_id":id_hotel, **dados}
        listar_hoteis.append(novo_hotel)
        return hotel,200

    def put(self, id_Hotel):
            ...
    def delete(self, id_Hotel):
            ...