#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🚀 MATEMÁTICA FINANCEIRA - RESOLUÇÃO COMPLETA DA PROVA (DO ZERO)
=============================================================================
Um guia visual, colorido e didático para entender cada conceito.

🎨 LEGENDA DE CORES (Semáforo Financeiro):
   🟢 VERDE   = Dinheiro ENTRANDO (Receitas, Lucros, Amortização)
   🔴 VERMELHO = Dinheiro SAINDO (Custos, Juros, Impostos, Saldo Devedor)
   🔵 AZUL    = Fórmulas, Taxas, Tempo (A Máquina do Tempo)
   🟡 AMARELO = ⚠️ ALERTAS e PEGADINHAS da prova
=============================================================================
"""

import numpy as np

# ==========================================
# 🎨 CONFIGURAÇÃO VISUAL DO TERMINAL
# ==========================================
class Cores:
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AZUL = '\033[94m'
    AMARELO = '\033[93m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m'

def titulo(texto):
    """Imprime um título destacado"""
    print(f"\n{Cores.CIANO}{Cores.NEGRITO}{'='*70}")
    print(f"  🚀 {texto}")
    print(f"{'='*70}{Cores.RESET}\n")

def subtitulo(texto):
    """Imprime um subtítulo"""
    print(f"\n{Cores.AZUL}{Cores.NEGRITO}▶ {texto}{Cores.RESET}")

def alerta(texto):
    """Imprime um alerta importante"""
    print(f"{Cores.AMARELO}⚠️  {texto}{Cores.RESET}")

def conceito(texto):
    """Imprime um conceito teórico"""
    print(f"{Cores.MAGENTA}💡 CONCEITO: {texto}{Cores.RESET}")

def formula(texto):
    """Imprime uma fórmula"""
    print(f"{Cores.AZUL}📐 FÓRMULA: {texto}{Cores.RESET}")

def resultado(texto, valor=None):
    """Imprime um resultado"""
    if valor is not None:
        print(f"{Cores.VERDE}✅ {texto}: R$ {valor:,.2f}{Cores.RESET}")
    else:
        print(f"{Cores.VERDE}✅ {texto}{Cores.RESET}")

def saida(texto, valor=None):
    """Imprime uma saída/custo"""
    if valor is not None:
        print(f"{Cores.VERMELHO}💸 {texto}: R$ {valor:,.2f}{Cores.RESET}")
    else:
        print(f"{Cores.VERMELHO}💸 {texto}{Cores.RESET}")

# ==========================================
# 📚 ITEM 1: MARGEM DE CONTRIBUIÇÃO, IR, VPL, TIR E PAYBACK
# ==========================================
titulo("ITEM 1: A Máquina de Fazer Dinheiro e o Leão do IR")

conceito("Margem de Contribuição = Preço - Custos Variáveis")
conceito("É o quanto cada venda contribui para pagar os custos fixos e gerar lucro.")
formula("Margem Total = Margem Unitária × Quantidade Vendida")
formula("Lucro Operacional = Margem Total - Custos Fixos")
formula("Imposto de Renda = Lucro Operacional × Alíquota (33%)")
formula("Lucro Líquido = Lucro Operacional - IR")

# Dados da prova
preco_unitario = 7.0
cv_unitario = 4.5
quantidade = 10000
custos_fixos = 18000
aliquota_ir = 0.33

# Cálculos
margem_unitaria = preco_unitario - cv_unitario
margem_total = margem_unitaria * quantidade
lucro_operacional = margem_total - custos_fixos
imposto_renda = lucro_operacional * aliquota_ir
lucro_liquido_atual = lucro_operacional - imposto_renda

subtitulo("Demonstração de Resultados do Último Mês")
print(f"  🟢 Receita Líquida: R$ {preco_unitario} × {quantidade} = R$ {preco_unitario * quantidade:,.2f}")
print(f"  🔴 Custos Variáveis: R$ {cv_unitario} × {quantidade} = R$ {cv_unitario * quantidade:,.2f}")
resultado("Margem de Contribuição", margem_total)
saida("Custos Fixos", custos_fixos)
print(f"  🔵 Lucro Operacional: R$ {lucro_operacional:,.2f}")
print(f"  🔴 IR (33%): R$ {imposto_renda:,.2f}")
resultado("Lucro Líquido Mensal", lucro_liquido_atual)

# ==========================================
# 📊 ANÁLISE DO NOVO PROJETO (VPL, TIR, PAYBACK)
# ==========================================
subtitulo("Análise do Novo Projeto: Investimento de R$ 12.000")

alerta("O projeto aumenta 1.000 unidades/mês, EXCETO em Janeiro (mês 1) e Julho (mês 7)")
alerta("As taxas são MENSAIS. Cuidado com conversões!")

# Cálculo do aumento na margem
aumento_unidades = 1000
aumento_margem_bruta = aumento_unidades * margem_unitaria  # 1000 × 2.5 = 2.500

# Fluxo de caixa líquido mensal (pós-IR)
# O IR incide APENAS sobre o lucro adicional
aumento_lucro_liquido = aumento_margem_bruta * (1 - aliquota_ir)  # 2500 × 0.67 = 1.675

subtitulo("Fluxo de Caixa do Projeto (12 meses)")
print(f"  🔵 Aumento Bruto Mensal: R$ {aumento_margem_bruta:,.2f}")
print(f"  🔴 IR sobre Lucro Adicional (33%): R$ {aumento_margem_bruta * aliquota_ir:,.2f}")
resultado("Fluxo Líquido Mensal (pós-IR)", aumento_lucro_liquido)

# Criando o fluxo de caixa completo
investimento_inicial = 12000
fluxos_33 = [-investimento_inicial]  # Mês 0: investimento (saída)

for mes in range(1, 13):
    if mes == 1 or mes == 7:  # Férias (Janeiro e Julho)
        fluxos_33.append(0)
    else:
        fluxos_33.append(aumento_lucro_liquido)

print(f"\n  Fluxo de Caixa: {fluxos_33}")

# ==========================================
# 📈 ITEM 1a: VPL com taxa de 13% e 33%
# ==========================================
subtitulo("ITEM 1a: VPL (Valor Presente Líquido)")

conceito("VPL traz todos os fluxos futuros para o valor de HOJE")
formula("VPL = Σ [Fluxo_t / (1 + i)^t]")
conceito("Se VPL > 0: Projeto VIÁVEL (gera valor)")
conceito("Se VPL < 0: Projeto INVIÁVEL (destrói valor)")

def calcular_vpl(fluxos, taxa):
    """Calcula o VPL de uma série de fluxos"""
    vpl = sum([fluxos[t] / (1 + taxa)**t for t in range(len(fluxos))])
    return vpl

# VPL com taxa de 13%
taxa_13 = 0.13
vpl_13 = calcular_vpl(fluxos_33, taxa_13)
print(f"\n  🔵 Taxa de Oportunidade: {taxa_13*100}% a.m.")
resultado("VPL (taxa 13%)", vpl_13)
if vpl_13 > 0:
    print(f"  {Cores.VERDE}✅ PROJETO VIÁVEL com taxa de 13%{Cores.RESET}")
else:
    print(f"  {Cores.VERMELHO}❌ PROJETO INVIÁVEL com taxa de 13%{Cores.RESET}")

# VPL com taxa de 33%
taxa_33 = 0.33
vpl_33 = calcular_vpl(fluxos_33, taxa_33)
print(f"\n  🔵 Taxa de Oportunidade: {taxa_33*100}% a.m.")
resultado("VPL (taxa 33%)", vpl_33)
if vpl_33 > 0:
    print(f"  {Cores.VERDE}✅ PROJETO VIÁVEL com taxa de 33%{Cores.RESET}")
else:
    print(f"  {Cores.VERMELHO}❌ PROJETO INVIÁVEL com taxa de 33%{Cores.RESET}")

# ==========================================
# 📈 ITEM 1b: TIR (Taxa Interna de Retorno)
# ==========================================
subtitulo("ITEM 1b: TIR (Taxa Interna de Retorno)")

conceito("TIR é a taxa que faz o VPL ser IGUAL A ZERO")
conceito("É o 'rendimento' real do projeto")
formula("TIR: taxa 'i' tal que VPL = 0")
alerta("Usamos np.irr() do NumPy para calcular")

tir = np.irr(fluxos_33) * 100  # np.irr retorna em decimal
print(f"\n  🔵 TIR do Projeto: {tir:.2f}% a.m.")
print(f"  🔵 Comparação com Taxa de Oportunidade (33%):")
if tir > 33:
    print(f"  {Cores.VERDE}✅ TIR ({tir:.2f}%) > Taxa (33%) → PROJETO VIÁVEL{Cores.RESET}")
else:
    print(f"  {Cores.VERMELHO}❌ TIR ({tir:.2f}%) < Taxa (33%) → PROJETO INVIÁVEL{Cores.RESET}")

# ==========================================
# 📈 ITEM 1c: PAYBACK DESCONTADO
# ==========================================
subtitulo("ITEM 1c: Payback Descontado")

conceito("Payback = Tempo para recuperar o investimento inicial")
conceito("Payback DESCONTADO = Considera o valor do dinheiro no tempo (traz fluxos a valor presente)")
formula("Payback Descontado: acumular fluxos descontados até igualar o investimento")

def calcular_payback_descontado(fluxos, taxa):
    """Calcula o payback descontado"""
    acumulado = 0
    for t in range(len(fluxos)):
        fluxo_descontado = fluxos[t] / (1 + taxa)**t
        acumulado += fluxo_descontado
        if acumulado >= 0:
            return t, acumulado
    return None, acumulado

# Payback com taxa de 33%
mes_payback_33, acumulado_33 = calcular_payback_descontado(fluxos_33, taxa_33)
print(f"\n  🔵 Taxa de desconto: {taxa_33*100}% a.m.")
if mes_payback_33 is not None:
    print(f"  {Cores.VERDE}✅ Payback Descontado ocorreu no mês {mes_payback_33}{Cores.RESET}")
    print(f"  {Cores.VERDE}   Saldo acumulado: R$ {acumulado_33:,.2f}{Cores.RESET}")
else:
    print(f"  {Cores.VERMELHO}❌ Payback Descontado NÃO ocorreu em 12 meses{Cores.RESET}")
    print(f"  {Cores.VERMELHO}   Saldo acumulado: R$ {acumulado_33:,.2f}{Cores.RESET}")
    
    # Calcular payback simples (não descontado)
    alerta("Calculando Payback SIMPLES (não descontado)...")
    acumulado_simples = 0
    for t in range(len(fluxos_33)):
        acumulado_simples += fluxos_33[t]
        if acumulado_simples >= 0:
            print(f"  {Cores.AMARELO}⚠️  Payback Simples ocorreu no mês {t}{Cores.RESET}")
            break

# Payback com taxa de 13%
mes_payback_13, acumulado_13 = calcular_payback_descontado(fluxos_33, taxa_13)
print(f"\n  🔵 Taxa de desconto: {taxa_13*100}% a.m.")
if mes_payback_13 is not None:
    print(f"  {Cores.VERDE}✅ Payback Descontado ocorreu no mês {mes_payback_13}{Cores.RESET}")
    print(f"  {Cores.VERDE}   Saldo acumulado: R$ {acumulado_13:,.2f}{Cores.RESET}")
else:
    print(f"  {Cores.VERMELHO}❌ Payback Descontado NÃO ocorreu em 12 meses{Cores.RESET}")
    print(f"  {Cores.VERMELHO}   Saldo acumulado: R$ {acumulado_13:,.2f}{Cores.RESET}")

# ==========================================
# 📈 ITEM 1d: E se o IR fosse 13%?
# ==========================================
subtitulo("ITEM 1d: E se o Imposto de Renda fosse 13%?")

alerta("Agora a alíquota do IR é 13%, não 33%")

# Recalcular fluxo com IR de 13%
aliquota_ir_13 = 0.13
aumento_lucro_liquido_13 = aumento_margem_bruta * (1 - aliquota_ir_13)  # 2500 × 0.87 = 2.175

fluxos_ir13 = [-investimento_inicial]
for mes in range(1, 13):
    if mes == 1 or mes == 7:
        fluxos_ir13.append(0)
    else:
        fluxos_ir13.append(aumento_lucro_liquido_13)

print(f"\n  🔵 Novo Fluxo Líquido Mensal (IR 13%): R$ {aumento_lucro_liquido_13:,.2f}")

# VPL com IR de 13% e taxa de oportunidade de 13%
vpl_ir13_taxa13 = calcular_vpl(fluxos_ir13, taxa_13)
print(f"\n  🔵 VPL (IR=13%, taxa=13%): R$ {vpl_ir13_taxa13:,.2f}")
if vpl_ir13_taxa13 > 0:
    print(f"  {Cores.VERDE}✅ PROJETO VIÁVEL{Cores.RESET}")
else:
    print(f"  {Cores.VERMELHO}❌ PROJETO INVIÁVEL{Cores.RESET}")

# TIR com IR de 13%
tir_ir13 = np.irr(fluxos_ir13) * 100
print(f"\n  🔵 TIR (IR=13%): {tir_ir13:.2f}% a.m.")

# ==========================================
# 🏦 ITEM 2: SISTEMAS DE AMORTIZAÇÃO (PRICE E SAC)
# ==========================================
titulo("ITEM 2: O Vilão (PRICE) e o Mocinho (SAC)")

conceito("Financiamento de R$ 12.000 em 24 meses")
alerta("Taxa de 33% a.a. (ao ano) - PRECISA CONVERTER PARA MENSAL!")
formula("Taxa Mensal Equivalente = (1 + taxa_anual)^(1/12) - 1")
alerta("NÃO basta dividir 33% por 12! Isso é juros simples!")

# Dados
pv = 12000
taxa_anual = 0.33
n_meses = 24

# Conversão correta da taxa
taxa_mensal = (1 + taxa_anual)**(1/12) - 1
print(f"\n  🔵 Taxa Anual: {taxa_anual*100}%")
print(f"  🔵 Taxa Mensal Equivalente: {taxa_mensal*100:.4f}%")

# ==========================================
# 🏦 ITEM 2e: PRICE - Saldo Devedor após 5ª parcela
# ==========================================
subtitulo("ITEM 2e: PRICE - Saldo Devedor após 5ª prestação")

conceito("Sistema PRICE: Prestações CONSTANTES")
formula("PMT = PV × [i(1+i)^n] / [(1+i)^n - 1]")
conceito("Saldo Devedor = Valor Presente das parcelas que FALTAM pagar")

# Cálculo da prestação
pmt_price = pv * (taxa_mensal * (1 + taxa_mensal)**n_meses) / (((1 + taxa_mensal)**n_meses) - 1)
print(f"\n  🔴 Valor da Prestação Constante: R$ {pmt_price:,.2f}")

# Saldo devedor após 5ª parcela
prestacoes_pagas = 5
prestacoes_restantes = n_meses - prestacoes_pagas
saldo_devedor_price = pmt_price * (1 - (1 + taxa_mensal)**-prestacoes_restantes) / taxa_mensal

print(f"\n  🔵 Prestações pagas: {prestacoes_pagas}")
print(f"  🔵 Prestações restantes: {prestacoes_restantes}")
saida("Saldo Devedor após 5ª prestação", saldo_devedor_price)

# ==========================================
# 🏦 ITEM 2f: SAC - Valor da 6ª prestação
# ==========================================
subtitulo("ITEM 2f: SAC - Valor da 6ª prestação")

conceito("Sistema SAC: Amortização CONSTANTE, prestações DECRESCENTES")
formula("Amortização = PV / n")
formula("Prestação_t = Amortização + (Saldo_Devedor_(t-1) × i)")

# Cálculo da amortização constante
amortizacao_sac = pv / n_meses
print(f"\n  🟢 Amortização Constante: R$ {amortizacao_sac:,.2f}")

# Saldo devedor após 5ª prestação no SAC
saldo_apos_5 = pv - (amortizacao_sac * prestacoes_pagas)
print(f"  🔴 Saldo Devedor após 5ª prestação: R$ {saldo_apos_5:,.2f}")

# Juros da 6ª prestação (incidem sobre o saldo após a 5ª)
juros_6 = saldo_apos_5 * taxa_mensal
print(f"  🔴 Juros da 6ª prestação: R$ {juros_6:,.2f}")

# Valor da 6ª prestação
prestacao_sac_6 = amortizacao_sac + juros_6
print(f"  🟢 Valor da 6ª Prestação: R$ {prestacao_sac_6:,.2f}")

# ==========================================
# 🏦 ITEM 2g: PRICE com CARÊNCIA de 6 meses
# ==========================================
subtitulo("ITEM 2g: PRICE com CARÊNCIA de 6 meses")

alerta("CARÊNCIA = Não paga nada durante 6 meses")
alerta("Os juros NÃO PAGOS são incorporados ao saldo devedor (JUROS SOBRE JUROS!)")
formula("Saldo após carência = PV × (1 + i)^carência")

carencia = 6
pv_apos_carencia = pv * (1 + taxa_mensal)**carencia
print(f"\n  🔴 Valor Financiado: R$ {pv:,.2f}")
print(f"  🔴 Período de Carência: {carencia} meses")
saida("Saldo Devedor após carência", pv_apos_carencia)

alerta("Agora calcula a prestação PRICE sobre o novo saldo, mas em 24-6=18 meses")
n_restante_price = n_meses - carencia
pmt_price_carencia = pv_apos_carencia * (taxa_mensal * (1 + taxa_mensal)**n_restante_price) / (((1 + taxa_mensal)**n_restante_price) - 1)
print(f"\n  🔴 Nova Prestação Constante: R$ {pmt_price_carencia:,.2f}")
print(f"  🔵 Prazo restante: {n_restante_price} meses")

# Saldo devedor após 5ª prestação (contando do início do pagamento)
# Como há carência de 6 meses, a 5ª prestação é paga no mês 11 (6+5)
# Restam 18-5 = 13 prestações
prestacoes_restantes_carencia = n_restante_price - prestacoes_pagas
saldo_devedor_carencia = pmt_price_carencia * (1 - (1 + taxa_mensal)**-prestacoes_restantes_carencia) / taxa_mensal

print(f"\n  🔵 Prestações pagas (após carência): {prestacoes_pagas}")
print(f"  🔵 Prestações restantes: {prestacoes_restantes_carencia}")
saida("Saldo Devedor após 5ª prestação (com carência)", saldo_devedor_carencia)

# ==========================================
# 🏦 ITEM 2h: SAC com CARÊNCIA de 6 meses
# ==========================================
subtitulo("ITEM 2h: SAC com CARÊNCIA de 6 meses (6ª prestação)")

alerta("Mesma lógica: saldo aumenta durante a carência")
alerta("Amortização é calculada sobre o saldo APÓS carência")

# Novo saldo após carência (já calculado acima)
print(f"\n  🔴 Saldo após carência: R$ {pv_apos_carencia:,.2f}")

# Amortização constante (sobre o novo saldo)
amortizacao_carencia = pv_apos_carencia / n_restante_price
print(f"  🟢 Nova Amortização Constante: R$ {amortizacao_carencia:,.2f}")

# Saldo após 5ª prestação (contando do início do pagamento)
saldo_apos_5_carencia = pv_apos_carencia - (amortizacao_carencia * prestacoes_pagas)
print(f"  🔴 Saldo Devedor após 5ª prestação: R$ {saldo_apos_5_carencia:,.2f}")

# Juros da 6ª prestação
juros_6_carencia = saldo_apos_5_carencia * taxa_mensal
print(f"  🔴 Juros da 6ª prestação: R$ {juros_6_carencia:,.2f}")

# Valor da 6ª prestação
prestacao_sac_6_carencia = amortizacao_carencia + juros_6_carencia
print(f"  🟢 Valor da 6ª Prestação (com carência): R$ {prestacao_sac_6_carencia:,.2f}")

# ==========================================
# 🎰 ITEM 3: HOT MONEY (Capitalização Diária)
# ==========================================
titulo("ITEM 3: Hot Money - O Cassino dos Bancos")

conceito("Hot Money: Empréstimo entre bancos, renovado DIARIAMENTE")
conceito("Taxa nominal mensal, mas capitalização DIÁRIA")
alerta("Taxa diária = Taxa nominal / 30")
formula("Taxa Efetiva Mensal = (1 + taxa_diária)^30 - 1")

# Dados
taxas_nominais = [0.04, 0.05, 0.06, 0.08]  # 4%, 5%, 6%, 8%
dias_semana = 4
valor_emprestimo = 33000
iof_diario = 0.000082  # 0,0082% ao dia

# ==========================================
# 🎰 ITEM 3i: Taxa efetiva SEM IOF
# ==========================================
subtitulo("ITEM 3i: Taxa Mensal Efetiva (SEM IOF)")

conceito("Desconsiderando o IOF, apenas a capitalização diária dos juros")

for taxa_nom in taxas_nominais:
    taxa_diaria = taxa_nom / 30
    taxa_efetiva = (1 + taxa_diaria)**30 - 1
    
    print(f"\n  🔵 Taxa Nominal: {taxa_nom*100}% a.m.")
    print(f"  🔵 Taxa Diária: {taxa_diaria*100:.4f}%")
    print(f"  🟢 Taxa Efetiva Mensal: {taxa_efetiva*100:.4f}%")

# ==========================================
# 🎰 ITEM 3j: Taxa efetiva COM IOF (pago no final)
# ==========================================
subtitulo("ITEM 3j: Taxa Mensal Efetiva (COM IOF pago no final)")

alerta("IOF de 0,0082% ao dia, mas PAGO APENAS NO FINAL da operação")
conceito("O IOF não é capitalizado diariamente, é um custo adicional no final")
formula("Montante = PV × (1 + i_diária)^dias + (PV × IOF × dias)")

for taxa_nom in taxas_nominais:
    taxa_diaria = taxa_nom / 30
    
    # Calcula o montante após 4 dias
    montante_juros = valor_emprestimo * (1 + taxa_diaria)**dias_semana
    iof_total = valor_emprestimo * iof_diario * dias_semana
    montante_total = montante_juros + iof_total
    
    # Taxa efetiva para o período de 4 dias
    taxa_4dias = (montante_total / valor_emprestimo) - 1
    
    # Taxa efetiva mensal equivalente
    taxa_efetiva_mensal = (1 + taxa_4dias)**(30/dias_semana) - 1
    
    print(f"\n  🔵 Taxa Nominal: {taxa_nom*100}% a.m.")
    print(f"  🔴 IOF Total (4 dias): R$ {iof_total:,.2f}")
    print(f"  🔴 Montante Total (juros + IOF): R$ {montante_total:,.2f}")
    print(f"  🟢 Taxa Efetiva (4 dias): {taxa_4dias*100:.4f}%")
    print(f"  🟢 Taxa Efetiva Mensal: {taxa_efetiva_mensal*100:.4f}%")

# ==========================================
# 🛒 ITEM 4: TAXA DE JUROS EM COMPRA PARCELADA
# ==========================================
titulo("ITEM 4: Taxa de Juros em Compra Parcelada")

conceito("Opção 1: Entrada de 33% + 3 parcelas mensais iguais")
conceito("Opção 2: Pagamento à vista com 10% de desconto sobre o preço a prazo")
alerta("Precisamos encontrar a taxa de juros implícita no parcelamento")

# Vamos usar um preço de referência (P) para facilitar
# Preço a prazo = P
# Entrada = 0.33 × P
# Saldo a financiar = 0.67 × P
# 3 parcelas iguais (PMT)

# Preço à vista = 0.90 × P (10% de desconto)

# Para encontrar a taxa, igualamos:
# Valor à vista = Entrada + VP das 3 parcelas
# 0.90P = 0.33P + PMT × [1 - (1+i)^-3] / i

# Mas precisamos encontrar PMT primeiro
# O preço a prazo P = Entrada + 3 × PMT
# P = 0.33P + 3 × PMT
# 0.67P = 3 × PMT
# PMT = 0.67P / 3

# Vamos usar P = 1000 para facilitar os cálculos
preco_prazo = 1000
entrada = 0.33 * preco_prazo
saldo_financiar = preco_prazo - entrada
pmt = saldo_financiar / 3
preco_vista = 0.90 * preco_prazo

print(f"\n  🔵 Preço a Prazo (referência): R$ {preco_prazo:,.2f}")
print(f"  🔴 Entrada (33%): R$ {entrada:,.2f}")
print(f"  🔴 Saldo a Financiar: R$ {saldo_financiar:,.2f}")
print(f"  🔴 Valor da Parcela (PMT): R$ {pmt:,.2f}")
print(f"  🟢 Preço à Vista (com 10% desc.): R$ {preco_vista:,.2f}")

# Agora encontramos a taxa que iguala:
# preço_vista = entrada + PMT × [1 - (1+i)^-3] / i
# Precisamos resolver numericamente (método de tentativa e erro ou np.rate)

# Fluxo de caixa do financiador:
# Mês 0: -preco_vista + entrada (ele recebe a entrada, mas "perde" o preço à vista)
# Na verdade, o fluxo é:
# Mês 0: -saldo_financiar (ele financia esse valor)
# Mês 1, 2, 3: +pmt (ele recebe as parcelas)

fluxo_compra = [-saldo_financiar, pmt, pmt, pmt]

# Usando np.irr para encontrar a taxa
taxa_compra = np.irr(fluxo_compra) * 100

print(f"\n  🔵 Fluxo de Caixa do Financiamento: {fluxo_compra}")
print(f"  🟢 Taxa Mensal de Juros da Operação: {taxa_compra:.2f}% a.m.")

alerta("Essa é a taxa de juros que o vendedor está cobrando no parcelamento!")
alerta("Se você pudesse pegar um empréstimo no banco com taxa menor, valeria mais a pena comprar à vista!")

# ==========================================
# 📊 RESUMO FINAL
# ==========================================
titulo("📊 RESUMO FINAL DOS RESULTADOS")

print(f"\n{Cores.CIANO}{'='*70}")
print(f"  ITEM 1: Análise de Projeto")
print(f"{'='*70}{Cores.RESET}")
print(f"  Lucro Líquido Mensal Atual: R$ {lucro_liquido_atual:,.2f}")
print(f"  VPL (taxa 13%): R$ {vpl_13:,.2f}")
print(f"  VPL (taxa 33%): R$ {vpl_33:,.2f}")
print(f"  TIR do Projeto: {tir:.2f}% a.m.")

print(f"\n{Cores.CIANO}{'='*70}")
print(f"  ITEM 2: Sistemas de Amortização")
print(f"{'='*70}{Cores.RESET}")
print(f"  Taxa Mensal Equivalente: {taxa_mensal*100:.4f}%")
print(f"  PRICE - Prestação: R$ {pmt_price:,.2f}")
print(f"  PRICE - Saldo após 5ª: R$ {saldo_devedor_price:,.2f}")
print(f"  SAC - 6ª Prestação: R$ {prestacao_sac_6:,.2f}")
print(f"  PRICE c/ Carência - Saldo após 5ª: R$ {saldo_devedor_carencia:,.2f}")
print(f"  SAC c/ Carência - 6ª Prestação: R$ {prestacao_sac_6_carencia:,.2f}")

print(f"\n{Cores.CIANO}{'='*70}")
print(f"  ITEM 3: Hot Money")
print(f"{'='*70}{Cores.RESET}")
print(f"  Taxa Efetiva Mensal (4% nominal, sem IOF): {((1+0.04/30)**30-1)*100:.4f}%")

print(f"\n{Cores.CIANO}{'='*70}")
print(f"  ITEM 4: Compra Parcelada")
print(f"{'='*70}{Cores.RESET}")
print(f"  Taxa Mensal de Juros: {taxa_compra:.2f}% a.m.")

print(f"\n{Cores.VERDE}{Cores.NEGRITO}{'='*70}")
print(f"  ✅ PROVA RESOLVIDA COM SUCESSO!")
print(f"{'='*70}{Cores.RESET}\n")

print(f"{Cores.AMARELO}💡 DICA FINAL: Sempre verifique se as taxas e prazos estão na mesma")
print(f"   unidade temporal (mensal com mensal, anual com anual)!{Cores.RESET}\n")
