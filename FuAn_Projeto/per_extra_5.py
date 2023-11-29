from time import sleep
import PySimpleGUI as sg


def espaco():
    print(' ')
    sleep(1)


def cinco_extra():
    while True:
            espaco()
            sg.popup('- Ele decide se divertir. Yuichi e Takumi vão até o fastfood e comem hambúrgueres deliciosos.\n '
                  '  Yuichi chega a ficar de barriga cheia de tanto que comeu. Depois de comerem decidem dar uma passeio pelas ruas de Quioto.\n '
                  '  Enquanto caminhavam Takumi escuta um belo som de piano vindo da rua de trás e decide ir até lá.\n '
                  '  Yuichi o segue pois estava curioso pra ver o que poderia ser também', title='', keep_on_top=True)
            espaco()
            sg.popup(
                'Takumi vê um garoto de aproximadamente 10 anos experimentando um piano em uma loja de instrumentos.\n '
                'Ele percebe que apesar da pouca idade o garoto possui muita habilidade,julgando que o garoto é um pianista melhor do que ele mesmo...', title='', keep_on_top=True)
            espaco()
            sg.popup(
                'akumi entra em uma crise de ansiedade junto a um sentimento de inferioridade por ver o menino tocando piano.\n '
                'Ele começa a se sentir mal,fica com vontade de ir pra casa e sua respiração começa a entrar em arritmia. ', title='', keep_on_top=True)
            espaco()
            sg.popup(' Ele vai pra casa logo depois do passeio,não decide falar nada,esconde suas emoções pra que seu amigo não perceba.\n '
                  'Ele decide fazer exercícios de respiração para melhorar sua condição.' , title='', keep_on_top=True)
            espaco()
            sg.popup('Ele passa essa semana inteira focando em exercícios para melhorar sua ansiedade e finalmente conseguir tocar com perfeição.\n '
                  'Eliminar suas inseguranças,focar no seu próprio ritmo e desenvolvimento. Takumi se sentia solitário,mas sabia que só ele poderia se tirar desta infeliz situação.', title='', keep_on_top=True)
            espaco()
            sg.popup('Obs: Além da respiração profunda e exercícios de relaxamento, atividades como meditação, exercícios físicos regulares, ter uma rotina estruturada,evitar\n'
                  ' cafeína e álcool, e buscar apoio emocional de amigos e familiares podem ajudar durante uma crise de ansiedade.\n'
                  ' É importante procurar ajuda profissional também.' , title='', keep_on_top=True)
            espaco()
            per_cinco_extra = sg.popup_yes_no('E o aguardado dia havia chegado. Takumi resolveu se cuidar por conta própria,mesmo não sendo o mais recomendado era o que estava no seu alcance.\n'
                                    ' Ele finalmente sobe ao palco,com suas partituras e tablaturas debaixo do braço em uma pasta cor púrpura.\n '
                                    'Ele põe tudo em cima do suporte do piano,para ser tocado durante a sua apresentação. Takumi deve tocar?  ' , title='', keep_on_top=True)

            if per_cinco_extra is None:
                if sg.popup_yes_no("Tem certeza de que deseja fechar o jogo?") == "Yes":
                    break

            espaco()
            if per_cinco_extra == 'Yes':
                sg.popup('E ele decide tocar. Suas mãos estão trêmulas. Tudo parecia tão,tão difícil.\n'
                      'Takumi percebe que está encurralado num labirinto criado pelas suas próprias emoções.\n '
                      'Mas mesmo assim ele decide fazer o melhor que podia. No meio da canção ele percebe que na plateia está seu amigo Yuichi,\n'
                      'sua família e inclusive tutores do colégio de Quioto. Ele poderia ter pedido ajuda,pois aquelas pessoas estavam sempre ali para ele...', title='', keep_on_top=True)
                espaco()
                sg.popup('As coisas não saíram do jeito que ele havia imaginado,mas de alguma forma aquilo se tornou uma experiência pra ele.\n '
                      'Cada nota errada,cada tremida de mão,cada olhar agoniado serviram para que ele percebesse que cuidar de sua própria mente é o mais importante.', title='', keep_on_top=True)
                espaco()
                sg.popup('No final de tudo ele não conseguiu passar para o colégio de música,mas percebe que se cuidar de si mesmo conseguirá ter uma nova chance. ', title='', keep_on_top=True)
                espaco()
                sg.popup('Hoje, Takumi conta com seus amigos para ajuda-lo a enfrentar a ansiedade. Ele já não se sente mais sozinho!', title='', keep_on_top=True)
                break

            elif per_cinco_extra == 'No':
                sg.popup('Naquele momento tudo estava tão escuro em sua mente...')
                espaco()
                sg.popup('Suas mãos tremiam como nunca,seu coração estava apertado. Ele só queria ir embora dali e se livrar daquela pressão.\n'
                      ' Takumi abandona o palco,com lágrimas nos olhos e percebe que na plateia estava sua família,seu melhor amigo e a equipe da escola torcendo por ele.\n '
                      'Ele havia decepcionado a todos...', title='', keep_on_top=True)
                espaco()
                sg.popup('O jovem decide falar a todos sobre o seu problema com a ansiedade.\n '
                      'Todos o acolhem de forma receptiva,oferecendo apoio ao jovem e recomendando e o incentivando a procurar ajuda profissional. ', title='', keep_on_top=True)
                espaco()
                sg.popup('Takumi sabe que nunca será aprovado por ter abandonado os palcos,mas percebe agora que novos caminhos podem surgir em sua vida de forma mais leve,\n'
                      'basta que ele procure cuidar mais de sua saúde mental, percebendo que estava de fato doente. ', title='', keep_on_top=True)
                espaco()
                sg.popup('Lidar com a sua ansiedade abrirá portas para que ele tente novos objetivos.\n '
                      'O menino então se senta em um piano de rua,em frente a um loja de instrumentos e começa a tocar o soneto mais pelo que vem a sua cabeça.\n '
                      'Sem pressão,sem mãos tremidas,sem impaciência. ', title='', keep_on_top=True)
                espaco()
                sg.popup('Naquele momento ele sabia que estava tendo um pedacinho de paz dentro de seu peito!', title='', keep_on_top=True)
                break

            if per_cinco_extra is None:
                if sg.popup_yes_no("Tem certeza de que deseja fechar o jogo?") == "Yes":
                    break