from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
  return "Labrīt!"

@app.route('/Sveiki')
def Sveiki():
  return "Nav vairs nekāds rīts!"

@app.route('/Sveiki/<vards>')
def sveikiPersona(vards):
  return "Sveiki, {} !".format(vards) #f"Sveiki, {vards}"

@app.route('/cik/<sk1>/<sk2>')
def reizinajums(sk1,sk2):
  print(type(sk1))
  sk1=int(sk1)
  sk2=int(sk2)
  reiz=sk1*sk2
  return str(reiz)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
