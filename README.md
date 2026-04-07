Here is exactly how to create that file on your Windows machine in under 30 seconds.

### Step 1: Create the File

Since you are already in your terminal (inside the `digest-py` folder), type this command and press Enter:

```powershell
notepad README.md
```
*Note: A popup will appear asking if you want to create a new file. Click **Yes**.*

### Step 2: Paste the Content

Copy the text block below, paste it into the empty Notepad window that just opened, and hit **Ctrl + S** to save it. You can then close Notepad.

```markdown
# 🧠 Digest.py

Digest.py is a lightweight Python CLI tool that cures tab fatigue. It takes a messy list of article URLs, extracts the core text, and uses the Google Gemini API to generate clean, concise summaries. The output is perfectly formatted in Markdown, ready to be copied and pasted straight into Notion.

## ✨ Features
* **Automated Web Scraping:** Bypasses ads, menus, and footers to extract only the main paragraph text of an article.
* **Smart Summarization:** Powered by the `gemini-2.5-flash` model using a strict prompt to ensure summaries are fluff-free and highly actionable.
* **Batch Processing:** Reads multiple URLs from a simple text file and processes them sequentially.
* **Notion-Ready Output:** Generates a `my_digests.md` file styled specifically for Notion's native formatting (headers, blockquotes, and bulleted lists).

## 🛠️ Prerequisites
* Python 3.x installed on your Windows machine.
* A free Google Gemini API Key (get one from [Google AI Studio](https://aistudio.google.com/)).

## 🚀 Windows Setup Guide

**1. Clone or create the project directory:**
```powershell
mkdir digest-py
cd digest-py
```

**2. Create and activate a virtual environment:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**3. Install the required dependencies:**
```powershell
pip install requests beautifulsoup4 google-genai
```

**4. Set your API Key as an environment variable:**
*If using PowerShell (default in VS Code/Windows 11):*
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```
*If using classic Command Prompt (cmd):*
```cmd
set GEMINI_API_KEY=your_api_key_here
```

## 📖 How to Use

1. **Add your links:** Create a file named `urls.txt` in the root directory. Paste the URLs you want to summarize, one per line. No blank lines at the bottom.
    ```text
    [https://basecamp.com/shapeup/0.3-chapter-01](https://basecamp.com/shapeup/0.3-chapter-01)
    [https://paulgraham.com/ds.html](https://paulgraham.com/ds.html)
    ```
2. **Run the script:**
3. ```powershell
    python main.py
    ```
4. **Export to Notion:** Once the script finishes, open the newly generated `my_digests.md` file. Select all (Ctrl+A), Copy (Ctrl+C), and paste directly into a blank Notion page to see it instantly format.
## 📝 The AI Prompt
This project uses a highly constrained system prompt wrapped in `<selection>` tags to ensure the AI strictly summarizes the extracted article and ignores hallucinations, filler text, or conversational intros. 
```
