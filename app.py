from flask import Flask, render_template
import random

app = Flask(__name__)

image_texts = {
    'image1.jpg': 'アイスです',
    'image2.jpg': '果物です',
    'image3.jpg': 'デブ！',
    'image4.jpg': 'デブ！！'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def random_element():
    random_image = random.choice(list(image_texts.keys()))
    return {'image': random_image, 'text': image_texts[random_image]}

if __name__ == '__main__':
    app.run(debug=True)
