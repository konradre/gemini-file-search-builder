# Monetization Setup Guide
**Actor:** Gemini File Search Builder
**Model:** Pay-Per-Page (PPE)
**Last Updated:** 2025-11-23

---

## 🎯 Pricing Strategy

**Per-Page Model (NOT per-job)**
- Start fee: ~$0.02 per run
- Per page: $0.0015/page base
- Store discounts: Up to 50% off

**Example costs:**
- 10 pages: $0.045 (FREE) → $0.025 (DIAMOND)
- 100 pages: $0.27 (FREE) → $0.145 (DIAMOND)
- 500 pages: $1.27 (FREE) → $0.645 (DIAMOND)

---

## ⚙️ Apify Console Configuration

### Step 1: Navigate to Monetization

1. Go to your Actor page in Apify Console
2. Click **"Settings"** tab
3. Scroll to **"Monetization"** section
4. Select **"Pay per event"** radio button

---

### Step 2: Configure Events

**You should have 2 events:**

#### Event 1: apify-actor-start (Automatic)

**This is pre-configured by Apify (don't change):**
- Event name: `apify-actor-start`
- Title: Actor Start
- Description: "Charged when the Actor starts running..."
- Price: $0.00005 per event
- **Leave as-is** ✅

#### Event 2: page-processed (Custom - YOU configure)

**Add new custom event:**
- Event name: `page-processed`
- Title: **Page Processed**
- Description: **Charged for each page successfully scraped and prepared for Gemini indexing**
- Price: **$0.0015**

**Click "+ Add event" and fill in:**

```
Event name: page-processed
Title: Page Processed
Description: Charged for each page successfully scraped and prepared for Gemini indexing
Price: 0.0015
```

---

### Step 3: Enable Store Discounts

**For the `page-processed` event:**

1. ✅ Check **"Set up Apify Store pricing discounts for this event"**

2. Fill in discount prices:

| Tier | Discount | Price to Enter |
|------|----------|----------------|
| **No discount (FREE)** | 0% | $0.0015 |
| **Bronze discount** | 10% | $0.00135 |
| **Silver discount** | 20% | $0.0012 |
| **Gold discount** | 30% | $0.00105 |

**Calculation:**
- Bronze: $0.0015 × 0.9 = $0.00135
- Silver: $0.0015 × 0.8 = $0.0012
- Gold: $0.0015 × 0.7 = $0.00105

---

### Step 4: Set Minimum Max Cost

**In "Additional options":**
- Minimum for max cost per run: **$0.20**

**Why $1.00:**
- Allows 10-page test runs ($0.045)
- Allows 100-page jobs ($0.27)
- Still reasonable minimum
- Prevents users setting $0.01 (insufficient)

---

### Step 5: Save

1. Click **"Save"** at bottom
2. Wait for confirmation
3. Monetization is now active!

---

## 🧪 Testing Monetization

### Test Before Going Live:

**Use test run with low page count:**

```json
{
  "target": "https://example.com",
  "max_pages": 10,
  "scraper_budget": "optimal"
}
```

**Expected charges:**
- Actor start: ~$0.02
- Pages (10): 10 × $0.0015 = $0.025
- **Total: ~$0.045**

**Verify in run details:**
- Check charges shown
- Confirm per-page charging works
- Validate Store discount applies (if you're on paid plan)

---

## 📊 Revenue Calculator

**Monthly revenue scenarios:**

### Conservative (Low Adoption):
- 10 users × 50 pages/month = 500 pages
- Revenue: $1.00 + $1.25 = **$2.25/month**

### Moderate (Medium Adoption):
- 50 users × 100 pages/month = 5,000 pages
- Revenue: $1.00 + $12.50 = **$13.50/month**

### Strong (High Adoption):
- 200 users × 150 pages/month = 30,000 pages
- Revenue: $4.00 + $75 = **$79/month**

### Excellent (Challenge Success):
- 500 users × 200 pages/month = 100,000 pages
- Revenue: $10 + $250 = **$260/month**

*During 0% commission period (until Mar 31, 2025): You keep 100%!*
*After: You keep 80% (20% Apify commission)*

---

## 🎯 Pricing Communication

### For Users (README/Description):

**Key messages:**
1. "Pay-per-page: $0.0015/page"
2. "Save up to 50% with higher Apify plans"
3. "Only charged for successfully processed pages"
4. "Typical 100-page job: $0.27"
5. "You provide your own Gemini API key (no token markup)"

### For Console Event Descriptions:

**page-processed event description:**
```
Charged for each page successfully scraped and prepared for Gemini indexing.
Includes content extraction, cleaning, and RAG optimization. Not charged for
failed pages or errors.
```

---

## ⚠️ Common Mistakes to Avoid

❌ **Setting price too high** - $0.01/page = 4x market rate
❌ **Not enabling Store discounts** - Misses revenue opportunity
❌ **Charging for failed pages** - Bad user experience
❌ **Confusing pricing model** - Mix of per-page and per-job
❌ **No cost estimates** - Users uncertain about budget

✅ **Do this instead:**
- Clear $0.0015/page pricing
- Enable all Store discount tiers
- Only charge on success
- Pure per-page model
- Show estimated costs upfront

---

## 📈 Optimization Strategy

### Month 1: Monitor & Learn
- Track adoption rate
- Monitor revenue per user
- Check if users hit budget limits
- Gather feedback on pricing

### Month 2-3: Adjust if Needed
- If adoption low: Consider lowering to $0.002/page
- If adoption high: Keep price, focus on scale
- If competition emerges: Adjust competitively

**Price change limit:** Once per month maximum, 14-day notice required

---

## ✅ Pre-Launch Checklist

**Monetization configured:**
- [ ] Pay-per-event model selected
- [ ] `apify-actor-start` event enabled (default price)
- [ ] `page-processed` event added ($0.0015)
- [ ] Store discounts enabled (10-50%)
- [ ] Minimum max cost set ($1.00)
- [ ] Saved successfully

**Code updated:**
- [x] Charges per page (not per job)
- [x] Shows cost estimates in logs
- [x] Respects budget limits
- [x] Only charges on success

**Documentation updated:**
- [x] README pricing section
- [x] INPUT_SCHEMA description
- [x] Cost examples clear
- [x] Store discounts explained

---

## 🚀 Go-Live Steps

1. ✅ Configure monetization (this document)
2. Create custom icon
3. Upload icon
4. **Rebuild actor** (gets latest code)
5. Test with 10-page run (verify $0.045 charge)
6. Publish to Store
7. Monitor first users

---

**Current status:** Code updated ✅, awaiting Console configuration + icon
