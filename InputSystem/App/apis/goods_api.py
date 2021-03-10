from flask import request
from flask_restful import Resource, abort, fields, marshal, marshal_with

from App.models import Goods

goods_fields = {
    'id': fields.Integer,
    'g_name': fields.String,
    'g_price': fields.Float,
    'url': fields.Url("single_goods", absolute=True)
}

single_goods_fields = {
    'data': fields.Nested(goods_fields),
    'status': fields.Integer,
    'msg': fields.String
}

multi_goods_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(goods_fields))
}


class GoodsListResource(Resource):
    @marshal_with(multi_goods_fields)
    def get(self):
        goods_list = Goods.query.all()

        data = {
            "status": 200,
            "msg": "ok",
            "data": goods_list
        }

        return data

    @marshal_with(single_goods_fields)
    def post(self):
        g_name = request.form.get('g_name')
        g_price = request.form.get('g_price')

        goods = Goods()
        goods.g_name = g_name
        goods.g_price = g_price

        if not goods.save():
            abort(400)

        """
            JOSN
                Response
            格式:
                单个对象
                {
                    "status":200,
                    "msg":"ok",
                    "data":{
                        "property":"value",
                        "property":"value",
                        "property":"value"
                    }
                }    
                
                多个对象
                {
                    "status":200,
                    "msg":"ok",
                    "data":[
                        {
                            "property":"value",
                            "property":"value",
                            "property":"value"                         
                        },
                        {
                            "property":"value",
                            "property":"value",
                            "property":"value"                         
                        },
                        {
                            "property":"value",
                            "property":"value",
                            "property":"value"                         
                        },
                        {
                            "property":"value",
                            "property":"value",
                            "property":"value"                         
                        }
                    ]
                }
        """

        data = {
            'msg': "create success",
            "status": 201,
            "data": goods
        }

        return data


class GoodsResource(Resource):
    @marshal_with(single_goods_fields)
    def get(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(400,**{'msg':'Do not understand!'})

        data = {
            'msg': "ok",
            "status": 200,
            "data": goods
        }
        return data

    def delete(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(404)

        if not goods.delete():
            abort(400)

        data = {
            'msg': 'delete success',
            'status': 204
        }
        return data

    def put(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(404)

        goods.g_name = request.form.get('g_name')
        goods.g_price = request.form.get('g_price')

        if not goods.save():
            abort(400)

        data = {
            'msg': 'put success',
            'status': 204,
            'data': goods
        }
        return marshal(data, single_goods_fields)

    @marshal_with(single_goods_fields)
    def patch(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(404)

        goods.g_name = request.form.get('g_name') or goods.g_name
        goods.g_price = request.form.get('g_price') or goods.g_price

        if not goods.save():
            abort(400)

        data = {
            'msg': 'put success',
            'status': 204,
            'data': goods
        }
        return data
