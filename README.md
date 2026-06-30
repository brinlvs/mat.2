# mat.2 
# 💰 Matemática Financeira Descomplicada: Do Básico ao Avançado
> *Um guia visual e dinâmico baseado em cenários reais de provas e mercado.*

## 🎨 Guia de Cores (Memorização Visual)
*   🟢 **VERDE**: <span style="color: #2E8B57;">Dinheiro entrando (Receitas, Margem, Lucro, VPL positivo).</span>
*   🔴 **VERMELHO**: <span style="color: #DC143C;">Dinheiro saindo (Custos, Impostos, Inflação, Prestações).</span>
*   🔵 **AZUL**: <span style="color: #1E90FF;">O Tempo e o Dinheiro (Fórmulas, Taxas, Prazos).</span>
*   🟡 **AMARELO**: <span style="color: #DAA520;">⚠️ ALERTAS (Pegadinhas de prova, como IR e Carência).</span>

---

## 📊 Unidade V: Inflação, Taxa Real e Poder Aquisitivo
**Conceito:** O dinheiro perde valor com o tempo. Ganhar 10% se a inflação é 10% significa que você não ganhou *nada* em poder de compra.

🔵 **Fórmula de Fisher (Taxa Real):**
$$ (1 + i_{nominal}) = (1 + i_{real}) \times (1 + inflação) $$
$$ i_{real} = \frac{1 + i_{nominal}}{1 + inflação} - 1 $$

🟢 **Exemplo Prático:** Você recebeu um aumento de 15% (<span style="color: #2E8B57;">nominal</span>), mas o preço do mercado subiu 10% (<span style="color: #DC143C;">inflação</span>).
*   $i_{real} = (1.15 / 1.10) - 1 = 0,0454$ ou **4,54% de ganho real**.

---

## 📈 Unidade VI: VPL (Valor Presente Líquido) e TIR
**Conceito:** R$ 1.000 hoje valem mais que R$ 1.000 amanhã. O VPL traz todos os fluxos de caixa futuros para a data de hoje.

🔵 **Fórmula do VPL:**
$$ VPL = \sum_{t=0}^{n} \frac{FC_t}{(1+i)^t} $$
*(Onde $FC_t$ é o Fluxo de Caixa no tempo $t$, e $i$ é a taxa de desconto/oportunidade).*

🟡 **⚠️ ALERTA DA PROVA (Imposto de Renda):**
O IR (ex: 33%) só incide sobre o **LUCRO**, não sobre o faturamento bruto!
*   *Fluxo Líquido* = (Receita - Custos Variáveis - Custos Fixos) * (1 - Alíquota IR).

🟢 **TIR (Taxa Interna de Retorno):** É a taxa $i$ que faz o VPL ser exatamente igual a zero. Se a TIR > Taxa de Oportunidade, o projeto é <span style="color: #2E8B57;">viável</span>.

---

## 🔄 Unidade VII: Sequências de Capitais (Séries Uniformes)
**Conceito:** Parcelas iguais e sucessivas (PMT). Usado para financiar carros, imóveis ou criar planos de poupança.

🔵 **Valor Presente de uma Série Uniforme (Quanto posso financiar?):**
$$ PV = PMT \times \left[ \frac{1 - (1+i)^{-n}}{i} \right] $$

🔵 **Montante de uma Série Uniforme (Quanto terei no futuro?):**
$$ FV = PMT \times \left[ \frac{(1+i)^n - 1}{i} \right] $$

🟢 **Exemplo da Prova (Item 4):** Entrada de 33% + 3 parcelas. O desconto à vista é calculado igualando o Valor Presente das parcelas ao Preço à Vista.

---

## 🏦 Unidade VIII: Amortização (SAC vs. PRICE)
O grande clássico! Como o saldo devedor é quitado?

### 🟢 1. SAC (Sistema de Amortização Constante)
*   **Amortização:** <span style="color: #1E90FF;">CONSTANTE</span> (divide o empréstimo pelo número de meses).
*   **Juros:** <span style="color: #DC143C;">DECRESCENTES</span> (incidem sobre o saldo devedor).
*   **Prestação:** <span style="color: #DC143C;">DECRESCENTE</span> (começa alta, termina baixa).
*   *Fórmula da Prestação:* $Prestação_t = Amortização + (SaldoDevedor_{t-1} \times i)$

### 🔴 2. PRICE (Sistema Francês)
*   **Prestação:** <span style="color: #1E90FF;">CONSTANTE</span> (a parcela não muda).
*   **Amortização:** <span style="color: #2E8B57;">CRESCENTE</span> (no início você paga quase só juros, no final, quase só amortização).
*   *Fórmula da Prestação:* $PMT = PV \times \frac{i(1+i)^n}{(1+i)^n - 1}$

🟡 **⚠️ ALERTA DA PROVA (Carência e Saldo Devedor):**
Se há **carência** (não paga nada), os juros não pagos são incorporados ao saldo devedor (Juros sobre Juros!). O Saldo Devedor no PRICE após a $k$-ésima parcela é o Valor Presente das parcelas que *faltam* pagar.

---

## ⏱️ Unidade IX: Hot Money e Capitalização Diária
**Conceito:** Taxa Nominal vs. Taxa Efetiva. Quando os juros são capitalizados mais de uma vez no período da taxa.

🔵 **Fórmula de Capitalização:**
$$ i_{efetiva} = \left(1 + \frac{i_{nominal}}{m}\right)^m - 1 $$
*(Onde $m$ é o número de capitalizações no período. Ex: Taxa mensal capitalizada diariamente -> $m \approx 30$).*

🟢 **Exemplo do Hot Money (Prova Item 3):**
Taxa nominal de 4% ao mês, capitalizada diariamente.
$i_{diário} = 4\% / 30 = 0,1333\%$
$i_{mensal\_efetiva} = (1 + 0,001333)^{30} - 1 = 4,07\%$
*Some-se a isso o IOF diário (0,0082%) que atua como um "custo" adicional diário.*
