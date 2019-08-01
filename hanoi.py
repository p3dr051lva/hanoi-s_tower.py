print('Ola, este eh o jogo, torre de hanoi, o jogo tem o objetivo de voce transferir \
os numero da tore um para a torre 3, sem que numeros maiores fiquem em cima de numeros menores, voce\
so pode mover o disco do "topo", e uma por vez, a primeira torre de baixo para cima eh a t1, a segunda a\
t2, e a terceira a t3, para move-los use o seguinte metodo:t1>t2. para movimentar o disco do "topo" da t1 para o "topo" da t2, bom jogo meu paladino')
def hanoi():
    
    t1= [3,2,1]
    t2= []
    t3= []
    torres = [t1, t2, t3]
    aux = 0
    print(t1)
    print(t2)
    print(t3)
    while len(torres[-1]) < 3:
        
        y1, y2 = [int(i[-1]) - 1 for i in input('digite a origem>destino: ').split('>')]
        while len(torres[y1]) == 0 or (len(torres[y2]) > 0 and torres[y1][-1] > torres[y2][-1]):
            print('jogada invalida')
            print(t1)
            print(t2)
            print(t3)
            y1, y2 = [int(i[-1]) - 1 for i in input('digite a origem>destino: ').split('>')]
            
        
        else:
            torres[y2].append(torres[y1].pop())
            aux += 1
        print(t1)
        print(t2)
        print(t3)

    else:
        print('parabens voce completou o quebra-cabeca em %d movimentos' %(aux))
hanoi()
              

        
    
