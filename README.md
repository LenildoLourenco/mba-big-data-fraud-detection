# 📊 Sistema de Detecção de Fraudes com Big Data

Este projeto implementa um sistema de detecção de fraudes utilizando Apache Spark para processamento de dados e Angular para visualização em uma interface web interativa.

---

## 🚀 Objetivo

Simular um cenário de análise de fraude em transações financeiras utilizando conceitos e ferramentas de Big Data.

---

## 🧠 Características de Big Data atendidas

- **Volume**: Processamento de 1 milhão de registros
- **Variedade**: Dados com múltiplos atributos (valor, país, dispositivo, horário, tentativas)
- **Velocidade (conceitual)**: Arquitetura preparada para evolução com processamento em tempo real (streaming)

---

## ⚙️ Arquitetura
[Spark ETL] → [API FastAPI] → [Frontend Angular]

---

## 🔄 Pipeline de Dados

1. Geração de dados simulados com grande volume
2. Enriquecimento com múltiplas variáveis (variedade)
3. Aplicação de regras de detecção de fraude
4. Persistência distribuída em arquivos JSON
5. Exposição dos dados via API REST
6. Consumo dos dados pelo frontend Angular

---

## 🔍 Regras de Fraude

O sistema identifica transações suspeitas com base em critérios como:

- Alto valor financeiro
- Transações fora do país de origem
- Múltiplas tentativas
- Horários incomuns (ex: madrugada)

Classificações:
- `ALTA_SUSPEITA`
- `MEDIA_SUSPEITA`
- `NORMAL`

---

## 🖥️ Tecnologias Utilizadas

- Apache Spark (PySpark)
- FastAPI
- Angular
- Chart.js
- Python

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd projeto-mba-spark
2. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate
3. Instalar dependências
python3 -m pip install -r requirements.txt
4. Executar o processamento com Spark
cd backend
python3 app_spark.py
Isso irá gerar os dados em:
backend/output/fraudes/
5. Subir a API
uvicorn api:app --reload
Acesse:
http://localhost:8000/fraudes
http://localhost:8000/fraudes/top
6. Executar o Frontend (Angular)
cd frontend
npm install
ng serve
Acesse:
http://localhost:4200
☁️ Escalabilidade
O sistema foi projetado para ser escalável e pode ser executado em ambientes distribuídos como:
AWS (Amazon Web Services)
Google Cloud Platform
Microsoft Azure
📌 Considerações
O projeto utiliza dados simulados, mas foi estruturado para suportar grandes volumes em ambientes reais
O Apache Spark permite execução distribuída e paralela
A arquitetura segue um modelo moderno de separação entre processamento, API e frontend