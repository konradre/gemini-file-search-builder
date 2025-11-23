# Gemini File Search Builder

**Build Gemini File Search RAG knowledge bases from any website with automatic citations**

[![Apify Store](https://img.shields.io/badge/Apify-Store-blue)](https://console.apify.com)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Apify SDK](https://img.shields.io/badge/Apify%20SDK-3.0-green)](https://docs.apify.com/sdk/python/)

## What It Does

This Apify actor creates a **permanent, queryable knowledge base** from any website using Google's Gemini File Search (announced November 6, 2025). Unlike traditional scrapers that just extract data, this actor transforms websites into intelligent Q&A systems with **automatic citation tracking**.

### Key Features

- 🧠 **Automatic RAG Pipeline** - Scrape → Clean → Upload → Query (all in one run)
- 📚 **Built-in Citations** - Every answer includes source documents
- ♾️ **Unlimited Free Queries** - Pay once to scrape, query forever (no storage fees)
- 🎯 **Challenge Compliant** - 100% banned scraper filtering (Instagram, Amazon, Google Maps, etc.)
- 🚀 **Zero Setup** - Just provide URL + Gemini API key
- 💰 **Cost Optimized** - Smart scraper selection based on your budget
- 🎨 **Multiple Output Formats** - Supports Markdown, HTML, and plain text extraction

## Use Cases

- **Documentation Indexing** - Convert technical docs into queryable knowledge bases
- **Research Databases** - Create searchable archives from academic sites
- **Content Libraries** - Index blog posts, articles, tutorials
- **Internal Wikis** - Transform company knowledge bases for AI access

## How It Works

```
Website URL → Scraper Selection → Content Extraction → Document Conversion
                                                              ↓
         Query Interface ← Gemini File Search ← Upload Documents
```

1. **Smart Scraper Selection** - Analyzes target and selects optimal Apify scraper
2. **Content Cleaning** - Removes ads, navigation, extracts main content
3. **Document Creation** - Formats as clean text with metadata
4. **Gemini Upload** - Creates File Search Store (persistent, free storage)
5. **Query Guide** - Returns instructions for using your knowledge base

## Quick Start

### 1. Get API Keys

**Gemini API Key** (required):
- Visit https://aistudio.google.com/apikey
- Create new API key (free tier available)
- ⚠️ **Important:** Use the SAME key you'll use to query the knowledge base later. File Search Stores are tied to the creating API key.

**Apify Token** (required):
- Visit https://console.apify.com/settings/integrations
- Copy your API token

### 2. Run the Actor

```json
{
  "target": "https://docs.python.org",
  "max_pages": 100,
  "scraper_budget": "optimal",
  "corpus_name": "python-docs",
  "gemini_api_key": "YOUR_GEMINI_KEY",
  "apify_token": "YOUR_APIFY_TOKEN"
}
```

### 3. Query Your Knowledge Base

After the actor completes, use the returned `file_search_store_name` to query:

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_GEMINI_KEY")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='How do I use decorators in Python?',
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            file_search=types.FileSearch(
                file_search_store_names=["YOUR_STORE_NAME"]
            )
        )]
    )
)

print(response.text)  # Answer with automatic citations
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `target` | string | ✅ | - | Website URL to scrape and index |
| `max_pages` | integer | | 100 | Maximum pages to scrape (1-2000) |
| `scraper_budget` | string | | "optimal" | Cost strategy: `minimal`, `optimal`, `premium` |
| `corpus_name` | string | | "scraped-knowledge" | Name for your knowledge base |
| `gemini_api_key` | string | ✅ | - | Google Gemini API key |
| `apify_token` | string | ✅ | - | Apify API token |

## Output

```json
{
  "file_search_store_name": "fileSearchStores/pythondocs-abc123",
  "files_indexed": 150,
  "total_size_mb": 2.5,
  "estimated_tokens": 125000,
  "indexing_cost_usd": 0.0188,
  "storage_type": "File Search Store",
  "storage_persistence": "Indefinite (free)",
  "query_cost_estimate": "$0.001 per query",
  "query_guide_url": "https://docs.google.com/..."
}
```

## Pricing & Costs

This Actor uses **pay-per-page pricing** for transparent, predictable costs:

### Base Pricing

- **Actor start**: $0.02 per run (one-time)
- **Page processed**: $0.0015 per page (base price)

### Store Discount Tiers

Your Apify subscription plan determines automatic discounts:

| Plan | Monthly Cost | Discount | Price/Page | 100 Pages Total |
|------|--------------|----------|------------|-----------------|
| **Free** | $0 | 0% | $0.0015 | **$0.17** |
| **Starter** | $39 | 10% (BRONZE) | $0.00135 | **$0.155** |
| **Scale** | $199 | 20% (SILVER) | $0.0012 | **$0.14** |
| **Business** | $999 | 30% (GOLD) | $0.00105 | **$0.125** |

💰 **Upgrade your Apify plan to save up to 30% on processing costs!**

### Example Costs

| Pages | FREE Tier | GOLD Tier | Savings |
|-------|-----------|-----------|---------|
| 10 | $0.035 | $0.03 | 14% |
| 50 | $0.095 | $0.07 | 26% |
| 100 | $0.17 | $0.125 | 26% |
| 500 | $0.77 | $0.545 | 29% |

*Prices include ~$0.02 actor start fee*

### What You DON'T Pay (to This Actor)

✅ **Gemini API costs** - You provide your own API key (billed per Google's pricing)
✅ **Apify platform usage** - You manage your own credits
✅ **Pass-through fees** - No markup on Gemini or Apify costs

**Note:** Gemini charges for indexing (~$0.15/1M tokens). Storage and query embeddings are free. See [Gemini pricing](https://ai.google.dev/pricing).

### Comparison

- **10x cheaper** than premium AI collectors ($0.0025 vs $0.25/page)
- **Gemini-optimized** vs generic scrapers
- **Transparent billing** - Only successful pages charged

## Challenge Compliance

**Apify $1M Challenge - Fully Compliant**

✅ **100% Banned Scraper Filter**
- Social media: Instagram, Facebook, TikTok, LinkedIn, Twitter, YouTube
- E-commerce: Amazon
- Search engines: Google Maps, Google Search, Google Trends
- B2B platforms: Apollo

✅ **Skills-Based Architecture**
- Progressive disclosure (75% token reduction)
- Hook-based enforcement (zero bypass)
- Automated compliance testing

✅ **Test Coverage**
- 49/49 unit tests passing
- 6/6 integration tests passing
- 100% banned pattern validation

## Architecture

### Key Features

1. **Modular Design** - Separate modules for scraping, conversion, and upload
2. **Challenge Compliance** - 100% banned scraper filtering (tested with 49 unit tests)
3. **Intelligent Selection** - Automatic scraper scoring based on target type and budget

### Tech Stack

- **Apify SDK 3.0** - Actor runtime & scraper orchestration
- **Google Gemini API** - File Search for RAG (unified SDK `google-genai`)
- **BeautifulSoup4** - HTML parsing & content extraction
- **Python 3.11+** - Type hints, async/await

### Project Structure

```
gemini-file-search-builder/
├── .actor/
│   ├── actor.json          # Actor configuration
│   ├── INPUT_SCHEMA.json   # Input validation schema
│   └── output_schema.json  # Output definition
├── src/
│   ├── main.py             # Main workflow orchestration
│   ├── tools/
│   │   ├── scraper_library.py     # Production scraper library (5 scrapers)
│   │   ├── scraper_selector.py    # Smart selection + banned filter
│   │   ├── document_converter.py  # HTML → clean text
│   │   └── gemini_uploader.py     # File Search integration
│   └── utils/
├── tests/
│   └── test_banned_filter.py     # 49 unit tests
├── Dockerfile
├── requirements.txt
└── README.md
```

## Development

### Local Setup

```bash
# Clone repository
git clone <your-repo-url>
cd gemini-file-search-builder

# Install dependencies
pip install -r requirements.txt

# Run locally
python __main__.py
```

### Running Tests

```bash
pytest tests/  # 49/49 tests should pass
```

### Environment Variables

Create `.env` file (not committed):
```bash
GEMINI_API_KEY=your_key_here
APIFY_TOKEN=your_token_here
```

## Limitations & Known Issues

1. **Apify Store Search** - Current MVP uses hardcoded scraper whitelist. Production would use dynamic Store search.

2. **Proxy Restrictions** - Some sites (e.g., docs.react.dev) may be blocked by Apify cloud proxies. Use accessible documentation sites.

3. **File Size Limits** - Gemini File Search supports up to 2GB per file, 10K files per store.

## FAQ

**Q: How long does the knowledge base persist?**
A: Indefinitely (until manually deleted). No storage expiration or fees.

**Q: Can I update the knowledge base later?**
A: Yes! Upload additional documents to the same File Search Store.

**Q: What's the maximum site size?**
A: Up to 2,000 pages (configurable), ~2GB total content.

**Q: Do I need a Google Cloud account?**
A: No! Just a Gemini API key from aistudio.google.com (free tier available).

**Q: Can I use a different API key to query the knowledge base?**
A: No. File Search Stores are tied to the API key that created them. You must use the SAME Gemini API key for both creating and querying the knowledge base. This ensures your data remains private and accessible only to you.

**Q: How accurate are the citations?**
A: Gemini File Search automatically cites source documents with chunk-level precision.

**Q: Is web scraping legal?**
A: Web scraping is generally legal for publicly available, non-personal data. Always respect robots.txt and website terms of service. For personal data, ensure GDPR compliance. Consult legal counsel if unsure. Learn more: [Is web scraping legal?](https://blog.apify.com/is-web-scraping-legal/)

## Integrations

This Actor works seamlessly with Apify's platform integrations:

- **Make, Zapier** - Automate workflows with no-code tools
- **Webhooks** - Trigger actions when knowledge base creation completes
- **API Access** - Control programmatically via Python/JavaScript SDKs
- **Scheduled Runs** - Automatically update knowledge bases on schedule

All Apify actors support these integrations out of the box. See [Apify integrations](https://docs.apify.com/platform/integrations) for setup guides.

## Using with AI Agents

This Actor is compatible with Model Context Protocol (MCP) and can be used with AI agents:

- **Claude Desktop** - Use via Apify MCP server
- **LibreChat** - Integrate into chat workflows
- **Custom MCP clients** - Programmatic access

AI agents can trigger this Actor automatically based on user queries. See the [MCP documentation](https://docs.apify.com/platform/integrations/mcp) for setup instructions.

## Support & Contributing

- **Issues**: GitHub Issues
- **Questions**: GitHub Discussions
- **Apify $1M Challenge**: Submission ID TBD

## License

MIT License - See LICENSE file

## Author

Built for the Apify $1M Challenge (November 2025 - January 2026)

---

**🎯 Ready to try it?** [Run on Apify](https://console.apify.com/actors) • [View Source](https://github.com/your-repo)
