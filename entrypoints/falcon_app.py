import falcon
from service_layer.controlador_bot import ControladorBot
from bd import inicializar_bd


# falcon.API instances are callable WSGI apps
app = falcon.API()

sesion = inicializar_bd()
CONTROLADOR_BOT = ControladorBot(sesion)


class entradaController(object):
    # def on_get(self, req, resp):
    #     """Handles GET requests"""
    #     resp.status = falcon.HTTP_200  # This is the default status
    #     resp.body = ('\nTwo things awe me most, the starry sky '
    #                  'above me and the moral law within me.\n'
    #                  '\n'
    #                  '    ~ Immanuel Kant\n\n')
    #
    #

    def on_post(self, req, resp):
        try:
            rta = CONTROLADOR_BOT.nuevo_mensaje(req)
            resp.body(rta)
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.status = falcon.HTTP_400
            resp.body("falla:", e)


# Resources are represented by long-lived class instances
controllerBot = entradaController()

# things will handle all requests to the '/things' URL path
app.add_route('/nuevo_mensaje', controllerBot)
