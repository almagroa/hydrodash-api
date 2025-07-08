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