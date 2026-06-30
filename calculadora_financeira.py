import numpy as np
import numpy_financial as npf

class CalculadoraFinanceira:
    """
    Classe didática para resolver problemas de Matemática Financeira
    baseados em cenários de provas (IR, SAC, PRICE, Hot Money).
    """

    @staticmethod
    def fluxo_de_caixa_com_ir(receita_liq, cv, cf, aliquota_ir):
        """
        🟡 ALERTA: O IR só incide sobre o Lucro Operacional!
        """
        margem_contribuicao = receita_liq - cv
        lucro_operacional = margem_contribuicao - cf
        
        # 🟢 Se tiver lucro, paga IR. Se tiver prejuízo, IR é 0.
        ir = max(0, lucro_operacional * aliquota_ir) 
        lucro_liquido = lucro_operacional - ir
        
        print(f"--- Demonstração de Resultados ---")
        print(f"🟢 Margem de Contribuição: R$ {margem_contribuicao:,.2f}")
        print(f"🔴 Custos Fixos: R$ {cf:,.2f}")
        print(f"🔵 Lucro Operacional: R$ {lucro_operacional:,.2f}")
        print(f"🔴 Imposto de Renda ({aliquota_ir*100}%): R$ {ir:,.2f}")
        print(f"🟢 Lucro Líquido (Fluxo de Caixa Real): R$ {lucro_liquido:,.2f}\n")
        return lucro_liquido

    @staticmethod
    def sistema_price(pv, taxa_mensal, n_meses, carencia=0):
        """
        Calcula a prestação constante do PRICE e o saldo devedor.
        🟡 ALERTA: Se houver carência, o saldo devedor aumenta (juros sobre juros).
        """
        # Aplica a carência (os juros correm e se acumulam ao Principal)
        pv_com_carencia = pv * ((1 + taxa_mensal) ** carencia)
        
        # Fórmula da Prestação Constante (PRICE)
        pmt = pv_com_carencia * (taxa_mensal * (1 + taxa_mensal)**n_meses) / (((1 + taxa_mensal)**n_meses) - 1)
        
        print(f"--- Sistema PRICE ---")
        print(f"🔵 Valor Financiado (após carência): R$ {pv_com_carencia:,.2f}")
        print(f"🔴 Prestação Constante: R$ {pmt:,.2f}")
        
        # Saldo devedor após k prestações (ex: 5ª prestação)
        k = 5
        # O saldo devedor é o Valor Presente das parcelas que FALTAM
        saldo_devedor = pmt * ((1 - (1 + taxa_mensal)**-(n_meses - k)) / taxa_mensal)
        print(f"🔴 Saldo Devedor após {k} prestações: R$ {saldo_devedor:,.2f}\n")
        return pmt

    @staticmethod
    def sistema_sac(pv, taxa_mensal, n_meses):
        """
        Calcula as parcelas do SAC (Amortização Constante).
        """
        amortizacao_constante = pv / n_meses
        print(f"--- Sistema SAC ---")
        print(f"🔵 Amortização Constante: R$ {amortizacao_constante:,.2f}")
        
        saldo = pv
        print("🔴 Evolução das 3 primeiras parcelas:")
        for i in range(1, 4):
            juros = saldo * taxa_mensal
            prestacao = amortizacao_constante + juros
            saldo -= amortizacao_constante
            print(f"  Mês {i}: Prestação R$ {prestacao:,.2f} (Juros: R$ {juros:,.2f} | Saldo: R$ {saldo:,.2f})")
        print()

    @staticmethod
    def taxa_efetiva_hot_money(taxa_nominal_pct, dias_no_mes=30, iof_diario_pct=0):
        """
        Converte taxa nominal mensal em efetiva, considerando capitalização diária e IOF.
        """
        i_nom = taxa_nominal_pct / 100
        iof = iof_diario_pct / 100
        
        # Taxa diária líquida (Juros + IOF)
        i_diaria = (i_nom / dias_no_mes) + iof 
        
        # Capitalização composta diária
        i_efetiva = ((1 + i_diaria) ** dias_no_mes) - 1
        
        print(f"--- Hot Money (Capitalização Diária) ---")
        print(f"🔵 Taxa Nominal Mensal: {taxa_nominal_pct}%")
        print(f"🔴 IOF Diário: {iof_diario_pct}%")
        print(f"🟢 Taxa Efetiva Mensal (com IOF): {i_efetiva*100:.4f}%\n")


# ==========================================
# 🚀 EXECUTANDO OS CENÁRIOS DA PROVA
# ==========================================
if __name__ == "__main__":
    calc = CalculadoraFinanceira()
    
    print("🔥 RESOLUÇÃO DIDÁTICA BASEADA NA PROVA 🔥\n")
    
    # CENÁRIO 1: Margem e IR (Item 1 da prova)
    # Receita 70k, CV 45k, CF 18k, IR 33%
    calc.fluxo_de_caixa_com_ir(receita_liq=70000, cv=45000, cf=18000, aliquota_ir=0.33)
    
    # CENÁRIO 2: PRICE com Carência (Itens 2g da prova)
    # Financiamento 12.000, 24 meses, taxa 33% a.a. (vamos usar 3% a.m. para o exemplo didático)
    # Carência de 6 meses.
    calc.sistema_price(pv=12000, taxa_mensal=0.03, n_meses=24, carencia=6)
    
    # CENÁRIO 3: SAC (Item 2f da prova)
    calc.sistema_sac(pv=12000, taxa_mensal=0.03, n_meses=24)
    
    # CENÁRIO 4: Hot Money (Item 3 da prova)
    # Taxa nominal 4% a.m., IOF 0,0082% ao dia
    calc.taxa_efetiva_hot_money(taxa_nominal_pct=4.0, iof_diario_pct=0.0082)
