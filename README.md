# Mission Control AI - Global Solution

## Descrição do Projeto
O Mission Control AI é um sistema de simulação de monitoramento de uma missão espacial experimental desenvolvido em Python. O sistema analisa dados de diferentes ciclos da missão, identifica riscos operacionais e gera relatórios automáticos para apoio à tomada de decisão.

Ele avalia variáveis críticas como: temperatura interna, comunicação com a base, sistema de energia, suporte de oxigênio e estabilidade operacional.

---

## Missão
Orion Test Alpha

## Equipe
Equipe Apollo  
Projeto desenvolvido individualmente

---

## Objetivo
Simular um sistema de controle de missão espacial utilizando lógica de programação em Python, com análise de risco baseada em regras condicionais.

---

## Estrutura dos dados
Os dados são armazenados em uma matriz chamada dados_missao, onde cada linha representa um ciclo da missão e segue a ordem: temperatura, comunicacao, bateria, oxigenio e estabilidade.

---

## Áreas monitoradas
Temperatura interna, comunicação com a base, sistema de energia, suporte de oxigênio e estabilidade operacional.

---

## Regras de classificação
Temperatura: normal até 30°C, atenção entre 31°C e 35°C, crítico acima de 35°C. Comunicação: normal acima de 60%, atenção entre 30% e 59%, crítico abaixo de 30%. Bateria: normal acima de 50%, atenção entre 20% e 49%, crítico abaixo de 20%. Oxigênio: normal acima de 90%, atenção entre 80% e 89%, crítico abaixo de 80%. Estabilidade: normal acima de 70%, atenção entre 40% e 69%, crítico abaixo de 40%.

---

## Sistema de pontuação
NORMAL vale 0 ponto, ATENÇÃO vale 1 ponto e CRÍTICO vale 2 pontos.

---

## Classificação da missão
0 a 2 pontos significa MISSÃO ESTÁVEL, 3 a 5 pontos significa MISSÃO EM ATENÇÃO e 6 a 10 pontos significa MISSÃO CRÍTICA.

---

## Funcionalidades do sistema
O sistema realiza análise automática de ciclos da missão, cálculo de risco por sistema, classificação de cada ciclo, geração de recomendações automáticas, análise de tendência (melhora ou piora), identificação da área mais afetada e geração de relatório final completo no terminal.

---

## Como executar
Execute o projeto com o comando: python mission_control.py

---

## Estrutura do projeto
mission-control-ai/ contém mission_control.py, README.md e entrega.txt.

---

## Exemplo de funcionamento
O sistema analisa cada ciclo da missão, gera status de cada sistema, pontuação de risco, classificação do ciclo e recomendação automática. No final, apresenta um relatório com médias dos sistemas, ciclo mais crítico, tendência da missão, área mais afetada e classificação final.

---

## Conclusão
O Mission Control AI demonstra como a programação em Python pode ser usada para simular sistemas reais de monitoramento e tomada de decisão em ambientes críticos como missões espaciais.
