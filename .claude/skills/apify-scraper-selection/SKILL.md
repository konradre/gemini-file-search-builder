---
name: apify-scraper-selection
description: Select optimal Apify scraper from 8,000+ Store catalog. Filter banned patterns per challenge terms. Score by budget mode. Configure fallbacks. Use when scraping, data extraction, web automation requested.
allowed-tools: Read
---

# Apify Scraper Selection

## Progressive Disclosure

**Level 1** (This file): Core selection logic (~800 tokens)
**Level 2**: BANNED_PATTERNS.md (~1K tokens, load before execution)
**Level 3**: SCORING_ALGORITHM.md (~1.5K tokens, load if tuning)

## Quick Start

1. Load banned patterns: Read .claude/skills/apify-scraper-selection/BANNED_PATTERNS.md
2. Query Apify Store (via Apify Client API)
3. Filter banned scrapers
4. Score by budget mode (minimal/optimal/premium)
5. Return top 3 + fallbacks

## When This Activates

Keywords: scrape, extract, crawl, data collection, web automation
