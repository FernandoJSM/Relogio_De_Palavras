import time
import tkinter as tk

BACKGROUND = "#252525"
COLOR_OFF = "#505050"
COLOR_ON = "#FF9700"


class Clock(tk.Tk):

    def __init__(self):
        """
            Inicializa e executa o relógio
        """
        super().__init__()

        self.title("Que horas são?")
        self.config(background=BACKGROUND)

        self.letters = [
            ['S', 'Ã', 'O', 'É', 'V', 'I', 'N', 'T', 'E', 'M', 'E', 'I', 'O', '-', 'D', 'I', 'A', 'M', 'E'],
            ['I', 'A', '-', 'N', 'O', 'I', 'T', 'E', 'U', 'M', 'A', 'D', 'U', 'A', 'S', 'T', 'R', 'Ê', 'S'],
            ['Q', 'U', 'A', 'T', 'R', 'O', 'C', 'I', 'N', 'C', 'O', 'N', 'Z', 'E', 'T', 'R', 'E', 'Z', 'E'],
            ['C', 'A', 'T', 'O', 'R', 'Z', 'E', 'Q', 'U', 'I', 'N', 'Z', 'E', 'D', 'E', 'Z', 'E', 'S', 'S'],
            ['E', 'I', 'S', 'D', 'E', 'Z', 'E', 'S', 'S', 'E', 'T', 'E', 'D', 'E', 'Z', 'O', 'I', 'T', 'O'],
            ['D', 'E', 'Z', 'E', 'N', 'O', 'V', 'E', 'H', 'O', 'R', 'A', 'S', 'E', 'V', 'I', 'N', 'T', 'E'],
            ['T', 'R', 'I', 'N', 'T', 'A', 'Q', 'U', 'A', 'R', 'E', 'N', 'T', 'A', 'C', 'I', 'N', 'Q', 'U'],
            ['E', 'N', 'T', 'A', 'Z', 'E', 'R', 'O', 'U', 'M', 'D', 'O', 'I', 'S', 'T', 'R', 'Ê', 'S', 'Q'],
            ['U', 'A', 'T', 'R', 'O', 'C', 'I', 'N', 'C', 'O', 'N', 'Z', 'E', 'D', 'O', 'Z', 'E', 'T', 'R'],
            ['E', 'Z', 'E', 'C', 'A', 'T', 'O', 'R', 'Z', 'E', 'Q', 'U', 'I', 'N', 'Z', 'E', 'D', 'E', 'Z'],
            ['E', 'S', 'S', 'E', 'I', 'S', 'D', 'E', 'Z', 'E', 'S', 'S', 'E', 'T', 'E', 'D', 'E', 'Z', 'O'],
            ['I', 'T', 'O', 'D', 'E', 'Z', 'E', 'N', 'O', 'V', 'E', 'M', 'I', 'N', 'U', 'T', 'O', 'S', '.']
        ]

        self.labels = {}

        for i in range(0, len(self.letters)):
            for j in range(0, len(self.letters[i])):
                self.labels["label_" + str(i) + "_" + str(j)] = tk.Label(
                    self,
                    fg=COLOR_OFF,
                    bg=BACKGROUND,
                    text=self.letters[i][j],
                    font="Helvetica 16",
                )
                self.labels["label_" + str(i) + "_" + str(j)].grid(column=j, row=i)

        self.update_time()

    @staticmethod
    def translate_hours(hours):
        """
            Define quais letras das horas serão iluminadas
        """
        if hours in [0, 12]:
            hours_text = [[0, 3]]  # É
        elif hours == 1:
            hours_text = [
                [0, 3], [5, 8], [5, 9], [5, 10], [5, 11]
            ]  # É ... HORA
        else:
            hours_text = [
                [0, 0], [0, 1], [0, 2], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12]
            ]  # SÃO ... HORAS

        hours_number = [
            [[0, 17], [0, 18], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]],  # MEIA-NOITE
            [[1, 8], [1, 9], [1, 10]],                          # UMA
            [[1, 11], [1, 12], [1, 13], [1, 14]],               # DUAS
            [[1, 15], [1, 16], [1, 17], [1, 18]],               # TRÊS
            [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5]],   # QUATRO
            [[2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],          # CINCO
            [[3, 18], [4, 0], [4, 1], [4, 2]],                  # SEIS
            [[4, 8], [4, 9], [4, 10], [4, 11]],                 # SETE
            [[4, 15], [4, 16], [4, 17], [4, 18]],               # OITO
            [[5, 4], [5, 5], [5, 6], [5, 7]],                   # NOVE
            [[4, 12], [4, 13], [4, 14]],                        # DEZ
            [[2, 10], [2, 11], [2, 12], [2, 13]],               # ONZE
            [[0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [0, 15], [0, 16]],        # MEIO-DIA
            [[2, 14], [2, 15], [2, 14], [2, 16], [2, 17], [2, 18]],                         # TREZE
            [[3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6]],                       # CATORZE
            [[3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12]],                            # QUINZE
            [[3, 13], [3, 14], [3, 15], [3, 16], [3, 17], [3, 18], [4, 0], [4, 1], [4, 2]], # DEZESSEIS
            [[4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11]],     # DEZESSETE
            [[4, 12], [4, 13], [4, 14], [4, 15], [4, 16], [4, 17], [4, 18]],                # DEZOITO
            [[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7]],               # DEZENOVE
            [[0, 4], [0, 5], [0, 6], [0, 7], [0, 8]],                                       # VINTE
            [[0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 7], [1, 8], [1, 9], [1, 10]],      # VINTE E UMA
            [[0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 7], [1, 11], [1, 12], [1, 13], [1, 14]],  # VINTE E DUAS
            [[0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 7], [1, 15], [1, 16], [1, 17], [1, 18]],  # VINTE E TRÊS
        ]

        # Meio dia, meia noite!
        output = hours_text
        output.extend(hours_number[hours])
        
        return output

    @staticmethod
    def translate_minutes(minutes):
        """
            Define quais serão os minutos iluminados
        """
        if minutes == 1:
            minutes_text = [
                [5, 13], [11, 11], [11, 12], [11, 13], [11, 14], [11, 15], [11, 16]
            ]   # E ... MINUTO
        else:
            minutes_text = [
                [5, 13], [11, 11], [11, 12], [11, 13], [11, 14], [11, 15], [11, 16], [11, 17]
            ]   # E ... MINUTOS

        minutes_units = [
            [[7, 8], [7, 9]],                                   # UM
            [[7, 10], [7, 11], [7, 12], [7, 13]],               # DOIS
            [[7, 14], [7, 15], [7, 16], [7, 17]],               # TRÊS
            [[7, 18], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4]],  # QUATRO
            [[8, 5], [8, 6], [8, 7], [8, 8], [8, 9]],           # CINCO
            [[10, 2], [10, 3], [10, 4], [10, 5]],               # SEIS
            [[10, 11], [10, 12], [10, 13], [10, 14]],           # SETE
            [[10, 18], [11, 0], [11, 1], [11, 2]],              # OITO
            [[11, 7], [11, 8], [11, 9], [11, 10]]               # NOVE
        ]

        minutes_tenths = [
            [[5, 14], [5, 15], [5, 16], [5, 17], [5, 18]],                                  # VINTE
            [[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5]],                               # TRINTA
            [[6, 6], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13]],           # QUARENTA
            [[6, 14], [6, 15], [6, 16], [6, 17], [6, 18], [7, 0], [7, 1], [7, 2], [7, 3]]   # CINQUENTA
        ]

        minutes_teens = [
            [[9, 16], [9, 17], [9, 18]],                    # DEZ
            [[8, 9], [8, 10], [8, 11], [8, 12]],            # ONZE
            [[8, 13], [8, 14], [8, 15], [8, 16]],           # DOZE
            [[8, 17], [8, 18], [9, 0], [9, 1], [9, 2]],     # TREZE
            [[9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]],   # CATORZE
            [[9, 10], [9, 11], [9, 12], [9, 13], [9, 14], [9, 15]],     # QUINZE
            [[9, 16], [9, 17], [9, 18], [10, 0], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5]],        # DEZESSEIS
            [[10, 6], [10, 7], [10, 8], [10, 9], [10, 10], [10, 11], [10, 12], [10, 13], [10, 14]],  # DEZESSETE
            [[10, 15], [10, 16], [10, 17], [10, 18], [11, 0], [11, 1], [11, 2]],                     # DEZOITO
            [[11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10]],               # DEZENOVE
        ]

        minutes_numbers = list()

        if minutes < 10 or minutes >= 20:
            if minutes % 10 != 0:
                units = minutes % 10
                minutes_numbers.extend(minutes_units[units-1])

                if minutes > 20:
                    tenths = minutes // 10
                    minutes_numbers.extend(minutes_tenths[tenths-2])
                    minutes_numbers.extend([[7, 5]])  # E
            else:
                if minutes > 20:
                    tenths = minutes // 10
                    minutes_numbers.extend(minutes_tenths[tenths-2])

        else:
            minutes_numbers.extend(minutes_teens[minutes % 10])

        output = minutes_text
        output.extend(minutes_numbers)

        return output

    def translate_time(self, hours, minutes, seconds):
        """
            A partir da hora inserida, retorna quais letras devem ser iluminadas. O ponto de segundos
            fica piscando
        """

        illuminated_letters = list()

        illuminated_letters.extend(self.translate_hours(hours=hours))
        illuminated_letters.extend(self.translate_minutes(minutes=minutes))

        if seconds % 2 == 0:
            illuminated_letters.extend([[11, 18]])  # Faz o último ponto piscar

        return illuminated_letters

    def update_time(self):
        """
            Rotina para atualizar a tela do relógio
        """
        # Reseta as cores das letras
        for i in range(0, len(self.letters)):
            for j in range(0, len(self.letters[i])):
                self.labels["label_" + str(i) + "_" + str(j)].config(
                    fg=COLOR_OFF, bg=BACKGROUND, font="Helvetica 16"
                )

        current_time = time.localtime()

        hours = int(time.strftime("%H", current_time))
        minutes = int(time.strftime("%M", current_time))
        seconds = int(time.strftime("%S", current_time))

        # Teste do relógio:
        # hours = 0  # 0 a 23
        # minutes = seconds

        illuminated_letters = self.translate_time(
            hours=hours, minutes=minutes, seconds=seconds
        )

        # Ilumina as letras conforme a hora
        for letter in illuminated_letters:
            self.labels["label_" + str(letter[0]) + "_" + str(letter[1])].config(
                fg=COLOR_ON, bg=BACKGROUND, font="Helvetica 16 bold"
            )

        self.after(1000, self.update_time)


if __name__ == "__main__":
    sentence_clock = Clock()
    sentence_clock.mainloop()
