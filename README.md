# linkedin-job-scraper
Scraper automatizado para buscar vagas no LinkedIn usando Python
# linkedin-job-scraper2

🔍 **Scraper automatizado para buscar vagas no LinkedIn**

## 📋 Descrição

Scraper automatizado para buscar vagas no LinkedIn usando Python

Este projeto utiliza Python para fazer web scraping de vagas públicas no LinkedIn, extraindo informações como:
- Título da vaga
- Nome da empresa
- Localização
- URL da vaga
- Data de postagem

## 🚀 Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/diogo0587/linkedin-job-scraper2.git
cd linkedin-job-scraper2
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute o scraper

**Uso básico (usa configurações padrão):**
```bash
python linkedin_scraper.py
```

**Personalizar busca:**
```bash
python linkedin_scraper.py "Python Developer" "São Paulo" 10
```

Parâmetros:
- **Argumento 1**: Título da vaga (ex: "Python Developer")
- **Argumento 2**: Localização (ex: "São Paulo")
- **Argumento 3**: Número de páginas para buscar (cada página tem ~25 vagas)

### 4. Verifique os resultados

Os dados serão salvos em `linkedin_jobs.csv` no formato:

| titulo | empresa | localizacao | url | data_postagem | data_scraping |
|--------|---------|-------------|-----|---------------|---------------|
| Desenvolvedor Python | Empresa XYZ | São Paulo, SP | https://... | 1 dia atrás | 2024-11-21 18:45:00 |

## 🛠️ Tecnologias

- **Python 3.7+**
- **requests** - Para fazer requisições HTTP
- **BeautifulSoup4** - Para parsing de HTML
- **csv** - Para exportar dados

## ⚙️ Funcionalidades

- ✅ Busca vagas públicas no LinkedIn (não requer autenticação)
- ✅ Extração de múltiplas páginas de resultados
- ✅ Delay entre requisições para evitar bloqueio
- ✅ Exportação para CSV
- ✅ Tratamento de erros
- ✅ Configuração via linha de comando

## 📊 Exemplo de saída

```
============================================================
                  LinkedIn Job Scraper
============================================================

🔍 Buscando vagas de 'Python Developer' em 'Brasil'...

Buscando vagas... (página 1)
✓ Página 1 concluída - 25 vagas encontradas
Buscando vagas... (página 2)
✓ Página 2 concluída - 50 vagas encontradas
...

✅ Total de 125 vagas coletadas!

💾 Dados salvos em 'linkedin_jobs.csv'

============================================================
                 Scraping concluído!
============================================================
```

## ⚠️ Avisos Importantes

- Este scraper utiliza **apenas dados públicos** disponíveis no LinkedIn
- Respeite os Termos de Serviço do LinkedIn
- Use com moderação para evitar bloqueios de IP
- O código inclui delays entre requisições
- Recomendado para uso educacional e pessoal

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto é open source e está disponível sob a [MIT License](LICENSE).

## 👨‍💻 Autor

**diogo0587**
- GitHub: [@diogo0587](https://github.com/diogo0587)

## 🔗 Links Úteis

- [Documentação BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Documentação Requests](https://docs.python-requests.org/)
- [LinkedIn Jobs](https://www.linkedin.com/jobs/)

---

⭐ Se este projeto foi útil, considere dar uma estrela!