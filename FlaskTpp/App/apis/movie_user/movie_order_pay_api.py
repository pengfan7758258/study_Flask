from alipay import AliPay
from flask_restful import Resource

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user.utils import login_required
from App.settings import app_private_key_string, alipay_public_key_string


class MovieOrderPayResource(Resource):
    @login_required
    def get(self, order_id):
        # 构建支付的客户端 AliPayClient
        alipay = AliPay(
            appid="",
            app_notify_url=None,  # 默认回调url
            app_private_key_string=app_private_key_string,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=alipay_public_key_string,
            sign_type="RSA",  # RSA 或者 RSA2
            debug=False  # 默认False
        )

        # 使用Alipayj进行支付请求的发起
        subject = "测试付款"

        # App支付，将order_string返回给app即可
        # 需要跳转到https://openapi.alipay.com/gateway.do? + order_string
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no="20161112",
            total_amount=10,
            subject=subject,
            notify_url="https://example.com/notify"  # 可选, 不填则使用默认notify url
        )

        pay_url = "https://openapi.alipay.com/gateway.do?" + order_string

        data = {
            'status': HTTP_OK,
            'msg': 'ok',
            'data': {
                'pay_url': pay_url,
                'order_id': order_id
            }
        }

        return data
