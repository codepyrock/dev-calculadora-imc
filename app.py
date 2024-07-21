import PySimpleGUI as sg
from funcoes import *

# theme
sg.theme('DarkGreen4')

# layout
layout = [
    [sg.Text('Peso:  (Kg)', size=(15,1)), 
             sg.Input(key='peso', size=(7,1)),             
             sg.Button('OK',key='validar_peso', button_color='MediumAquamarine')
             ],
    [sg.Text('Altura:  (m)', size=(15,1)), 
             sg.Input(key='altura', size=(7,1)),              
             sg.Button('OK', key='validar_altura', button_color='MediumAquamarine'),
             ],
    [sg.Button('Calcular', button_color='MediumAquamarine')],    
    [sg.Text('-------------------------- Relatório --------------------------',
            justification='center', size=(280))
            ],
    [sg.Text('Peso:'), sg.Text('', key='peso_registrado')],
    [sg.Text('Altura:'), sg.Text('', key='altura_registrada')],
    [sg.Text('Resultado IMC:'), sg.Text('', key='imc')],
    [sg.Text('Categoria IMC:'), sg.Text('', key='categoria')],
]
# window
window = sg.Window('IMC Calculator', layout=layout, size=(370,290), font=['TimeNewRoman', 13])

# events and values
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'sair':
        break
    if event == 'validar_peso':
        peso_validado = validar_valor(values['peso'])
        try:
            if peso_validado:
                peso_formatado = formatar_valor(values['peso'])
                window['peso'].update(peso_formatado)
                window['peso_registrado'].update((peso_formatado + ' Kg'))   
                sg.popup("Peso validado")
                 
        except:
            sg.popup_error("Digite apenas números")
            window['peso'].update('')
    if event == 'validar_altura':
        altura_validada = validar_valor(values['altura'])
        try:
            if altura_validada:
                altura_formatada = formatar_valor(values['altura'])
                if float(altura_formatada) < 3:
                    window['altura'].update(altura_formatada)
                    window['altura_registrada'].update((altura_formatada + ' m')) 
                    sg.popup("Altura validada")   
                else:
                    sg.popup_error('Digite a altura em metros')
                    window['altura'].update('')
        except:
            sg.popup_error("Digite apenas números")
            window['altura'].update('')
    if event == 'Calcular':
        try:
            if (window['peso'] or window['altura'] != ''):
                calculo_imc = calcular_imc(peso_formatado, altura_formatada)
                categoria = categoria_imc(calculo_imc)
                cor_categoria = definir_cor(categoria)
                window['imc'].update(calculo_imc)
                window['categoria'].update(categoria, text_color=cor_categoria)
                window['peso'].update('')
                window['altura'].update('')
        except:
            sg.popup_error("Informe peso e altura")
       
window.close()
