from database.DB_connect import DBConnect

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    def readDisponibili(self,valore):
        conn = DBConnect.get_connection()
        query = """
                SELECT 
                    LEAST(id_hub_origine, id_hub_destinazione) as ID1, 
                    GREATEST(id_hub_origine, id_hub_destinazione) as ID2, 
                    AVG(valore_merce) as valore,
                    COUNT(*) as numero_spedizioni
                FROM spedizione
                GROUP BY 
                    LEAST(id_hub_origine, id_hub_destinazione), 
                    GREATEST(id_hub_origine, id_hub_destinazione)
                HAVING valore >= %s
                """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (valore,))

        result = []
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    def get_all_hubs(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("""SELECT id AS id_hub, nome AS nome_hub, stato AS stato_hub
                    FROM hub""")

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        cursor.close()
        cnx.close()
        return result