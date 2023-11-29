import PySimpleGUI as sg

def lay_final():
    layout_final = [
        [sg.Text('Parabéns! Você concluiu a jornada de Takumi Yamamoto.', font=('Times New Roman', 20))],
        [sg.Text('"A ansiedade é uma reação natural do corpo relacionada à preocupação e ao medo."')],
        [sg.Text('Isso tem repercussão no psicológico de quem a possui quando ela torna-se um excesso e passa')],
        [sg.Text('a atrapalhar as atividades rotineiras do mesmo.')],
        [sg.Text('Querido jogador, saiba que a superação da ansiedade é uma jornada desafiadora, mas repleta de crescimento')],
        [sg.Text('pessoal. Não desista quando as dificuldades surgirem. Lembre-se de respirar fundo, enfrentar seus medos e')],
        [sg.Text('confiar em sua capacidade de lidar com eles. Você é mais forte do que imagina e acredite que é possível')],
        [sg.Text('alcançar a paz interior que tanto deseja. Mantenha-se firme e lembre-se de que cada passo dado na direção')],
        [sg.Text('da superação é uma vitória em si mesma. Estaremos aqui torcendo por você!')],
        [sg.Image(filename='image_final.png', key='image_final')],
        [sg.Text('', (38, 1)), sg.Button('Sair', button_color=('black', 'yellow'), border_width=2, size=(15, 2))]
    ]

    window_final = sg.Window('Final do Jogo', layout_final)

    while True:
        event_final, values_final = window_final.read()

        if event_final == sg.WIN_CLOSED or event_final == 'Sair':
            window_final.close()
            break
