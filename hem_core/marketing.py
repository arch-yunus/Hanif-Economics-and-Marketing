import re

class MarketingAuditor:
    """
    Hanif Pazarlama (Anti-Manipulation Marketing) denetçisi.
    Pazarlama metinlerini ve stratejilerini ahlaki ve fıtri sınırlara göre analiz eder.
    """
    
    MANIPULATIVE_PATTERNS = {
        "FOMO": [
            r"son \d+ ürün", r"sadece bugün", r"fırsatı kaçırmayın", 
            r"acele edin", r"zaman daralıyor", r"başka şansınız yok"
        ],
        "INFERIORITY": [
            r"yetersiz misiniz", r"herkesin var", r"geride kalmayın",
            r"statü kazanın", r"dikkat çekin", r"siz de sahip olun"
        ],
        "DECEPTIVE": [
            r"bedava", r"kesin sonuç", r"sıfır risk", 
            r"mucizevi", r"asla bozulmaz"
        ]
    }

    def __init__(self):
        self.rules = []

    def analyze_copy(self, text):
        """
        Pazarlama metnini manipülatif kalıplar açısından tarar.
        """
        findings = {}
        score = 100
        
        for category, patterns in self.MANIPULATIVE_PATTERNS.items():
            matches = []
            for pattern in patterns:
                found = re.findall(pattern, text, re.IGNORECASE)
                if found:
                    matches.extend(found)
                    score -= 10 * len(found)
            
            if matches:
                findings[category] = list(set(matches))
        
        return {
            "compliance_score": max(0, score),
            "findings": findings,
            "status": "PASS" if score >= 70 else "FAIL"
        }

    def check_irade_testi(self, answers):
        """
        README'deki İrade Testi sorularını değerlendirir.
        """
        # answers: {question_id: bool}
        passed_count = sum(1 for v in answers.values() if v is True)
        total_count = len(answers)
        
        return {
            "score": (passed_count / total_count) * 100,
            "status": "HANIF_COMPLIANT" if passed_count == total_count else "NEEDS_OPTIMIZATION"
        }
