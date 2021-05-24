from flask import Blueprint

from .views.cliente import cliente, cliente_new

bp_cliente = Blueprint('clientes', __name__)
bp_cliente.add_url_rule('/clientes', view_func=cliente, methods=['GET'])
bp_cliente.add_url_rule('/clientes/new/', view_func=cliente_new, methods=['GET', 'POST'])
bp_cliente.add_url_rule('/clientes/<int:id/', view_func=cliente, methods=['GET', 'POST'])