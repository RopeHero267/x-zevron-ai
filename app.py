from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# =========================
# AI BRAIN
# =========================

def ai(msg):

    msg = msg.lower().strip()

    # GREETINGS
    greetings = [
        "hi",
        "hello",
        "hey",
        "hey there",
        "good morning",
        "good evening"
    ]

    if any(g in msg for g in greetings):
        return "👋 Hello! আমি X-Zevron AI। আমি তোমাকে help করতে প্রস্তুত আছি."

    # INTRO
    if "your name" in msg or "who are you" in msg:
        return "🤖 আমার নাম X-Zevron AI। আমি একটি smart assistant chatbot।"

    if "what can you do" in msg:
        return "আমি প্রশ্নের উত্তর দিতে পারি, information explain করতে পারি, ideas দিতে পারি এবং coding help করতে পারি।"

    # AI KNOWLEDGE
    if "what is ai" in msg or ("ai" in msg and "what" in msg):
        return "🧠 AI মানে Artificial Intelligence — যা machine কে মানুষের মতো চিন্তা করতে সাহায্য করে।"

    # EDUCATION
    if "python" in msg:
        return "🐍 Python হলো একটি popular programming language যা AI, web development ও automation এ ব্যবহার হয়।"

    if "html" in msg:
        return "🌐 HTML হলো web page structure তৈরি করার language।"

    if "javascript" in msg:
        return "⚡ JavaScript web কে interactive করার programming language।"

    if "flutter" in msg:
        return "📱 Flutter হলো Google এর framework যা দিয়ে Android ও iOS app তৈরি করা যায়।"

    # MOTIVATION
    if "motivate" in msg or "motivation" in msg:
        return "🔥 তুমি যদি consistent থাকো, তাহলে impossible কিছু নাই। Start small, grow big!"

    if "sad" in msg:
        return "💙 দুঃখ temporary। তুমি strong 💪"

    # GENERAL KNOWLEDGE
    if "capital of bangladesh" in msg:
        return "🇧🇩 Bangladesh এর capital হলো Dhaka।"

    if "capital of india" in msg:
        return "🇮🇳 India এর capital হলো New Delhi।"

    if "earth" in msg:
        return "🌍 Earth হলো আমাদের planet যেখানে আমরা বাস করি।"

    # TECH HELP
    if "code" in msg:
        return "💻 আমি coding help করতে পারি। তুমি specific problem বলো।"

    if "error" in msg:
        return "⚠️ তুমি exact error message পাঠাও, আমি help করার চেষ্টা করবো।"

    # RELATION STYLE
    if "love" in msg:
        return "❤️ আমি AI, কিন্তু friendly ভাবে কথা বলতে পারি।"

    if "friend" in msg:
        return "🤝 আমি তোমার virtual AI friend।"

    # BUSINESS
    if "business idea" in msg:
        return "💡 Online business, content creation, freelancing ভালো option হতে পারে।"

    if "earn money" in msg:
        return "💰 Skill develop করে freelancing, YouTube বা AI tools use করে earning করা যায়।"

    # DEFAULT RESPONSE
    return (
        "🤖 আমি তোমার প্রশ্ন বুঝেছি: '" + msg + "'.\n\n"
        "আমি এখনো learning phase এ আছি, কিন্তু আমি সবচেয়ে ভালো উত্তর দেওয়ার চেষ্টা করছি.\n"
        "👉 তুমি চাইলে আরও specific question করতে পারো."
    )

# =========================
# API ROUTE
# =========================

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    msg = data.get("message", "")

    reply = ai(msg)

    return jsonify({
        "reply": reply
    })

# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
