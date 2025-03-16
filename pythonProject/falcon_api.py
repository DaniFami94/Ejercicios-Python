import json,falcon

class ObjRequestClass:
    def on_get(self,req,resp):

        content= {
            'name':'Daniel',
            'age':'30',
            'country': 'Venezuela'
        }
        resp.text = json.dumps(content)
        resp.status = falcon.HTTP_200

api = falcon.App()
api.add_route('/test',ObjRequestClass())

# "waitress - serve - -port = 8000 falcon_api: api" , lanzamos el servidor con este comando


