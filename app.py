from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>الوحدة الخامسة - الحياة الاقتصادية</h1>

    <h2>الزراعة</h2>
    <ul>
        <li>نشاط اقتصادي مهم</li>
        <li>تعتمد على الأمطار</li>
    </ul>

    <h2>الصناعة</h2>
    <ul>
        <li>استخراجية وتحويلية</li>
        <li>مثل الفوسفات</li>
    </ul>

    <h2>التجارة</h2>
    <ul>
        <li>داخلية وخارجية</li>
        <li>تبادل السلع</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)
