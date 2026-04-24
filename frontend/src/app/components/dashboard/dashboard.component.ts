import { Component, OnInit, ChangeDetectorRef, ViewChild, ElementRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Chart, registerables } from 'chart.js';

// Registra todos os componentes do Chart.js (necessário nas versões novas)
Chart.register(...registerables);

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent implements OnInit {
  // Referência direta ao elemento <canvas> do HTML
  @ViewChild('graficoCanvas') graficoCanvas!: ElementRef<HTMLCanvasElement>;

  fraudes: any[] = [];
  totalValor: number = 0;
  chart: any;

  // Variáveis de Paginação
  paginaAtual: number = 1;
  itensPorPagina: number = 10;

  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef
  ) { }

  ngOnInit() {
    this.carregarDados();
  }

  // Getters para facilitar o HTML
  get totalPaginas(): number {
    return Math.ceil(this.fraudes.length / this.itensPorPagina);
  }

  get dadosPaginados(): any[] {
    const inicio = (this.paginaAtual - 1) * this.itensPorPagina;
    const fim = inicio + this.itensPorPagina;
    return this.fraudes.slice(inicio, fim);
  }

  mudarPagina(proxima: boolean) {
    if (proxima && this.paginaAtual < this.totalPaginas) {
      this.paginaAtual++;
    } else if (!proxima && this.paginaAtual > 1) {
      this.paginaAtual--;
    }
  }

  carregarDados() {
    // Busca o JSON da pasta public (mapeada na raiz '/')
    this.http.get('data_results.json').subscribe({
      next: (data: any) => {
        console.log('Dados carregados com sucesso:', data);
        this.fraudes = data;

        // Calcula o valor total das fraudes para o KPI Card
        this.totalValor = this.fraudes.reduce((acc, curr) => acc + (curr.valor || 0), 0);

        // Avisa o Angular para atualizar o HTML (necessário se usar OnPush ou SSR)
        this.cdr.detectChanges();

        // Aguarda o Angular renderizar o Canvas antes de inicializar o gráfico
        setTimeout(() => this.createChart(), 150);
      },
      error: (err) => {
        console.error('Erro ao carregar o arquivo JSON:', err);
      }
    });
  }

  createChart() {
    // Verifica se a referência ao canvas existe
    if (!this.graficoCanvas) {
      console.warn('Canvas ainda não está pronto no DOM.');
      return;
    }

    const context = this.graficoCanvas.nativeElement.getContext('2d');

    if (!context) {
      console.error("Não foi possível adquirir o contexto 2D do canvas.");
      return;
    }

    // Se já houver um gráfico (ex: após um refresh de dados), destrói o anterior
    if (this.chart) {
      this.chart.destroy();
    }

    // Configuração do Gráfico
    this.chart = new Chart(context, {
      type: 'bar',
      data: {
        // Pega os 10 primeiros IDs para não poluir o gráfico
        labels: this.fraudes.slice(0, 10).map(i => "ID " + (i.id_transacao || i.id)),
        datasets: [{
          label: 'Valor da Fraude (R$)',
          data: this.fraudes.slice(0, 10).map(i => i.valor),
          backgroundColor: '#e74c3c', 
          borderColor: '#c0392b',
          borderWidth: 1,
          borderRadius: 5
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
            position: 'top'
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: (value) => 'R$ ' + value
            }
          }
        }
      }
    });
  }
}
