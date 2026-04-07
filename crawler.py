import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_all_website_links(base_url, max_pages=50):
    # Sets are faster than lists for checking if an item exists
    visited_urls = set()
    urls_to_visit = [base_url]
    internal_links = set()
    
    # Extract the core domain so we don't accidentally crawl the entire internet
    domain_name = urlparse(base_url).netloc

    print(f"🕵️‍♂️ Starting crawler on: {base_url}")
    print("-" * 40)

    while urls_to_visit and len(visited_urls) < max_pages:
        # Grab the first URL in our queue
        current_url = urls_to_visit.pop(0)
        
        if current_url in visited_urls:
            continue
            
        print(f"Crawling: {current_url}")
        visited_urls.add(current_url)

        try:
            # Pretend to be a browser
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(current_url, headers=headers, timeout=5)
            
            # Skip if it's a PDF, image, or anything other than a standard webpage
            if "text/html" not in response.headers.get("Content-Type", ""):
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            # Find all <a> tags (hyperlinks)
            for a_tag in soup.find_all("a"):
                href = a_tag.attrs.get("href")
                
                if href == "" or href is None:
                    continue
                    
                # Fix relative links (e.g., turns "/pricing" into "https://site.com/pricing")
                href = urljoin(current_url, href)
                
                # Clean up the URL by stripping off # fragments (e.g., #section-1)
                parsed_href = urlparse(href)
                href = f"{parsed_href.scheme}://{parsed_href.netloc}{parsed_href.path}"
                
                # If it's a new link on the SAME domain, add it to our lists
                if domain_name in href and href not in internal_links and href not in visited_urls:
                    internal_links.add(href)
                    urls_to_visit.append(href)

        except requests.exceptions.RequestException as e:
            print(f"  [!] Failed to crawl {current_url}: {e}")
            
    return internal_links

# --- Execution Block ---
if __name__ == "__main__":
    # A safe, legal sandbox website specifically built for practicing web scraping
    target_website = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"
    
    # Limit to 20 pages for testing so you aren't waiting forever
    found_links = get_all_website_links(target_website, max_pages=20)
    
    print("\n" + "="*40)
    print(f"🎉 FOUND {len(found_links)} INTERNAL LINKS")
    print("="*40)
    
    output_file = "crawled_urls.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for link in sorted(found_links):
            print(link)
            f.write(link + "\n")
            
    print(f"\n✅ Saved to '{output_file}'. You can copy these directly into your urls.txt for Digest.py!")