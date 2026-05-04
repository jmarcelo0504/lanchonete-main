def test_deve_cancelar_pedido_com_sucesso(client):
    # TODO: criar cliente

    # TODO: criar produto

    # TODO: criar pedido

    response = client.post("/lanchonete/pedidos/1/cancelar")

    assert response.status_code == 200

    data = response.json()

    # TODO: validar se data["ok"] é True

    # TODO: validar mensagem de sucesso

def test_nao_deve_cancelar_pedido_inexistente(client):
    response = client.post("/lanchonete/pedidos/999/cancelar")

    # TODO: validar status_code

    data = response.json()

    # TODO: validar mensagem de erro

def test_nao_deve_cancelar_pedido_finalizado(client):
    # TODO: criar cliente

    # TODO: criar produto

    # TODO: criar pedido

    # TODO: finalizar pedido

    response = client.post("/lanchonete/pedidos/1/cancelar")

    # TODO: validar erro

def test_deve_listar_pedidos_cancelados(client):
    # TODO: criar cliente

    # TODO: criar produto

    # TODO: criar pedido

    # TODO: cancelar pedido

    response = client.get("/lanchonete/pedidos/cancelados")

    assert response.status_code == 200

    data = response.json()

    # TODO: validar se retornou uma lista

    # TODO: validar se existe pelo menos um pedido cancelado

    # TODO: validar se esta_cancelado é True