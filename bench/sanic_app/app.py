from sanic import Sanic
from sanic.response import text, json

from record import get_record


app = Sanic(configure_logging=False)


@app.route("/record/read/<record_id>")
async def record_read(request, record_id):
    record = await get_record(record_id)
    return json(record)


@app.route("/version")
async def ping(request):
    return text('sanic_app')


@app.route("/")
async def ping(request):
    return text('Hello')


if __name__ == "__main__":
    app.run(port=80, debug=False, access_log=False, workers=4)
