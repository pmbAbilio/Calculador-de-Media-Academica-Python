#!/usr/bin/python
from tkinter import *


class GPA_calculator:
    def __init__(self):
        self.window_height = 500
        self.window_width = 500
        self.SEL_SUBJECTS = "Quantas cadeiras tens feitas ? "
        self.SUBJECT_AMOUNT = 0
        self.gui = Tk()
        self.entries = []
        self.ects_entries = []
        self.running = False
        self.createLayout()

        self.gui.mainloop()

    def createLayout(self):
        # self.gui.geometry("500x500")
        self.gui.title("Calculadora de Media Academica")

        self.createTop()
        self.createContent()
        self.createBottom()
        self.createLeftContainer()

    def createTop(self):
        self.topFrame = Frame(self.gui)
        self.topFrame.pack(side=TOP)

        var = StringVar()
        var.set(self.SEL_SUBJECTS)

        # Label numero de Cadeiras
        self.n_subjects_label = Label(self.topFrame, textvariable=var)
        self.n_subjects_label.pack(side=LEFT, padx=5)
        # Input para inserir quantas cadeiras
        self.n_subjects = Entry(self.topFrame)
        self.n_subjects.pack(side=LEFT, padx=5)

        # Botão para gerar a ação
        n_subjects_button = Button(
            self.topFrame,
            text="Gerar Tabela",
            command=self.callbackGenerateSeleters,
            height=1,
        )
        n_subjects_button.pack(side=LEFT, padx=5)

    def createBottom(self):
        self.bottomFrame = Frame(self.gui)
        self.bottomFrame.pack(side=BOTTOM, fill=X)

    def createContent(self):
        self.contentFrame = Frame(self.gui)
        self.contentFrame.pack(side=RIGHT)

    def createLeftContainer(self):
        self.leftContainer = Frame(self.gui)
        self.leftContainer.pack(side=LEFT)

    def callbackGenerateSeleters(self):
        container = self.leftContainer
        column_value = 0
        row_value = 0
        if self.running is False:
            n_subjects_got = self.n_subjects.get()
            subject = StringVar()
            subject.set("Nota Cadeira/Ects(ex: 10-6):")

            for value in range(int(n_subjects_got)):
                if (
                    value == round(int(n_subjects_got) / 2)
                    or value == 25
                    or value == 75
                    or value == 50
                ):
                    column_value += 2
                    row_value = 0
                subjectInput_label = Label(container, textvariable=subject)
                subjectInput_label.grid(row=row_value, column=column_value)

                subjectInput = Entry(container, width=20)
                subjectInput.grid(row=row_value, column=column_value + 1)
                self.entries.append(subjectInput)
                row_value += 1

            submit = Button(
                self.bottomFrame, text="Calcular", command=self.calculateGPA
            )
            submit.pack(side=BOTTOM, fill="x")
            self.running = True

    def calculateGPA(self):
        total_subjects = []
        for entry in self.entries:
            total_subjects.append(str(entry.get()))
        total_ects = 0
        GPA_temp_values = 0
        for row, grade in enumerate(total_subjects):
            GPA_temp_values += int(grade.split("-")[0]) * int(
                total_subjects[row].split("-")[1]
            )
        for e in total_subjects:
            total_ects += int(e.split("-")[1])

        GPA = GPA_temp_values / total_ects
        textBox = Text(self.contentFrame, height=10, width=30)
        textBox.pack(padx=10, pady=5, fill="y")
        if GPA < 12:
            message = "Não estudes não"
        if GPA > 12 and GPA < 15:
            message = "Epah não está mau mas podia ser melhor"
        else:
            message = "Muito bem!!! és um génio"
        textBox.insert(
            "1.0",
            "A tua media é de aprox: {} e abs {}!!!! {} ".format(
                round(GPA), GPA, message
            ),
        )


test = GPA_calculator()

