"""
Banned Filter Tests - 100% Pass Rate Required

CRITICAL: These tests validate Apify $1M Challenge compliance.
ALL tests MUST pass before deployment to cloud.

Test coverage:
- All banned patterns (social media, e-commerce, search engines, B2B)
- Allowed scrapers (general web, documentation, forums, etc.)
- Edge cases (partial matches, case insensitivity, combined patterns)
- Real-world examples from Apify Store
"""

import pytest
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from tools.scraper_selector import (
    is_scraper_banned,
    filter_banned_scrapers,
    BANNED_PATTERNS
)


# ========== BANNED SCRAPERS (MUST ALL RETURN TRUE) ==========

class TestBannedSocialMedia:
    """Test social media scrapers are banned"""

    def test_instagram_scraper(self):
        """Instagram scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/instagram-scraper'}) == True

    def test_instagram_posts(self):
        """Instagram post scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/instagram-posts-scraper'}) == True

    def test_facebook_scraper(self):
        """Facebook scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/facebook-posts'}) == True

    def test_facebook_pages(self):
        """Facebook page scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/facebook-pages-scraper'}) == True

    def test_tiktok_scraper(self):
        """TikTok scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/tiktok-scraper'}) == True

    def test_linkedin_scraper(self):
        """LinkedIn scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/linkedin-profile-scraper'}) == True

    def test_linkedin_jobs(self):
        """LinkedIn job scrapers must be banned"""
        assert is_scraper_banned({'id': 'epctex/linkedin-jobs-scraper'}) == True

    def test_twitter_scraper(self):
        """Twitter scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/twitter-scraper'}) == True

    def test_x_scraper(self):
        """X (Twitter) scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/x-scraper'}) == True

    def test_youtube_scraper(self):
        """YouTube scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/youtube-scraper'}) == True

    def test_youtube_channel(self):
        """YouTube channel scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/youtube-channel-scraper'}) == True


class TestBannedEcommerce:
    """Test e-commerce scrapers are banned"""

    def test_amazon_scraper(self):
        """Amazon scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/amazon-scraper'}) == True

    def test_amazon_products(self):
        """Amazon product scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/amazon-products-scraper'}) == True

    def test_amazon_reviews(self):
        """Amazon review scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/amazon-reviews-scraper'}) == True

    def test_amz_prefix(self):
        """Amazon scrapers with amz- prefix must be banned"""
        assert is_scraper_banned({'id': 'apify/amz-product-scraper'}) == True


class TestBannedSearchEngines:
    """Test search engine scrapers are banned"""

    def test_google_maps(self):
        """Google Maps scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/google-maps-scraper'}) == True

    def test_google_search(self):
        """Google Search scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/google-search-scraper'}) == True

    def test_google_trends(self):
        """Google Trends scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/google-trends-scraper'}) == True


class TestBannedB2B:
    """Test B2B platform scrapers are banned"""

    def test_apollo_scraper(self):
        """Apollo scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/apollo-scraper'}) == True

    def test_apollo_io(self):
        """Apollo.io scrapers must be banned"""
        assert is_scraper_banned({'id': 'apify/apollo-io-scraper'}) == True


# ========== ALLOWED SCRAPERS (MUST ALL RETURN FALSE) ==========

class TestAllowedScrapers:
    """Test general web scrapers are allowed"""

    def test_web_scraper(self):
        """Generic web scrapers must be allowed"""
        assert is_scraper_banned({'id': 'apify/web-scraper'}) == False

    def test_cheerio_scraper(self):
        """Cheerio scraper must be allowed"""
        assert is_scraper_banned({'id': 'apify/cheerio-scraper'}) == False

    def test_puppeteer_scraper(self):
        """Puppeteer scraper must be allowed"""
        assert is_scraper_banned({'id': 'apify/puppeteer-scraper'}) == False

    def test_playwright_scraper(self):
        """Playwright scraper must be allowed"""
        assert is_scraper_banned({'id': 'apify/playwright-scraper'}) == False

    def test_beautifulsoup_scraper(self):
        """BeautifulSoup scraper must be allowed"""
        assert is_scraper_banned({'id': 'apify/beautifulsoup-scraper'}) == False

    def test_reddit_scraper(self):
        """Reddit scrapers must be allowed (not in banned list)"""
        assert is_scraper_banned({'id': 'apify/reddit-scraper'}) == False

    def test_github_scraper(self):
        """GitHub scrapers must be allowed"""
        assert is_scraper_banned({'id': 'apify/github-scraper'}) == False

    def test_hacker_news_scraper(self):
        """Hacker News scrapers must be allowed"""
        assert is_scraper_banned({'id': 'apify/hacker-news-scraper'}) == False

    def test_documentation_scraper(self):
        """Documentation scrapers must be allowed"""
        assert is_scraper_banned({'id': 'apify/documentation-scraper'}) == False

    def test_blog_scraper(self):
        """Blog scrapers must be allowed"""
        assert is_scraper_banned({'id': 'apify/blog-scraper'}) == False

    def test_news_scraper(self):
        """News scrapers must be allowed"""
        assert is_scraper_banned({'id': 'apify/news-article-scraper'}) == False


# ========== EDGE CASES ==========

class TestEdgeCases:
    """Test edge cases and tricky scenarios"""

    def test_case_insensitive_instagram(self):
        """Pattern matching must be case-insensitive"""
        assert is_scraper_banned({'id': 'APIFY/INSTAGRAM-SCRAPER'}) == True

    def test_mixed_case_facebook(self):
        """Mixed case patterns must be detected"""
        assert is_scraper_banned({'id': 'apify/FaceBook-Scraper'}) == True

    def test_title_contains_banned(self):
        """Banned patterns in title must be detected"""
        assert is_scraper_banned({
            'id': 'apify/web-scraper',
            'title': 'Instagram Data Extractor'
        }) == True

    def test_description_contains_banned(self):
        """Banned patterns in description must be detected"""
        assert is_scraper_banned({
            'id': 'apify/web-scraper',
            'title': 'Web Scraper',
            'description': 'Scrape data from Amazon product pages'
        }) == True

    def test_partial_match_not_banned(self):
        """Partial matches that don't match patterns should be allowed"""
        # 'face' is not 'facebook'
        assert is_scraper_banned({'id': 'apify/interface-scraper'}) == False
        # 'linked' is not 'linkedin'
        assert is_scraper_banned({'id': 'apify/linked-data-scraper'}) == False

    def test_empty_actor_dict(self):
        """Empty actor dict should not crash (returns False)"""
        assert is_scraper_banned({}) == False

    def test_missing_fields(self):
        """Missing fields should not crash"""
        assert is_scraper_banned({'id': 'apify/web-scraper'}) == False
        assert is_scraper_banned({'title': 'Web Scraper'}) == False

    def test_whitespace_handling(self):
        """Patterns with hyphens should be detected"""
        # Our patterns use hyphens (google-maps), so hyphens should match
        assert is_scraper_banned({'id': 'apify/google-maps-scraper'}) == True
        # Compound without hyphen should still match substring
        assert is_scraper_banned({'id': 'apify/googlemaps'}) == False  # Doesn't contain 'google-maps'


# ========== FILTER FUNCTION TESTS ==========

class TestFilterBannedScrapers:
    """Test the filter function that processes lists"""

    def test_filter_all_allowed(self):
        """Filter should return all actors if none banned"""
        actors = [
            {'id': 'apify/web-scraper'},
            {'id': 'apify/cheerio-scraper'},
            {'id': 'apify/reddit-scraper'}
        ]
        result = filter_banned_scrapers(actors)
        assert len(result) == 3

    def test_filter_all_banned(self):
        """Filter should return empty list if all banned"""
        actors = [
            {'id': 'apify/instagram-scraper'},
            {'id': 'apify/facebook-scraper'},
            {'id': 'apify/amazon-scraper'}
        ]
        result = filter_banned_scrapers(actors)
        assert len(result) == 0

    def test_filter_mixed(self):
        """Filter should return only allowed actors from mixed list"""
        actors = [
            {'id': 'apify/web-scraper'},           # Allowed
            {'id': 'apify/instagram-scraper'},    # Banned
            {'id': 'apify/cheerio-scraper'},      # Allowed
            {'id': 'apify/amazon-scraper'},       # Banned
            {'id': 'apify/reddit-scraper'}        # Allowed
        ]
        result = filter_banned_scrapers(actors)
        assert len(result) == 3
        assert all(not is_scraper_banned(actor) for actor in result)

    def test_filter_preserves_order(self):
        """Filter should preserve order of allowed actors"""
        actors = [
            {'id': 'apify/web-scraper'},
            {'id': 'apify/instagram-scraper'},  # Banned
            {'id': 'apify/cheerio-scraper'},
        ]
        result = filter_banned_scrapers(actors)
        assert result[0]['id'] == 'apify/web-scraper'
        assert result[1]['id'] == 'apify/cheerio-scraper'

    def test_filter_empty_list(self):
        """Filter should handle empty list"""
        result = filter_banned_scrapers([])
        assert len(result) == 0


# ========== PATTERN COVERAGE TEST ==========

class TestPatternCoverage:
    """Ensure all BANNED_PATTERNS are tested"""

    def test_all_patterns_have_tests(self):
        """Verify each banned pattern has at least one test case"""
        # This is a meta-test to ensure coverage
        tested_patterns = {
            'instagram', 'facebook', 'tiktok', 'linkedin',
            'twitter', 'x-scraper', 'youtube',
            'amazon', 'amz-',
            'google-maps', 'google-search', 'google-trends',
            'apollo', 'apollo-io'
        }

        for pattern in BANNED_PATTERNS:
            assert pattern in tested_patterns, f"Pattern '{pattern}' is not tested!"


# ========== REAL-WORLD VALIDATION ==========

class TestRealWorldExamples:
    """Test with real actor IDs from Apify Store"""

    def test_apify_web_scraper_allowed(self):
        """apify/web-scraper is the most popular general scraper"""
        assert is_scraper_banned({'id': 'apify/web-scraper'}) == False

    def test_apify_cheerio_scraper_allowed(self):
        """apify/cheerio-scraper is popular for HTML parsing"""
        assert is_scraper_banned({'id': 'apify/cheerio-scraper'}) == False

    def test_epctex_instagram_banned(self):
        """Third-party Instagram scrapers must also be banned"""
        assert is_scraper_banned({'id': 'epctex/instagram-scraper'}) == True

    def test_epctex_web_scraper_allowed(self):
        """Third-party general scrapers should be allowed"""
        assert is_scraper_banned({'id': 'epctex/smart-web-scraper'}) == False


# ========== RUN ALL TESTS ==========

if __name__ == '__main__':
    # Run pytest programmatically
    pytest.main([__file__, '-v', '--tb=short'])
