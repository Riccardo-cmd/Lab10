import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO

        input = self._view.guadagno_medio_minimo.value

        try:
            # Controllo se è vuoto
            if not input:
                raise ValueError

            soglia = float(input)
        except ValueError:
            self._view.show_alert("ERRORE! Inserire un valore numerico valido.")
            return

        self._model.costruisci_grafo(soglia)

        n_nodi = self._model.get_num_nodes()
        n_tratte = self._model.get_num_edges()
        tratte = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()

        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Grafo creato correttamente.\nNumero nodi: {n_nodi}\nNumero archi: {n_tratte}",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_200)
        )

        self._view.lista_visualizzazione.controls.append(ft.Divider())

        # Itero su tutti gli archi per mostrarli
        # u = nodo1, v = nodo2, data = dizionario attributi ({'weight': ..., 'count': ...})
        for u, v, data in tratte:
            peso = data.get('weight', 0)  # Guadagno medio
            num = data.get('count', 0)  # Numero spedizioni (nome che hai scelto nel model)

            # Creo la stringa formattata
            testo_tratta = f"{u} <-> {v} | Valore: {peso:.2f} € | Spedizioni: {num}"

            # Aggiungo alla lista
            self._view.lista_visualizzazione.controls.append(ft.Text(testo_tratta))

        # 5. Aggiorno la pagina per rendere visibili le modifiche
        self._view.update()