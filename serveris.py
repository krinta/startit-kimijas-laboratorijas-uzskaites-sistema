from flask import Flask, jsonify, render_template, json, request
import dati


app = Flask(__name__)

# nepieciešams garum- un mīkstinājumzīmēm json formātā
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/publiski')
def publiski():
    return render_template("pub_data.html")


@app.route('/pieslegties')
def pieslegties():
    return render_template("login.html")


@app.route('/uzskaite')
def uzskaite():
    return render_template("vielu_aprikojuma_uzskaite.html")


@app.route('/pievienot')
def pievienot():
    return render_template("pievienot_vielu_aprikojumu.html")


@app.route('/lietotajs')
def lietotajs():
    return render_template("user_menu.html")


@app.route('/api/v1/vielas')
def vielas():
  with open("dati/vielas.json","r",encoding="utf-8")as f:
    dati=json.loads(f.read())
    # pārveidojam par json pirms atgriežam
    return jsonify(dati)


@app.route('/api/v1/viela/<vielasID>')
def viela_id(vielasID):
    # Noklusēta vērtība, ja viela netiks atrasta
    viela = "Viela ar ID {} neeksistē".format(vielasID)
    # meklējam vielu sarakstā
    for v in dati.vielas:
        # vielas ID ir skaitlis, jāpārveido datu tips
        if v["id"] == int(vielasID):
            viela = v
    return jsonify(viela)

@app.route('/api/v1/viela', methods = ['POST'])
def pievienot_vielu():
  datne = "dati/vielas.json"

  with open(datne, "r", encoding = "utf-8") as f:
    vielas = json.loads(f.read())

  last_id = vielas[len(vielas) - 1]['id']
  
  jauna_viela = json.loads(request.data)
  jauna_viela['id'] = last_id + 1

  vielas.append(jauna_viela)

  with open(datne, "w", encoding = "utf-8") as f:
    f.write(json.dumps(vielas))
  
  return "1"


  #print("=======================")
  #print(len(vielas))
  #print(vielas[len(vielas)-1])
  #print("======================")
  

@app.route('/api/v1/<kategorija>/<id>/dzest', methods=['POST'])
def dzestVielu(kategorija,id):
  if kategorija=="viela":
    datne="dati/vielas.json"
  elif kategorija=="inventars":
    datne="dati/inventars.json"
  else:
    return "Datne nav atrasta!"
  with open(datne, "r",encoding="utf-8") as f:
    dati=json.loads(f.read())
  new_data=[]
  for v in dati:
    if str(v['id'])!=id:
      new_data.append(v)
  
  with open(datne,"w", encoding="utf-8") as f:
    f.write(json.dumps(new_data))


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
