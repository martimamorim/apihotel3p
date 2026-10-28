from flask_restful import Resource, reqparse
from models.user import userModel
from hmac import compare_digest
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

class User(Resource) : 
    def get(self, username):
        user = userModel.find_user(username)
        if user:
            return user.json(),200
        return {"message": "User not found"} , 404

    def delete(self, username):
        user = userModel.find_user(username)
        if user:
            try:
                user.delete_user()
                return {"message": "User deleted"}, 200
            except:
                return {"message": "internal error ...."}, 500
        return {"message": "User not found"}, 404


class UserRegister(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("username", type = str, required= True, help="Username obrigatorio")
    argumentos.add_argument("password", type = str, required= True, help="Password obrigatorio")

    def post(self):
        dados = UserRegister.argumentos.parse_args()
        if userModel.find_user(dados["username"]):
            return {"message": "User with this username already exists"} 
        try:
            novo_user = userModel(**dados)
            novo_user.save_user()
            return novo_user.json(),200
        except:
            return {"message": "interal error ...."}, 500

class UserLogin(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("username", type = str, required= True, help="Username obrigatorio")
    argumentos.add_argument("password", type = str, required= True, help="Password obrigatorio")

    def post(self):
        dados = UserLogin.argumentos.parse_args()
        user = userModel.find_user(dados["username"])
        if user and compare_digest(user.password, dados["password"]):
            access_token = create_access_token(identity=user.username)
            return {"access_token": access_token}, 200
        return {"message": "Invalid credentials"}, 401

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        # Implement logout logic here (e.g., token invalidation)
        return {"message": "Logged out successfully"}, 200
    