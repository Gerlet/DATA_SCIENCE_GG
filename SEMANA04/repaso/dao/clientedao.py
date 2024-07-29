from .dao import DAO

class ClienteDAO(DAO):

    def __init__(self):
        super().__init__()
        query_create = """
        CREATE TABLE IF NOT EXISTS tbl_cliente(
            id INT AUTO_INCREMENT PRIMARY KEY,
            razon_social VARCHAR(255) NOT NULL,
            ruc VARCHAR(20) NOT NULL,
            direccion TEXT,
            linea_credito INT default 0
        );
        """
        self.cursor.execute(query_create)
        self.db.commit()

    def insertar(self,cliente):
        nuevo_cliente = (
            cliente.ruc,
            cliente.razon_social,
            cliente.direccion,
        )
        query = "insert into tbl_cliente(ruc,razon_social,direccion) values(%s,%s,%s)"
        self.cursor.execute(query,nuevo_cliente)
        self.db.commit()

    def consultar(self):
        self.cursor.execute("select id,razon_social,ruc,direccion from tbl_cliente")
        return self.cursor.fetchall()