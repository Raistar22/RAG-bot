import os
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.angelone.in/support"
SAVE_FOLDER = "data/webpages"

def scrape_and_save():
    print("[*] Starting scraping process...")
    os.makedirs(SAVE_FOLDER, exist_ok=True)

    try:
        # Use custom headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

        print(f"[*] Accessing support page: {BASE_URL}")
        response = requests.get(BASE_URL, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract main content
        title = soup.title.text.strip() if soup.title else "Angel One Support"
        content_sections = []
        
        # Get Quick Links section
        quick_links = soup.find_all(class_="quick-links")
        for section in quick_links:
            links = section.find_all("a")
            for link in links:
                text = link.get_text(strip=True)
                if text and "Please Wait" not in text:
                    content_sections.append(f"Quick Link: {text}")
        
        # Get all paragraphs with meaningful content
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") 
                     if p.get_text(strip=True) and "Please Wait" not in p.get_text()]
        content_sections.extend(paragraphs)
        
        # Get all headings
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings = [h.get_text(strip=True) for h in soup.find_all(tag) 
                       if h.get_text(strip=True) and "Please Wait" not in h.get_text()]
            content_sections.extend(headings)

        # Get support categories and links
        categories = soup.find_all(class_="support-category")
        for category in categories:
            cat_title = category.find(["h2", "h3", "h4"])
            if cat_title:
                content_sections.append(f"\nCategory: {cat_title.get_text(strip=True)}")
                items = category.find_all("a")
                for item in items:
                    text = item.get_text(strip=True)
                    if text and "Please Wait" not in text:
                        content_sections.append(f"- {text}")

        # Get any additional useful content
        for div in soup.find_all("div", class_=["card-content", "content-section"]):
            text = div.get_text(strip=True)
            if text and "Please Wait" not in text:
                content_sections.append(text)

        # Combine all content
        content = f"{title}\n\n" + "\n\n".join(filter(None, content_sections))

        # Save main page content
        filename = os.path.join(SAVE_FOLDER, "support_main.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Saved main support page: {filename}")

    except Exception as e:
        print(f"[!] Failed to scrape support page: {e}")

if __name__ == "__main__":
    scrape_and_save()