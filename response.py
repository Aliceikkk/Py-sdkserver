from __main__ import app

from flask import Response, render_template
import json

import define

# error handlers
@app.errorhandler(404)
def page_not_found(e):
   print(f"ErrorHandler: {e=}, {e.description}")
   return render_template('404.tmpl'), 404


# custom json response
def json_rsp(code, data):
   response_data = {"retcode": code}
   response_data.update(data)
   return Response(json.dumps(response_data, separators=(',', ':')), mimetype='application/json')

def json_rsp_with_msg(code, msg, data):
   response_data = {"retcode": code, "message": msg}
   response_data.update(data)
   return Response(json.dumps(response_data, separators=(',', ':')), mimetype='application/json')
