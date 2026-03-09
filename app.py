from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/oc_d6320885048ca26f33d2c51933257707"
QWEN_API_KEY = "sk-cab477a63e1045f2864dc1d2899f510d"

def get_qwen_response(prompt):
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {QWEN_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen-plus",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500
    }
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=30)
        result = resp.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI服务暂时不可用: {str(e)}"

def send_feishu_message(text):
    data = {"msg_type": "text", "content": {"text": text}}
    requests.post(WEBHOOK_URL, json=data, timeout=10)

@app.route("/")
def index():
    return "AI Bot Running!"

@app.route("/feishu/webhook", methods=["POST"])
def webhook():
    try:
        payload = request.get_json()
        if not payload or "msg_type" not in payload:
            return jsonify({"status": "ok"}), 200

        msg_type = payload.get("msg_type")
        
        if msg_type == "text":
            content = payload.get("content", {}).get("text", "")
            
            if "确认" in content or "开始" in content:
                reply = "好的，项目已确认！我会立即开始工作，完成后第一时间交付给您。如有需要修改的地方，请随时告诉我。"
            
            elif "写" in content or "文章" in content or "文案" in content:
                reply = "【写作服务报价】\n\n📝 文章/文案撰写：\n- 短文案（500字内）：50元\n- 中篇文章（1000字内）：100元\n- 长篇文章（2000字内）：200元\n- 商业文案/软文：300元起\n\n请告诉我您的具体需求，确认后即可开始工作。"
            
            elif "设计" in content or "图" in content or "海报" in content:
                reply = "【设计服务报价】\n\n🎨 平面设计：\n- 海报/DM单：80元起\n- logo设计：200元起\n- 包装设计：300元起\n- 店铺装修设计：500元起\n\n请告诉我具体设计需求，确认后即可开始工作。"
            
            elif "编程" in content or "代码" in content or "网站" in content or "小程序" in content:
                reply = "【编程服务报价】\n\n💻 开发服务：\n- 网页制作：300元起\n- 小程序开发：800元起\n- 简单工具开发：200元起\n- API接口开发：500元起\n\n请告诉我具体功能需求，确认后即可开始工作。"
            
            elif "接单" in content or "报价" in content or "价格" in content:
                reply = "【自由职业服务报价】\n\n📋 本人提供以下服务：\n\n📝 写作/文案：50元起\n🎨 设计/平面：80元起\n💻 编程/开发：300元起\n\n请告诉我您需要的具体服务类型，我会为您报价。"
            
            else:
                ai_reply = get_qwen_response(f"你是一个自由职业者助手，用户说：'{content}'。请用中文回复，简洁友好，询问用户具体需求并提供相应服务报价。")
                reply = ai_reply
            
            send_feishu_message(reply)
            
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
