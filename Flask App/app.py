from flask import Flask, render_template
from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
def generate():
        with open("Traffic analysis\Data\Cars.mp4", "rb") as f:
            data = f.read(1024)
            while data:
                yield data
                data = f.read(1024)
@app.route('/video_feed')
def video_feed():
    # code for streaming the video
    
      

    return Response(generate(),mimetype="video/mp4")

if __name__ == '__main__':
    app.run(debug=True)