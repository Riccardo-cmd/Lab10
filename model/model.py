from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._dao = DAO()
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self._idMap = {}
        self._load_hubs()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()
        tratte = self._dao.readDisponibili(threshold)

        for tratta in tratte:
            u = tratta["ID1"]
            v = tratta["ID2"]
            peso = tratta["valore"]
            n_sped = tratta["numero_spedizioni"]
            self.G.add_edge(u, v, weight=peso, count=n_sped)

    def _load_hubs(self):
        hubs = self._dao.get_all_hubs()
        for hub in hubs:
            self._idMap[hub["id_hub"]] = f"{hub['nome_hub']} ({hub['stato_hub']})"

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()
    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return self.G.edges(data=True)

    def get_nome_hub(self, id_hub):
        return self._idMap.get(id_hub, str(id_hub))



