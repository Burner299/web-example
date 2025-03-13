from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 处理健康建议的 API
@app.route('/health_advice', methods=['POST'])
def health_advice():
    data = request.json  # 获取前端传来的 JSON 数据
    age = data.get('age')
    bmi = data.get('bmi')

    try:
        # 将 bmi 转换为浮动类型，以确保可以进行比较
        bmi = float(bmi)
    except ValueError:
        return jsonify({"error": "无效的 BMI 值"}), 400  # 如果 bmi 不是有效的数字，返回错误信息

    # 根据 bmi 给出健康建议
    if bmi > 25:
        advice = "您的 BMI 较高，建议增加运动，保持健康饮食！"
    else:
        advice = "您的 BMI 正常，继续保持良好的生活习惯！！！！"

    return jsonify({"advice": advice})  # 返回 JSON 格式的数据


# 渲染前端 HTML 页面
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

