from .database import get_conn

def fetch_streamflow(bacia_id=None, start_date=None, end_date=None, limit=100):
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

    query += " ORDER BY data LIMIT %s"
    params.append(limit)

    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [
        {
            "bacia_id": r[0],
            "data": r[1],
            "vazao_m3s": float(r[2]),
            "rodada": r[3],
            "produto_id": r[4]
        } for r in rows
    ]

def fetch_climate(bacia_id=None, start_date=None, end_date=None, limit=100):
    conn = get_conn()
    cur = conn.cursor()

    query = """
        SELECT bacia_id, data, prec_mmdia, temp_c, rodada, produto_id
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

    query += " ORDER BY data LIMIT %s"
    params.append(limit)

    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [
        {
            "bacia_id": r[0],
            "data": r[1],
            "prec_mmdia": float(r[2]) if r[2] is not None else None,
            "temp_c": float(r[3]) if r[3] is not None else None,
            "rodada": r[4],
            "produto_id": r[5]
        } for r in rows
    ]
