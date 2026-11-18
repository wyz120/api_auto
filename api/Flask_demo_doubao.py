from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# ========== 就加在这里！！ ==========
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "msg":"客达天下Mock服务已启动",
        "captcha":"/api/captchaImage",
        "login":"/api/login"
    })
# ==================================

# 内存存储验证码
captcha_store = {}

@app.route("/api/captchaImage", methods=["GET"])
def captcha_image():
    """获取验证码接口 GET"""
    captcha_uuid = str(uuid.uuid4())
    captcha_code = "2"
    captcha_store[captcha_uuid] = captcha_code
    resp_data = {
        "msg": "操作成功",
        "img": "base64编码的图片内容......",
        "code": 200,
        "uuid": captcha_uuid
    }
    return jsonify(resp_data)


@app.route("/api/login", methods=["POST"])
def login():
    """登录接口 POST /api/login"""
    req_json = request.get_json()
    if not req_json:
        return jsonify({"msg": "参数异常", "code": 500})

    username = req_json.get("username")
    password = req_json.get("password")
    code_input = req_json.get("code")
    req_uuid = req_json.get("uuid")

    real_captcha = captcha_store.get(req_uuid)
    if not real_captcha or real_captcha != code_input:
        return jsonify({
            "msg": "验证码已失效",
            "code": 500
        })

    if username == "manager" and password == "123456":
        mock_token = "Bearer_" + str(uuid.uuid4())
        return jsonify({
            "msg": "操作成功",
            "code": 200,
            "token": mock_token
        })
    else:
        return jsonify({
            "msg": "用户名或密码错误",
            "code": 500
        })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
