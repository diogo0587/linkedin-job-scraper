#!/usr/bin/env python3
"""
LinkedIn Job Scraper
Busca vagas no LinkedIn e salva em arquivo CSV
Autor: diogo0587
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime
import sys

class LinkedInJobScraper:
    def __init__(self, job_title="Python Developer", location="Brasil"):
        self.job_title = job_title
        self.location = location
        self.base_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
        self.jobs = []
        
    def build_url(self, start=0):
        """Constrói URL para busca de vagas"""
        params = {
            'keywords': self.job_title,
            'location': self.location,
            'start': start
        }
        
        param_string = '&'.join([f"{k}={v.replace(' ', '%20')}" for k, v in params.items()])
        return f"{self.base_url}?{param_string}"
    
    def scrape_page(self, start=0):
        """Faz scraping de uma página de resultados"""
        url = self.build_url(start)
        
        try:
            print(f"Buscando vagas... (página {start//25 + 1})")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            job_cards = soup.find_all('li')
            
            if not job_cards:
                return False
            
            for card in job_cards:
                try:
                    # Extrair título
                    title_elem = card.find('h3', class_='base-search-card__title')
                    title = title_elem.text.strip() if title_elem else 'N/A'
                    
                    # Extrair empresa
                    company_elem = card.find('h4', class_='base-search-card__subtitle')
                    company = company_elem.text.strip() if company_elem else 'N/A'
                    
                    # Extrair localização
                    location_elem = card.find('span', class_='job-search-card__location')
                    location = location_elem.text.strip() if location_elem else 'N/A'
                    
                    # Extrair URL
                    link_elem = card.find('a', class_='base-card__full-link')
                    job_url = link_elem['href'] if link_elem and 'href' in link_elem.attrs else 'N/A'
                    
                    # Extrair data de postagem
                    date_elem = card.find('time')
                    posted_date = date_elem.text.strip() if date_elem else 'N/A'
                    
                    job_data = {
                        'titulo': title,
                        'empresa': company,
                        'localizacao': location,
                        'url': job_url,
                        'data_postagem': posted_date,
                        'data_scraping': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    
                    self.jobs.append(job_data)
                    
                except Exception as e:
                    print(f"Erro ao processar vaga: {e}")
                    continue
            
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return False
    
    def scrape_jobs(self, max_pages=5):
        """Busca vagas em múltiplas páginas"""
        print(f"\n🔍 Buscando vagas de '{self.job_title}' em '{self.location}'...\n")
        
        for page in range(max_pages):
            start = page * 25
            
            if not self.scrape_page(start):
                print(f"Nenhuma vaga encontrada na página {page + 1}")
                break
            
            print(f"✓ Página {page + 1} concluída - {len(self.jobs)} vagas encontradas")
            
            # Delay entre requisições para evitar bloqueio
            time.sleep(2)
        
        print(f"\n✅ Total de {len(self.jobs)} vagas coletadas!\n")
        return self.jobs
    
    def save_to_csv(self, filename='linkedin_jobs.csv'):
        """Salva vagas em arquivo CSV"""
        if not self.jobs:
            print("Nenhuma vaga para salvar.")
            return
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['titulo', 'empresa', 'localizacao', 'url', 'data_postagem', 'data_scraping']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(self.jobs)
            
            print(f"💾 Dados salvos em '{filename}'")
            
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")

def main():
    """Função principal"""
    print("=" * 60)
    print("LinkedIn Job Scraper".center(60))
    print("=" * 60)
    
    # Configurações padrão
    job_title = "Python Developer"
    location = "Brasil"
    max_pages = 5
    
    # Aceitar argumentos da linha de comando
    if len(sys.argv) > 1:
        job_title = sys.argv[1]
    if len(sys.argv) > 2:
        location = sys.argv[2]
    if len(sys.argv) > 3:
        max_pages = int(sys.argv[3])
    
    # Criar scraper e executar
    scraper = LinkedInJobScraper(job_title, location)
    scraper.scrape_jobs(max_pages)
    scraper.save_to_csv()
    
    print("\n" + "=" * 60)
    print("Scraping concluído!".center(60))
    print("=" * 60)

if __name__ == "__main__":
    main()