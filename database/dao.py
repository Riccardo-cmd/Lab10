from database.DB_connect import DBConnect

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    def readDisponibili(self,valore):
        conn = DBConnect.get_connection()
        query = """ SELECT LEAST(id_hub_origine, id_hub_destinazione) AS ID1,
                    GREATEST (id_hub_origine, id_hub_destinazione) AS ID2,
                    AVG(valore_merce) AS valore,
                    COUNT * AS numero_spedizioni,
                    FROM spedizione
                    GROUP BY LEAST(id_hub_origine, id_hub_destinazione),
                    GREATEST (id_hub_origine, id_hub_destinazione)
                    HAVING valore >= %s
                    """
        cursor = conn.cursor()
        cursor.execute(query, (valore,))

        result = []
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result