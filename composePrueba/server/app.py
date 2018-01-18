import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Escribe /vias para ver las vías.\n'
@app.route('/vias')
def vias():
    return 'Caricias de coral\t6b\Alfacar\nFrío polar\t6a6\Alfacar\nArre con la chota\t6b\Alfacar\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
