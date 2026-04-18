import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt, Confirm
from hem_core.marketing import MarketingAuditor
from hem_core.growth import EquilibriumManager
from hem_core.production import ProductionAuditor

console = Console()

def show_banner():
    banner = """
    ⚖️  HANIF ECONOMICS & MARKETING (HEM)
    Meta-Mühendislik & Fıtrat Odaklı Denetim Sistemi
    ------------------------------------------------
    "Beşeriyetten Ademiyete Giden Yolda Bir Araç"
    """
    console.print(Panel(banner, style="bold cyan", expand=False))

def run_marketing_test():
    console.rule("[bold yellow]Pazarlama Etik Testi")
    auditor = MarketingAuditor()
    
    copy = Prompt.ask("Analiz edilecek pazarlama metnini girin")
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
        progress.add_task(description="Nöropazarlama kalıpları taranıyor...", total=None)
        time.sleep(1.5)
        
    result = auditor.analyze_copy(copy)
    
    table = Table(title="Analiz Sonuçları")
    table.add_column("Kategori", style="cyan")
    table.add_column("Bulgu", style="magenta")
    
    for cat, findings in result["findings"].items():
        table.add_row(cat, ", ".join(findings))
        
    console.print(table)
    
    status_style = "green" if result["status"] == "PASS" else "red"
    console.print(f"\n[bold {status_style}]Uyumluluk Skoru: {result['compliance_score']}%[/]")
    console.print(f"[{status_style}]Durum: {result['status']}[/]\n")

def run_growth_test():
    console.rule("[bold green]Denge ve Kanaat Analizi")
    manager = EquilibriumManager()
    
    profit = float(Prompt.ask("Yıllık Net Kâr (TL)"))
    costs = float(Prompt.ask("Yıllık Operasyonel Maliyetler (TL)"))
    employees = int(Prompt.ask("Toplam Çalışan Sayısı"))
    
    result = manager.calculate_satiety_point(profit, costs, employees)
    
    console.print(f"\n[bold]Hesaplanan Doyum Noktası:[/] {result['satiety_point']:,.2f} TL")
    
    if result["excess_profit"] > 0:
        console.print(f"[bold red]Fazla Kâr Tespit Edildi:[/] {result['excess_profit']:,.2f} TL")
        console.print("[yellow]Öneri: Bu miktar Ar-Ge, çalışan refahı veya ekosisteme geri döndürülmelidir.[/]")
    else:
        console.print("[bold green]Şirket büyüme eşiğinde, denge korunuyor.[/]")

def main():
    show_banner()
    
    while True:
        console.print("\n[bold]1.[/] Pazarlama Manipülasyon Testi")
        console.print("[bold]2.[/] Büyüme ve Kanaat Analizi")
        console.print("[bold]3.[/] Çıkış\n")
        
        choice = Prompt.ask("Yapmak istediğiniz işlemi seçin", choices=["1", "2", "3"])
        
        if choice == "1":
            run_marketing_test()
        elif choice == "2":
            run_growth_test()
        else:
            console.print("[italic]Darüsselam yolunda başarılar dileriz...[/]")
            break

if __name__ == "__main__":
    main()
