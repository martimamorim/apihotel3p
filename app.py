from flask import Flask
from flask_restful import Resource, Api
from resources.hotel import Hoteis, Hotel
app = Flask(__name__)
api = Api(app)

#configuraçoes

#rotas
api.add_resource(Hoteis,"/hoteis")
api.add_resource(Hotel,"/hoteis/<string:id_hotel>")

#iniciar a aplicaçao

if __name__ == "__main__":
    app.run(debug=True)