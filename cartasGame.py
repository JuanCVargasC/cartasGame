import tkinter as tk
from tkinter import messagebox
import random

# Valores de las cartas
card_values = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 11, 'K': 11
}

cards = ['A', 'K', '3', '6', '8', '2', '10', 'Q', '4', 'J']

# Función alfa-beta
def alphabeta(cards, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or not cards:
        return 0

    if maximizingPlayer:
        maxEval = float('-inf')
        for i in [0, -1]:  # Elegir desde los extremos
            card = cards[i]
            new_cards = cards[:i] if i == -1 else cards[1:]
            eval = card_values[card] + alphabeta(new_cards, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for i in [0, -1]:
            card = cards[i]
            new_cards = cards[:i] if i == -1 else cards[1:]
            eval = alphabeta(new_cards, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

# IU
class CardGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego de Cartas")
        self.geometry("600x400")
        self.cards = cards.copy()
        random.shuffle(self.cards)  # Barajar las cartas
        self.player_scores = [0, 0]  # Puntuación
        self.current_player = 0  # Jugador actual (0: Humano, 1: Máquina)
        self.create_widgets()

    def create_widgets(self):
        self.card_labels = [tk.Label(self, text=card, font=('Arial', 20)) for card in self.cards]
        for i, label in enumerate(self.card_labels):
            label.grid(row=0, column=i)

        self.score_labels = [
            tk.Label(self, text="Puntuación del Jugador: 0", font=('Arial', 16)),
            tk.Label(self, text="Puntuación de la Máquina: 0", font=('Arial', 16))
        ]
        self.score_labels[0].grid(row=1, columnspan=len(self.cards)//2)
        self.score_labels[1].grid(row=1, column=len(self.cards)//2, columnspan=len(self.cards)//2)

        self.button_left = tk.Button(self, text="Elegir Izquierda", command=lambda: self.choose_card(0))
        self.button_left.grid(row=2, column=0, columnspan=len(self.cards) // 2)

        self.button_right = tk.Button(self, text="Elegir Derecha", command=lambda: self.choose_card(-1))
        self.button_right.grid(row=2, column=len(self.cards) // 2, columnspan=len(self.cards) // 2)

        self.button_max_min = tk.Button(self, text="Mostrar Max/Min Puntaje", command=self.show_max_min_score)
        self.button_max_min.grid(row=3, column=0, columnspan=len(self.cards))

    def choose_card(self, index):
        if not self.cards:
            return

        card = self.cards.pop(index)
        self.player_scores[self.current_player] += card_values[card]

        for label in self.card_labels:
            label.grid_forget()
        self.card_labels = [tk.Label(self, text=card, font=('Arial', 20)) for card in self.cards]
        for i, label in enumerate(self.card_labels):
            label.grid(row=0, column=i)

        self.score_labels[self.current_player].config(
            text=f"Puntuación del {'Jugador' if self.current_player == 0 else 'Máquina'}: {self.player_scores[self.current_player]}"
        )

        if not self.cards:
            messagebox.showinfo("Juego Terminado", f"Puntuación final:\nJugador: {self.player_scores[0]}\nMáquina: {self.player_scores[1]}")
            self.quit()
        else:
            # Cambiar jugador
            self.current_player = 1 - self.current_player
            if self.current_player == 1:
                self.machine_move()

    def machine_move(self):
        if not self.cards:
            return

        # Simular la jugada de la la máquina con alfa-beta
        best_score = float('-inf')
        best_move = None

        for i in [0, -1]:  # Máquina elige
            card = self.cards[i]
            new_cards = self.cards[:i] if i == -1 else self.cards[1:]
            score = card_values[card] + alphabeta(new_cards, len(new_cards), float('-inf'), float('inf'), False)
            if score > best_score:
                best_score = score
                best_move = i

        # Realizar la mejor jugada encontrada
        self.choose_card(best_move)

    def show_max_min_score(self):
        max_score = alphabeta(self.cards, len(self.cards), float('-inf'), float('inf'), True)
        min_score = alphabeta(self.cards, len(self.cards), float('-inf'), float('inf'), False)
        messagebox.showinfo("Max/Min Puntaje", f"Puntaje Máximo Posible: {max_score}\nPuntaje Mínimo Posible: {min_score}")

# Ejecuta app
if __name__ == "__main__":
    app = CardGameApp()
    app.mainloop()
