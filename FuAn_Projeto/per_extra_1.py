from time import sleep
import PySimpleGUI as sg


def espaco():
    print(' ')
    sleep(1)


def um_extra():
    while True:
        espaco()
        sg.popup('Ele decide ficar em casa estudando, pois dentro de si sabia que poderia se esforçar mais.\n'
                 'Ele mesmo se questiona sobre, se perguntando se talvez ver coisas novas pudesse tirá-lo do medo.\n'
                 'Mas é claro que ele pensa que coisas novas podem tirá-lo do foco, e isso, bom...ele não pode perder.', title='', keep_on_top=True)
        espaco()
        sg.popup('Sua ansiedade bate forte durante as horas que passa pensando em como seguir em frente. Ele percebe que pode estar entrando em crise.\n'
                 'O grande dia era daqui a uma semana, e ele sente que ainda não estava preparado. Mas o que faltava? O menino é incapaz de se responder...', title='')
        espaco()
        sg.popup('Takumi apenas deita em sua cama, põe seus fones de ouvido, escuta um som não muito "agradável" com guitarras pesadas.\n'
                 'Ele acha que isso pode acalma-lo de alguma forma, já que não tinha vontade de tocar piano, mas não sentia vontade de sair...\n'
                 'No final ele não estava fazendo nada! Não estava se distraindo, não estava estudando, e quando parava pra pensar ficava tudo muito pior.\n'
                 'Ele permanecee em silencio na frente de seus familiares e amigos, achando que talvez dessa forma ele pudesse manter o controle.\n'
                 'ão tocar no assunto era o melhor a se fazer na cabeça dele.', title='', keep_on_top=True)
        espaco()
        per_extra_um = sg.popup_yes_no('E o tão aguardado dia havia chegado. Takumi se prepara para subir ao palco, totalmente intimidado pela pressão.\n'
                                       'Ele sobe e se senta na cadeira em frente ao piano, segurando uma pasta preta com tudo que precisava ser tocado.\n'
                                       'O seu silencio durante toda aquela semana vez com que ele refletisse sobre o momento que está agora,que não é dos melhores.\n'
                                       'Takumi deve tentar tocar mesmo achando que não está preparado o suficiente?', title='', keep_on_top=True)

        if per_extra_um is None:
            if sg.popup_yes_no("Tem certeza de que deseja fechar o jogo?") == "Yes":
                break

        espaco()
        if per_extra_um == 'Yes':
            sg.popup('Em meio ao caos e paranoia que estava sua mente ele decide criar coragem. O que poderia dar errado? Alías ele fazia isso a muito tempo.\n'
                     'O piano já estava no seu DNA como qualquer outra caracteristica que ele possuia. O menino sabia que deveria ter procurado ajuda,\n'
                     'sabia que precisava ter enfrentado isso antes, mas a hora de ter coragem era agora!', title='', keep_on_top=True)
            espaco()
            sg.popup('E cada nota, cada batida no teclado, cada erro, cada acerto, cada gesto...Tudo fazia aquela musica se tornar a voz de sua liberdade.\n'
                     'Naquele momento não existia ansiedade que pudesse impedi-lo de terminar o que estava fazendo. O nervosismo batia mas era repelido\n'
                     'pela vontade de mostrar a todos o que estava escondendo.', title='', keep_on_top=True)
            espaco()
            sg.popup('No final de tudo ele conseguiu o que tanto queria. A performance de Takumi fez com que ele fosse admitido no colegio de musica.\n'
                     'O jovem pianista sabe que o processo poderia ter sido mais leve, que tudo poderia ter sido menos doloroso, e ele não quer passar por\n'
                     'isso novamente.', title='', keep_on_top=True)
            espaco()
            sg.popup('Takumi começa a se consultar com uma psicologa e a estudar formas de respiração alternativa. Ele quer melhorar e fazer tudo\n'
                     'de uma forma mais racional. Certamente ele chegará longe com seu esforço', title='', keep_on_top=True)
            break

        elif per_extra_um == 'No':
            sg.popup('A confusão mental de Takumi fez com que ele paralisasse na frente do instrumento. Mesmo com todos ali torcendo pra que ele vencesse.\n'
                     'Ele pega sua pasta, e corre para fora do palco, mesmo sabendo que estava abandonando o seu sonho naquele instante. Mas algo poderia mudar neste instante.', title='', keep_on_top=True)
            espaco()
            sg.popup('Yuichi, seu amigo, aparece bem em cima do palco, assim que Takumi o deixa. Yuichi grita a todos que Takumi só havia saído para beber uma agua e que já voltava.\n'
                     'Essa foi a sua forma de ganhar tempo, e fazer Takumi perceber que ele nunca esteve sozinho em sua caminhada.', title='', keep_on_top=True)
            espaco()
            sg.popup('O jovem pianista mesmo aflito decide voltar ao palco. Ele não poderia deixar os esforços de seu amigo serem em vão.\n'
                     'Ele decide se arriscar...', title='', keep_on_top=True)
            espaco()
            sg.popup(
                'E cada nota, cada batida no teclado, cada erro, cada acerto, cada gesto...Tudo fazia aquela musica se tornar a voz de sua liberdade.\n'
                'Naquele momento não existia ansiedade que pudesse impedi-lo de terminar o que estava fazendo. O nervosismo batia mas era repelido\n'
                'pela vontade de mostrar a todos o que estava escondendo.', title='', keep_on_top=True)
            espaco()
            sg.popup(
                'No final de tudo ele conseguiu o que tanto queria. A performance de Takumi fez com que ele fosse admitido no colegio de musica.\n'
                'O jovem pianista sabe que o processo poderia ter sido mais leve, que tudo poderia ter sido menos doloroso, e ele não quer passar por\n'
                'isso novamente.', title='', keep_on_top=True)
            espaco()
            sg.popup('Takumi agradece o seu amigo que diz que era o minimo que ele poderia fazer, e imaginava que Takumi poderia estar mal\n'
                     'devido o seu afastamento.\n')
            espaco()
            sg.popup('Takumi começa a se consultar com uma psicologa por recomendação de Yuichi (a qual tem desabafado muito\n'
                     ' e a estudar formas de respiração alternativa. Ele quer melhorar e fazer tudo\n'
                     'de uma forma mais racional. Certamente ele chegará longe com seu esforço', title='', keep_on_top=True)
            break

