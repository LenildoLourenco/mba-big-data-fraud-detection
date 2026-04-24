## 🏗️ Arquitetura do Sistema

A solução foi estruturada em duas camadas principais:

### 1. Backend: Processamento Spark (Python)
- *Tecnologia:* Apache Spark (PySpark).
- *Funcionalidade:* Simulação de processamento de volumes massivos de dados. O motor gera registros sintéticos em memória e aplica regras de negócio para detecção de anomalias (score de fraude).
- *Saída:* Geração de resultados estruturados em JSON para consumo da camada de visualização.

### 2. Frontend: Dashboard Analítico (Angular 21)
- *Tecnologia:* Angular 21 com arquitetura baseada em Signals.
- *Funcionalidade:* Interface de alta performance que consome os dados processados pelo Spark, exibindo métricas, alertas de risco e tabelas de transações suspeitas.
- *Diferenciais:* Foco em Clean Code, performance de renderização e separação clara de responsabilidades.

## 🚀 Como Executar o Projeto

### Backend (Spark)
1. Certifique-se de ter o Python e o PySpark instalados.
2. Navegue até a pasta backend:
   ```bash
   python app_spark.py

### Frontend (Angular)
1. Navegue até a pasta frontend:
   npm install
   ng serve
2. Acesse http://localhost:4200 no seu navegador. 

🛠️ Tecnologias Utilizadas
​Linguagens: Python, TypeScript.
​Processamento: Apache Spark.
​Framework Web: Angular 21.
​DevOps: CI/CD ready, Git para versionamento.