class ProductionAuditor:
    """
    Fıtrat Uyumlu Üretim (Sustainable Value Chain) denetçisi.
    Ürünlerin tamir edilebilirliğini ve ekolojik uyumunu analiz eder.
    """

    def calculate_repairability_score(self, factors):
        """
        factors: {
            "is_modular": bool,
            "standard_screws": bool,
            "spare_parts_available": bool,
            "documentation_open": bool,
            "no_glue": bool
        }
        """
        base_score = 0
        points_per_factor = 100 / len(factors)
        
        for factor, value in factors.items():
            if value:
                base_score += points_per_factor
                
        return {
            "score": base_score,
            "repairability_class": self._get_class(base_score),
            "is_hanif_compliant": base_score >= 80
        }

    def _get_class(self, score):
        if score >= 90: return "A (Excellence)"
        if score >= 75: return "B (Good)"
        if score >= 50: return "C (Fair)"
        return "F (Planned Obsolescence Risk)"

    def check_ekolojik_fitrat(self, metrics):
        """
        metrics: {
            "recycled_content_ratio": float (0-1),
            "biodegradable": bool,
            "carbon_neutral": bool
        }
        """
        score = 0
        if metrics["recycled_content_ratio"] > 0.5: score += 40
        if metrics["biodegradable"]: score += 30
        if metrics["carbon_neutral"]: score += 30
        
        return {
            "ecological_score": score,
            "status": "GREEN" if score >= 70 else "YELLOW" if score >= 40 else "RED"
        }
