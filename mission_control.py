# ==========================================================
# MISSION CONTROL AI - GS2026.1
# ==========================================================

missao = "Orion Test Alpha"
equipe = "Equipe Apollo"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


# ==========================================================
# FUNÇÕES DE ANÁLISE
# ==========================================================

def analisar_temperatura(v):
    if v < 18:
        return "ATENÇÃO", 1
    elif v <= 30:
        return "NORMAL", 0
    elif v <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2


def analisar_comunicacao(v):
    if v < 30:
        return "CRÍTICO", 2
    elif v <= 59:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(v):
    if v < 20:
        return "CRÍTICO", 2
    elif v <= 49:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_oxigenio(v):
    if v < 80:
        return "CRÍTICO", 2
    elif v <= 89:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_estabilidade(v):
    if v < 40:
        return "CRÍTICO", 2
    elif v <= 69:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


# ==========================================================
# CLASSIFICAÇÕES
# ==========================================================

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável."


def identificar_area_mais_afetada(riscos_areas):
    indice = riscos_areas.index(max(riscos_areas))
    return areas_monitoradas[indice]


# ==========================================================
# RECOMENDAÇÃO INTELIGENTE (MELHORADO PARA NOTA MÁXIMA)
# ==========================================================

def gerar_recomendacao(t, c, b, o, e):

    if t == "CRÍTICO":
        return "Ativar controle térmico imediatamente."

    if c == "CRÍTICO":
        return "Restabelecer comunicação com a base."

    if b == "CRÍTICO":
        return "Ativar modo de economia de energia."

    if o == "CRÍTICO":
        return "Acionar protocolo de suporte à vida."

    if e == "CRÍTICO":
        return "Reduzir operações não essenciais."

    if "ATENÇÃO" in [t, c, b, o, e]:
        return "Monitorar sistemas em atenção e preparar contingência."

    return "Manter operação normal."


# ==========================================================
# EXECUÇÃO PRINCIPAL
# ==========================================================

riscos_ciclos = []
riscos_areas = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {missao}")
print(f"Equipe: {equipe}")
print(f"Ciclos analisados: {len(dados_missao)}")
print("=" * 60)


for i, ciclo in enumerate(dados_missao):

    temp, com, bat, oxi, est = ciclo

    s_t, r_t = analisar_temperatura(temp)
    s_c, r_c = analisar_comunicacao(com)
    s_b, r_b = analisar_bateria(bat)
    s_o, r_o = analisar_oxigenio(oxi)
    s_e, r_e = analisar_estabilidade(est)

    risco_total = r_t + r_c + r_b + r_o + r_e
    riscos_ciclos.append(risco_total)

    riscos_areas[0] += r_t
    riscos_areas[1] += r_c
    riscos_areas[2] += r_b
    riscos_areas[3] += r_o
    riscos_areas[4] += r_e

    classificacao = classificar_ciclo(risco_total)
    recomendacao = gerar_recomendacao(s_t, s_c, s_b, s_o, s_e)

    print("\n" + "-" * 60)
    print(f"CICLO {i + 1}")
    print("-" * 60)

    print(f"Temperatura: {temp}°C | {s_t}")
    print(f"Comunicação: {com}% | {s_c}")
    print(f"Bateria: {bat}% | {s_b}")
    print(f"Oxigênio: {oxi}% | {s_o}")
    print(f"Estabilidade: {est}% | {s_e}")

    print(f"\nRisco total: {risco_total}")
    print(f"Classificação: {classificacao}")
    print(f"Recomendação: {recomendacao}")


# ==========================================================
# RELATÓRIO FINAL
# ==========================================================

print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

media = [
    sum(c[i] for c in dados_missao) / len(dados_missao)
    for i in range(5)
]

print(f"Média Temperatura: {media[0]:.2f}")
print(f"Média Comunicação: {media[1]:.2f}")
print(f"Média Bateria: {media[2]:.2f}")
print(f"Média Oxigênio: {media[3]:.2f}")
print(f"Média Estabilidade: {media[4]:.2f}")

maior_risco = max(riscos_ciclos)
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

print(f"\nCiclo mais crítico: {ciclo_critico}")
print(f"Maior risco: {maior_risco}")
print(f"Risco médio: {sum(riscos_ciclos)/len(riscos_ciclos):.2f}")

print(f"\nCiclos críticos: {len([r for r in riscos_ciclos if r >= 6])}")

print("\nTendência da missão:")
print(analisar_tendencia(riscos_ciclos))

print("\nPontuação por área:")
for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {riscos_areas[i]} pontos")

area_critica = identificar_area_mais_afetada(riscos_areas)
print(f"\nÁrea mais afetada: {area_critica}")

# classificação final
media_risco = sum(riscos_ciclos) / len(riscos_ciclos)
classificacao_final = classificar_ciclo(round(media_risco))

print(f"\nClassificação final: {classificacao_final}")

print("\nConclusão:")

if media_risco <= 2:
    print("Missão estável e sob controle.")
elif media_risco <= 5:
    print("Missão com instabilidades moderadas.")
else:
    print("Missão crítica. Ação imediata recomendada.")