from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_numbers():
    data = request.get_json()
    angka_pertama = data.get('angka_pertama')
    angka_kedua = data.get('angka_kedua')

    if angka_pertama is None or angka_kedua is None or angka_pertama > angka_kedua:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        angka_pertama = int(angka_pertama)
        angka_kedua = int(angka_kedua)
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

    hasil = []
    for angka in range(angka_pertama, angka_kedua + 1):
        if angka % 2 == 0:
            hasil.append(f'{angka} adalah bilangan genap')
        else:
            hasil.append(f'{angka} adalah bilangan ganjil')

    return jsonify({'hasil': hasil}), 200

if __name__ == '__main__':
    app.run(debug=True)
