# Apify $1M Challenge Banned Scrapers

**Last Updated**: 2025-11-10
**Source**: https://apify.com/challenges/ai-1m-dollar-challenge (Section 2.3)

## Pattern Matching Rules

Reject if actor ID, title, or description contains:

### Social Media (Banned)
- instagram
- facebook
- tiktok
- linkedin
- twitter, x-scraper
- youtube

### E-Commerce (Banned)
- amazon, amz-

### Search Engines (Banned)
- google-maps
- google-search
- google-trends

### B2B Platforms (Banned)
- apollo, apollo-io

## Implementation

```python
BANNED_PATTERNS = [
    'instagram', 'facebook', 'tiktok', 'linkedin',
    'twitter', 'x-scraper', 'youtube',
    'amazon', 'amz-',
    'google-maps', 'google-search', 'google-trends',
    'apollo'
]

def is_scraper_banned(actor: dict) -> bool:
    text = f"{actor['id']} {actor.get('title', '')} {actor.get('description', '')}".lower()
    return any(pattern in text for pattern in BANNED_PATTERNS)
```
