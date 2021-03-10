from flask_restful import Resource


class UsersResource(Resource):
    def get(self):
        return {'msg': 'users get api'}

    def post(self):
        return {'msg': 'users post api'}


class UserResource(Resource):
    def get(self):
        return {'msg': 'user get api %d' % id}

    def post(self):
        return {'msg': 'user post api'}
