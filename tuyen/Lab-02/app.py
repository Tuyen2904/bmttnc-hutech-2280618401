from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Route trang chủ
@app.route("/")
def home():
    return render_template("index.html")

# Route trang Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

# Xử lý mã hóa Caesar Cipher
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    Caesar = CaesarCipher()
    
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

# Xử lý giải mã Caesar Cipher
@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    Caesar = CaesarCipher()
    
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# Chạy ứng dụng Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)