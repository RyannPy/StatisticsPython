from flask import Flask, render_template, request
import statistics as st

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = []
    hasil = {'rata': None, 'median': None, 'modus': None, 'max': None, 'min': None, 'range': None, 'std': None}
    
    if request.method == "POST":
        data = list(map(int, request.form.get("angka").split()))
        
        hasil['rata'] = round(sum(data) / len(data), 2)
        hasil['median'] = st.median(data)
        hasil['modus'] = st.mode(data)
        hasil['max'] = max(data)
        hasil['min'] = min(data)
        hasil['range'] = max(data) - min(data)
        hasil['std'] = round(st.stdev(data), 2)
        
    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)