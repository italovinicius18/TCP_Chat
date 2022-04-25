# TCP_Chat

## Relatório

- Universidade de Brasília
- Curso: Engenharia de Software
- Matéria: Fundamentos de redes de computadores
- Professor: Fernando William

- Integrantes:
    - Ítalo Vinícius P. Guimarães - 18/0102656
    - Álvaro Leles Guimarães - 18/0096991

### Introdução

Projeto final da disciplina "Fundamentos de Redes de computadores", cujo objetivo é criar chats onde qualquer pessoa possa conversar em grupos ou criar um novo, desvendando quais são os possíveis problemas que ocorrem em uma arquitetura de conversas utilizando tcp/ip e cliente-servidor.

A solução para o problema estipulado será desenvolvida por meio das bibliotecas socket e threading, cujas quais já são padrão do Python. Além do que serão implementadas estruturas próprias para armazenar as informações dos membros e dos grupos, como listas e classes de objetos.

### Metodologia

Nos organizamos através de encontros por meio de chamadas no Discord, facilitando o processo de pair programming.

#### Reuniões

- O primeiro encontro foi no dia 20/04/22, onde decidimos que iríamos trabalhar com Python, principalmente por ter mais familiaridade com a linguagem e ela facilitar a implementação de sockets e threads.


- No encontro do dia 25/04/22 decidimos como seria a estrutura e a hierarquia inicial dos componentes, classes e funções em Python. Tentando seguir o padrão

    - main.py que vai utilizar o módulo do cliente.py e assim criar um novo cliente
    - server.py que vai gerir todos os clientes e suas possíveis operações.