import connection as cn
import socket
def main():
    
    # Inicializa a conexão
    c = cn.connect(2037)
       
    # Verifica se conectou com sucesso
    if isinstance(c, socket.socket):
        
        # Código para o algoritmo de aprendizado
        # Ações possíveis:
        # "left" = Girar para a Esquerda
        # "right" = Girar para a Direita
        # "jump" = Pular para a Frente        
        print("Conectado com sucesso")
        estado, recompensa = cn.get_state_reward(c, "jump")
    else:
        print("Falha na conexão")
main()