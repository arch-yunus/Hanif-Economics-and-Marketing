class EquilibriumManager:
    """
    Denge (Equilibrium) Optimizasyonu ve Kanaat denetçisi.
    Şirketlerin büyüme-dağıtım dengesini analiz eder.
    """

    def __init__(self, target_redistribution_ratio=0.3):
        self.target_redistribution_ratio = target_redistribution_ratio

    def calculate_satiety_point(self, current_profit, operational_costs, employee_count):
        """
        'Doyum Noktası' (Satiety Point) hesaplar. 
        Bu noktadan sonraki kârın öncelikli olarak dağıtılması önerilir.
        """
        # Basit bir model: Operasyonel maliyetlerin 3 katı + çalışan refah payı
        survival_threshold = operational_costs * 1.5
        growth_buffer = operational_costs * 1.5
        refah_payi = employee_count * 1000 # Örnek sabit değer
        
        satiety_point = survival_threshold + growth_buffer + refah_payi
        excess_profit = max(0, current_profit - satiety_point)
        
        return {
            "satiety_point": satiety_point,
            "excess_profit": excess_profit,
            "recommendation": "REDISTRIBUTE" if excess_profit > 0 else "NUTRISH"
        }

    def evaluate_redistribution(self, total_profit, redistributed_amount):
        """
        Kârın ne kadarının ekosisteme (Ar-Ge, çalışan, doğa) geri döndürüldüğünü analiz eder.
        """
        actual_ratio = redistributed_amount / total_profit if total_profit > 0 else 0
        
        return {
            "actual_ratio": actual_ratio,
            "target_ratio": self.target_redistribution_ratio,
            "is_hanif_compliant": actual_ratio >= self.target_redistribution_ratio,
            "gap": max(0, self.target_redistribution_ratio - actual_ratio)
        }
