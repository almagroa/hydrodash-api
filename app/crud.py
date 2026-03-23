import math
from .database import get_conn

def fetch_streamflow(bacia_id=None, start_date=None, end_date=None, rodada=None, produto_id=None, limit=100):
    conn = get_conn()
    cur = conn.cursor()

    query = """
        SELECT bacia_id, data, vazao_m3s, rodada, produto_id
        FROM streamflow
        WHERE 1=1
    """
    params = []

    if bacia_id:
        query += " AND bacia_id = %s"
        params.append(bacia_id)
    if start_date:
        query += " AND data >= %s"
        params.append(start_date)
    if end_date:
        query += " AND data <= %s"
        params.append(end_date)
    if rodada:
        query += " AND rodada = %s"
        params.append(rodada)
    if produto_id:
        query += " AND produto_id = %s"
        params.append(produto_id)

    query += " ORDER BY data LIMIT %s"
    params.append(limit)

    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for r in rows:
        valor = r[2]
        if valor is not None and isinstance(valor, float) and math.isnan(valor):
            valor = None

        result.append({
            "bacia_id": r[0],
            "data": r[1],
            "vazao_m3s": valor,
            "rodada": r[3],
            "produto_id": r[4]
        })
    return result


def fetch_climate(bacia_id=None, start_date=None, end_date=None, rodada=None, produto_id=None, limit=100):
    conn = get_conn()
    cur = conn.cursor()

    query = """
        SELECT bacia_id, data, precipitacao_mm, rodada, produto_id
        FROM clima
        WHERE 1=1
    """
    params = []

    if bacia_id:
        query += " AND bacia_id = %s"
        params.append(bacia_id)
    if start_date:
        query += " AND data >= %s"
        params.append(start_date)
    if end_date:
        query += " AND data <= %s"
        params.append(end_date)
    if rodada:
        query += " AND rodada = %s"
        params.append(rodada)
    if produto_id:
        query += " AND produto_id = %s"
        params.append(produto_id)

    query += " ORDER BY data LIMIT %s"
    params.append(limit)

    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for r in rows:
        prec = r[2]
        if prec is not None and isinstance(prec, float) and math.isnan(prec):
            prec = None

        result.append({
            "bacia_id": r[0],
            "data": r[1],
            "precipitacao_mm": prec,
            "rodada": r[3],
            "produto_id": r[4]
        })
    return result

def fetch_bacias(bacia_id=None):
    conn = get_conn()
    cur = conn.cursor()

    query = "SELECT id, cidade, estado, nome, area_km2 FROM bacias WHERE 1=1"
    params = []

    if bacia_id:
        query += " AND id = %s"
        params.append(bacia_id)

    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "cidade": r[1],
            "estado": r[2],
            "nome": r[3],
            "area_km2": float(r[4]) if r[4] is not None else None
        })
    return result

def fetch_produtos(produto_id=None):
    conn = get_conn()
    cur = conn.cursor()

    query = "SELECT id, nome, descricao FROM produtos WHERE 1=1"
    params = []

    if produto_id:
        query += " AND id = %s"
        params.append(produto_id)

    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "nome": r[1],
            "descricao": r[2]
        })
    return result


def fetch_bacias_cotas(bacia_id=None):
    conn = get_conn()
    cur = conn.cursor()

    query = "SELECT id, cidade, estado, nome FROM bacias_cotas WHERE 1=1"
    params = []

    if bacia_id:
        query += " AND id = %s"
        params.append(bacia_id)

    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "cidade": r[1],
            "estado": r[2],
            "nome": r[3]
        })
    return result


def fetch_cotas(bacia_id=None, start_date=None, end_date=None, rodada=None, produto_id=None, limit=100):
    conn = get_conn()
    cur = conn.cursor()

    query = """
        SELECT c.bacia_id, bc.cidade, bc.estado, bc.nome, c.data, c.cota, c.rodada, c.produto_id, c.ci
        FROM cotas c
        JOIN bacias_cotas bc ON c.bacia_id = bc.id
        WHERE 1=1
    """
    params = []

    if bacia_id:
        query += " AND c.bacia_id = %s"
        params.append(bacia_id)
    if start_date:
        query += " AND c.data >= %s"
        params.append(start_date)
    if end_date:
        query += " AND c.data <= %s"
        params.append(end_date)
    if rodada:
        query += " AND c.rodada = %s"
        params.append(rodada)
    if produto_id:
        query += " AND c.produto_id = %s"
        params.append(produto_id)

    query += " ORDER BY c.data LIMIT %s"
    params.append(limit)

    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for r in rows:
        cota = r[5]
        if cota is not None and isinstance(cota, float) and math.isnan(cota):
            cota = None
        
        ci = r[8]
        if ci is not None and isinstance(ci, float) and math.isnan(ci):
            ci = None

        result.append({
            "bacia_id": r[0],
            "cidade": r[1],
            "estado": r[2],
            "nome": r[3],
            "data": r[4],
            "cota": cota,
            "rodada": r[6],
            "produto_id": r[7],
            "ci": ci
        })
    return result

def fetch_cotas_obs(bacia_id=None, start_date=None, end_date=None, limit=100):
    conn = get_conn()
    cur = conn.cursor()

    query = """
        SELECT c.bacia_id, bc.cidade, bc.estado, bc.nome, c.data, c.cota
        FROM cotas_obs c
        JOIN bacias_cotas bc ON c.bacia_id = bc.id
        WHERE 1=1
    """
    params = []

    if bacia_id:
        query += " AND c.bacia_id = %s"
        params.append(bacia_id)
    if start_date:
        query += " AND c.data >= %s"
        params.append(start_date)
    if end_date:
        query += " AND c.data <= %s"
        params.append(end_date)

    query += " ORDER BY c.data LIMIT %s"
    params.append(limit)

    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for r in rows:
        cota_observada = r[5]
        if cota_observada is not None and isinstance(cota_observada, float) and math.isnan(cota_observada):
            cota_observada = None

        result.append({
            "bacia_id": r[0],
            "cidade": r[1],
            "estado": r[2],
            "nome": r[3],
            "data": r[4],
            "cota_observada": cota_observada
        })
    return result