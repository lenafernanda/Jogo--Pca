from time import sleep
import PySimpleGUI as sg


def espaco():
    print(' ')
    sleep(1)


def tres_extra():
    while True:
        espaco()
        sg.popup('Ele decide de dedicar inteiramente ao seu estudo. Mesmo que pra isso precise sacrificar sua mente.\n'
                 'Takumi já sente sua alma cansada. Ele sente que quanto mais estuda menos sabe, e esse efeito acaba deixando-o\n'
                 'com uma forte crise. Ele sente que deveria se esforçar mais, sente que não está bom o suficiente para sentar na cadeira\n'
                 'do sucesso.',  title='', keep_on_top=True)
        espaco()
        sg.popup('Ele decide virar algumas noites durante a semana, treinando sua canção no piano.\n'
                 'O garoto acredita que desta forma conseguirá chegar onde deseja. Suas mãos já não aguentam o esforço.\n'
                 'Sua mente está estagnada com as escalas que foram feitas no instruemento. Ele sente que sua mente está exalada.\n'
                 'Tudo que ele consegue pensar são notas, são sons, são as teclas. É como se sua vida fosse apenas aquilo...',  title='', keep_on_top=True)
        espaco()
        per_tres_extra = sg.popup_yes_no('E o aguardado dia havia chegado. Takumi preferiu se dedicar inteira a sua performance.\n'
                ' Ele finalmente sobe ao palco,com suas partituras e tablaturas debaixo do braço em uma pasta avermelhada.\n '
                'Ele põe tudo em cima do suporte do piano,para ser tocado durante a sua apresentação. Takumi deve tocar?  ', title='', keep_on_top=True)
        espaco()

        if per_tres_extra is None:
            if sg.popup_yes_no("Tem certeza de que deseja fechar o jogo?") == "Yes":
                break

        if per_tres_extra == 'Yes':
            sg.popup('Ele decide tocar. Não havia como errar, já que havia praticado tanto. Mas não é muito bem isso que acontece.\n'
                     'O jovem musico acaba confundindo algumas notas, ele não entendia o porque daquilo acontecer, e claro\n'
                     'o primeiro erro foi fatal para que ele parasse de tocar ali mesmo. Ele não entendia o motivo do seu fracasso...\n', title='', keep_on_top=True)
            espaco()
            sg.popup('Muito frustrado o jovem sai chutando a cadeira, jogando as partituras ao chão e se retirando em prantos\n'
                     'do palco que poderia fazer do seu futuro o mais perfeito possivel, mas tudo saiu mal...BEM MAL.', title='', keep_on_top=True)
            espaco()
            sg.popup('A familia de Takumi se preocupa com a reação do garoto no palco e o convencem a ir até a psicologa para que ela possa orinta-lo.\n'
                     'Ele nega nas primeiras tentativas mas logo após aceita justamente para entender o que aconteceu consigo mesmo.', title='', keep_on_top=True)
            espaco()
            sg.popup('A psicologa Doutora Matsuda esclarece o garoto sobre o motivo de seu fracasso, dizendo que seu estado mental\n'
                     'não estava nos melhores dias, e possivelmente o estresse e ansiedade acumulados fizeram com que ele não tivesse um bom desempenho.\n'
                     'O descanço tem que ser uma parte importante do processo, e deve ser respeitada assim como o esforço, mas ansiedade aguda do jovem\n'
                     'não permitiu que isso ocorresse.', title='', keep_on_top=True)
            espaco()
            sg.popup('Takumi começa a frequentar semanalmente as sessões da Doutora Matsuda, afim de focar na su saúde mental.\n'
                     'Ele tambem decide praticar atividades que envolvam lazer, fora da sua responsabilidade com a musica.\n'
                     'O menino de Quioto sabe que precisa melhorar seus aspectos mentais para se tornar um profissional mais adequado.', title='', keep_on_top=True)
            espaco()
            sg.popup('E tudo termina com Takumi saindo de casa, com seus fones de ouvido pedurados, descendo a ladeira proxima com sua bicicleta\n'
                     'e claro, ouvindo um belo som de piano. Ele sabe pra onde estava indo, e sabia que conseguiria chegar lá se cobrando menos.\n'
                     'Ele tem a impressão de que estaria nascendo novamente, que as notas que ecoavam vinham de seu coração.', title='', keep_on_top=True)
            espaco()
            sg.popup('Ele certamenbte chegará aonde quiser...', title='', keep_on_top=True)
            break

        elif per_tres_extra == 'No':
            sg.popup('E mesmo depois de ter treinado tanto, mesmo depois de virar noites, de consumir diversos conteúdos sobre piano\n'
                     'parecia que nada disso era suficiente pra dar verdadeira confiança ao menino. Ele se sente uma vergonha por não ter criado coragem.\n'
                     'Não conseguia encarar seus amigos, sua mãe, seus professores...não conseguia encarar a si mesmo. Tudo parecia tão escuro\n'
                     'sordico, imprevisivel, a vida era imprevisivel de mais para o jovem menino, que apenas desejava impressionar a todos... ', title='', keep_on_top=True)
            espaco()
            sg.popup('Sua mente tranbordava de com o nervosismo, ele realmente estava passando muito mal, não tinha mais condições de se manter de pé.\n'
                     'Talvez o caminho dele na musica tivesse terminado ali mesmo...talvez aquele fosse o fim de uma historia que até começou bem.\n'
                     'Ele se senta no chão e se lembra da primeira vez que tocou piano, seus olhos e seu coração brilhavam como fogo, era tão bom...\n'
                     'Não havia a pressão de ser o melhor, havia apenas a vontade de fazer o SEU melhor.', title='', keep_on_top=True)
            espaco()
            sg.popup('Um tempo passa e Takumi é encorajado a procurar ajuda profissional para controlar sua ansiedade de uma vez por todas.\n'
                     'Ele começa a tentar resgatar seu "eu" mais saudavel, para recuperar seu relacionamento com a musica.\n'
                     'O jovem sabe que isso demandará bastante tempo, e que o processo é cansativo, delirante e até mesmo propicio a falhas.\n'
                     'Mas o mesmo estava determinado a se exigir menos, então este processo era extremamente importante pra que ele alcançasse isto no final.', title='', keep_on_top=True)
            espaco()
            sg.popup('O tempo era agonizante, o suficiente para faze-lo entrar em diversas crises, até que ele mesmo aprendeu a controla-las.\n'
                     'Com o tempo elas diminuiam, e ele até se sente confortavel para tocar uma musica qualquer no piano, e ve que aquilo era maravilhoso por si só.\n', title='', keep_on_top=True)
            espaco()
            sg.popup('Takumi respirava melhor, ouvia, sentia e sonhava melhor tambem. Sabendo que não pode negligenciar mais a si mesmo ele segue\n'
                     'em busca de um novo começo, pois talvez o fim seja apenas isso...um novo começo.', title='', keep_on_top=True)
            break





