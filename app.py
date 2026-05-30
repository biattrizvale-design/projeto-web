from flask import Flask, render_template, request

app = Flask(**name**)

@app.route('/', methods=['GET', 'POST'])
def home():
mensagem = ""

```
if request.method == 'POST':
    nome = request.form['nome']
    mensagem = f'Olá, {nome}! Seja bem-vindo ao meu projeto web.'

return render_template('index.html', mensagem=mensagem)
```

if **name** == '**main**':
app.run(debug=True)

