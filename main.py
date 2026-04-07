import requests
from bs4 import BeautifulSoup
from google import genai
import os

def extract_text(url):
    print(f"Fetching URL: {url}...")
    try:
        # Pretend to be a standard browser to avoid basic bot-blockers
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text only from paragraph tags
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {e}"

def summarize_text(text):
    print("Generating digest...")
    try:
        client = genai.Client()
        
        prompt = f"""
        Role: You are an expert editor and summarizer. 
        
        Task: Condense the provided content into a clear, concise summary that captures the key points.
        
        Strict Scope Rules:
        * If the content is wrapped in <selection> tags, ONLY summarize the text inside those tags. Ignore everything else.
        * If there are no <selection> tags, summarize the entire provided text.
        * If the content is already highly concise (under 3 sentences), reply ONLY with: "No summary needed: Content is already concise."
        
        Guidelines:
        * Focus strictly on the most important ideas, decisions, or actionable takeaways.
        * Remove all examples, filler, and repetitive details.
        * Keep the summary significantly shorter than the original text.
        * Preserve the original meaning and intent perfectly.
        * Use simple, clear language. 
        * Maintain helpful formatting (use bullet points for multiple distinct ideas).
        
        Output Constraint: Output ONLY the summary. Do not include introductory phrases like "Here is the summary" or "In this text."
        
        Text to summarize:
        <selection>
        {text[:15000]}
        </selection>
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating summary: {e}"

# --- Execution Block ---
if __name__ == "__main__":
    input_file = "urls.txt"
    output_file = "my_digests.md"
    
    if not os.path.exists(input_file):
        print(f"Error: Please create a '{input_file}' file in this folder and add some URLs.")
    else:
        with open(output_file, "w", encoding="utf-8") as f:
            # Main Notion Page Header
            f.write("# 🧠 My Daily Digests\n\n")
            
            with open(input_file, "r") as urls:
                for line in urls:
                    url = line.strip()
                    if not url: 
                        continue
                        
                    print(f"\n--- Processing: {url} ---")
                    raw_content = extract_text(url)
                    
                    if "Error" not in raw_content and len(raw_content) > 100:
                        digest = summarize_text(raw_content)
                        
                        # Clean Notion Formatting
                        f.write(f"## 📑 Digest: {url.split('//')[-1]}\n") # Strips the https:// for a cleaner title
                        f.write(f"[Read Original Source]({url})\n\n")
                        f.write(f"{digest}\n\n")
                        f.write("---\n\n") # Notion Divider
                        
                        print("✅ Success! Saved to my_digests.md")
                    else:
                        print("❌ Extraction failed or text was too short.")
                        f.write(f"## 📑 Failed Digest: {url}\n\n*Failed to extract or summarize.*\n\n---\n\n")
        
        print(f"\n🎉 All done! Open '{output_file}', copy everything, and paste it directly into a blank Notion page.")