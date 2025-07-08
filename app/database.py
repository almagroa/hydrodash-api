import psycopg2

def get_conn():
    return psycopg2.connect(
        host="yamanote.proxy.rlwy.net",
        database="railway",
        user="postgres",
        password="IEttkORGWOiHKfQrXdRSYqqkCUzxDFyn",
        port="47712"
    )
