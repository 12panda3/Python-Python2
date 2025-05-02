1. Qual empresa você está modelando, quais tipos de usuário vão usufruir do sistema e quais produtos e serviços a empresa oferece;

  é um sistema básico para uma empresa poder monitorar seus produtos, com diferentes níveis de permissão, podendo editar tanto os produtos quanto quem pode editar eles
  a ideia é que poucas pessoas possam utilizar o sistema, então me deixei relaxar com etapas extras de segurança

2. Para cada elemento da sua solução (usuário e produto/serviço) você deve: 
(1) descrever a estrutura de dados escolhida para carregar as informações,
(2) como o arquivo de registro está estruturado e 
(3) a lista de funcionalidades daquele elemento (associe cada funcionalidade a uma letra da sigla CRUD).

  usei csv para ambos afim de mantes a simplicidade e familiaridade, assim seria mais facil para os administradores poderem corrijir qualquer possivel erro futuro nos bancos de dados
  o banco de dados está estruturado de forma simples, usando id como base para editar e localizar os usuarios e produtos
  é possivel C: criar usuarios e produtos, usando uma janela separada, R: imprimir os bancos de dados nas próprias janelas, assim como filtrar e buscar produtos, U: é possivel atualizar todos dado (exceto id) dos usuarios 
  e produtos pela propria interface separada, e D: deletar usuarios e produtos, sem correr o risco de apagar o cabecalho.

3. Aproveite esse espaço para descrever coisas como dificuldades encontradas, escolhas bem sucedidas, o que faria diferente, etc.

  achei excentrico utilizar tantas funcoes e operacoes em conjunto ao mesmo tempo, assim como tive dificuldade para aplicar a logica, principalmente em interacao com o banco de dados
  achei uma boa escolha usar janelas separadas para o aplicativo, me pareceu uma escolha boa para que os usuarios menos acostumados com terminais possam utilizar o aplicativo, apesar de ter me
  dados algumas dificuldades adicionais
  tirando adicionar mais niveis de seguranca e verificacoes, nao acho que haja nada que necessite ser adicionado, é simples, mas funcional

