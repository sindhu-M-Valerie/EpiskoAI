#!/usr/bin/env python3
"""
Real Job Scraper for Trust & Safety Positions
Fetches actual job listings from multiple sources
"""

import requests
import json
from datetime import datetime, timedelta
from typing import List, Dict
import os

class JobAggregator:
    def __init__(self):
        self.jobs = []
        self.days_old_threshold = 60  # Only show jobs posted within last 60 days
        
    def is_job_recent(self, posted_date_str: str) -> bool:
        """Check if job was posted within the threshold"""
        try:
            from datetime import timezone
            # Parse various date formats
            if 'T' in posted_date_str:
                # Remove timezone info for simpler comparison
                posted_date_str = posted_date_str.split('T')[0] + 'T' + posted_date_str.split('T')[1].split('-')[0].split('+')[0]
                posted_date = datetime.fromisoformat(posted_date_str.replace('Z', ''))
            else:
                posted_date = datetime.strptime(posted_date_str, "%Y-%m-%d")
            
            cutoff_date = datetime.now() - timedelta(days=self.days_old_threshold)
            
            return posted_date.replace(tzinfo=None) >= cutoff_date.replace(tzinfo=None)
        except Exception as e:
            # If we can't parse the date, assume it's recent
            return True
        
    def fetch_adzuna_jobs(self, api_id: str = None, api_key: str = None) -> List[Dict]:
        """Fetch jobs from Adzuna API (UK & US job boards)"""
        if not api_id or not api_key:
            print("ℹ️  Adzuna API credentials not provided. Visit https://developer.adzuna.com/")
            return []
            
        jobs = []
        keywords = ["trust and safety", "content moderation", "fraud prevention", "threat intelligence"]
        
        for keyword in keywords:
            try:
                url = f"https://api.adzuna.com/v1/api/jobs/us/search/1"
                params = {
                    "app_id": api_id,
                    "app_key": api_key,
                    "what": keyword,
                    "results_per_page": 20,
                    "content-type": "application/json"
                }
                
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    for result in data.get("results", []):
                        company_name = result.get("company", {}).get("display_name", "Unknown")
                        jobs.append({
                            "company": company_name,
                            "company_url": f"https://www.google.com/search?q={company_name.replace(' ', '+')}",  # Generic search link
                            "title": result.get("title", ""),
                            "location": result.get("location", {}).get("display_name", "Unknown"),
                            "description": result.get("description", "")[:200] + "...",
                            "url": result.get("redirect_url", ""),
                            "salary": result.get("salary_min", "Not specified"),
                            "posted_date": result.get("created", "Unknown"),
                            "source": "Adzuna"
                        })
            except Exception as e:
                print(f"⚠️  Error fetching from Adzuna for '{keyword}': {e}")
                
        return jobs
    
    def fetch_greenhouse_jobs(self) -> List[Dict]:
        """Fetch jobs from companies using Greenhouse ATS"""
        jobs = []
        companies = {
            # Major Tech
            "figma": ("Figma", "https://www.figma.com"),
            "canva": ("Canva", "https://www.canva.com"), 
            "grammarly": ("Grammarly", "https://www.grammarly.com"),
            "airtable": ("Airtable", "https://www.airtable.com"),
            "databricks": ("Databricks", "https://www.databricks.com"),
            "cloudflare": ("Cloudflare", "https://www.cloudflare.com"),
            "doordash": ("DoorDash", "https://www.doordash.com"),
            "github": ("GitHub", "https://github.com"),
            "gitlab": ("GitLab", "https://about.gitlab.com"),
            "stripe": ("Stripe", "https://stripe.com"),
            "square": ("Square", "https://squareup.com"),
            "dropbox": ("Dropbox", "https://www.dropbox.com"),
            "atlassian": ("Atlassian", "https://www.atlassian.com"),
            "snap": ("Snap Inc", "https://www.snap.com"),
            "uber": ("Uber", "https://www.uber.com"),
            "lyft": ("Lyft", "https://www.lyft.com"),
            "airbnb": ("Airbnb", "https://www.airbnb.com"),
            "twitch": ("Twitch", "https://www.twitch.tv"),
            "reddit": ("Reddit", "https://www.reddit.com"),
            "discord": ("Discord", "https://discord.com"),
            "roblox": ("Roblox", "https://corp.roblox.com"),
            "spotify": ("Spotify", "https://www.spotify.com"),
            "netflix": ("Netflix", "https://www.netflix.com"),
            "patreon": ("Patreon", "https://www.patreon.com"),
            "pinterest": ("Pinterest", "https://www.pinterest.com"),
            "medium": ("Medium", "https://medium.com"),
            "tumblr": ("Tumblr", "https://www.tumblr.com"),
            "vimeo": ("Vimeo", "https://vimeo.com"),
            "soundcloud": ("SoundCloud", "https://soundcloud.com"),
            
            # Web3/Crypto
            "immunefi": ("Immunefi", "https://immunefi.com"),
            "chainalysis": ("Chainalysis", "https://www.chainalysis.com"),
            "consensys": ("ConsenSys", "https://consensys.net"),
            "alchemy": ("Alchemy", "https://www.alchemy.com"),
            "coinbase": ("Coinbase", "https://www.coinbase.com"),
            "circle": ("Circle", "https://www.circle.com"),
            "gemini": ("Gemini", "https://www.gemini.com"),
            "opensea": ("OpenSea", "https://opensea.io"),
            "uniswap": ("Uniswap Labs", "https://uniswap.org"),
            "luno": ("Luno", "https://www.luno.com"),
            "kraken": ("Kraken", "https://www.kraken.com"),
            "binance": ("Binance", "https://www.binance.com"),
            "blockdaemon": ("Blockdaemon", "https://blockdaemon.com"),
            "infura": ("Infura", "https://infura.io"),
            "anchorage": ("Anchorage Digital", "https://www.anchorage.com"),
            "fireblocks": ("Fireblocks", "https://www.fireblocks.com"),
            "messari": ("Messari", "https://messari.io"),
            "aave": ("Aave", "https://aave.com"),
            "sushiswap": ("SushiSwap", "https://www.sushi.com"),
            "thegraph": ("The Graph", "https://thegraph.com"),
            "pythereum": ("Pyth Network", "https://pyth.network"),
            "lido": ("Lido", "https://lido.fi"),
            "rarible": ("Rarible", "https://rarible.com"),
            "magiceden": ("Magic Eden", "https://magiceden.io"),
            "looksrare": ("LooksRare", "https://looksrare.org"),
            "moonbeam": ("Moonbeam", "https://moonbeam.network"),
            "render": ("Render", "https://render.com"),
            "farcaster": ("Farcaster", "https://www.farcaster.xyz"),
            "lensprotocol": ("Lens Protocol", "https://www.lens.xyz"),
            "optimism": ("Optimism", "https://optimism.io"),
            "arbitrum": ("Arbitrum", "https://arbitrum.io"),
            "polygon": ("Polygon", "https://polygon.technology"),
            "solana": ("Solana Labs", "https://solana.com"),
            "avalabs": ("Avalabs", "https://www.avalabs.org"),
            "near": ("Near Protocol", "https://near.org"),
            "sideshift": ("SideShift.ai", "https://sideshift.ai"),
            "changelly": ("Changelly", "https://changelly.com"),
            "shapeshift": ("ShapeShift", "https://shapeshift.com"),
            "thorchain": ("Thorchain", "https://thorchain.org"),
            "0x": ("0x", "https://0x.org"),
            "paraswap": ("Paraswap", "https://paraswap.io"),
            "kybernetwork": ("Kyber Network", "https://kyber.network"),
            "lifi": ("Li.Fi", "https://li.fi"),
            "dydx": ("dYdX", "https://dydx.exchange"),
            "compound": ("Compound", "https://compound.finance"),
            "makerdao": ("MakerDAO", "https://makerdao.com"),
            "curve": ("Curve Finance", "https://curve.fi"),
            "balancer": ("Balancer", "https://balancer.fi"),
            "1inch": ("1inch", "https://1inch.io"),
            "metamask": ("MetaMask", "https://metamask.io"),
            "rainbow": ("Rainbow", "https://rainbow.me"),
            "phantom": ("Phantom", "https://phantom.app"),
            "ledger": ("Ledger", "https://www.ledger.com"),
            "trezor": ("Trezor", "https://trezor.io"),
            "safe": ("Safe", "https://safe.global"),
            "zksync": ("zkSync", "https://zksync.io"),
            "starkware": ("StarkWare", "https://starkware.co"),
            "matter-labs": ("Matter Labs", "https://matter-labs.io"),
            "scroll": ("Scroll", "https://scroll.io"),
            "base": ("Base", "https://base.org"),
            "mantle": ("Mantle", "https://www.mantle.xyz"),
            "linea": ("Linea", "https://linea.build"),
            
            # Blockchain Security & Auditing
            "code4rena": ("Code4rena", "https://code4rena.com"),
            "sherlock": ("Sherlock", "https://www.sherlock.xyz"),
            "openzeppelin": ("OpenZeppelin", "https://www.openzeppelin.com"),
            "certik": ("CertiK", "https://www.certik.com"),
            "halborn": ("Halborn", "https://halborn.com"),
            "trailofbits": ("Trail of Bits", "https://www.trailofbits.com"),
            
            # Blockchain Analytics & Compliance
            "trmlabs": ("TRM Labs", "https://www.trmlabs.com"),
            "elliptic": ("Elliptic", "https://www.elliptic.co"),
            "crystalblockchain": ("Crystal Blockchain", "https://crystalblockchain.com"),
            "merklescience": ("Merkle Science", "https://www.merklescience.com"),
            
            # AI Startups
            "anthropic": ("Anthropic", "https://www.anthropic.com"),
            "openai": ("OpenAI", "https://www.openai.com"),
            "scale": ("Scale AI", "https://scale.com"),
            "huggingface": ("Hugging Face", "https://huggingface.co"),
            "cohere": ("Cohere", "https://cohere.com"),
            "adept": ("Adept", "https://www.adept.ai"),
            "inflection": ("Inflection AI", "https://inflection.ai"),
            "character": ("Character.AI", "https://character.ai"),
            "midjourney": ("Midjourney", "https://www.midjourney.com"),
            "runway": ("Runway", "https://runwayml.com"),
            "jasper": ("Jasper", "https://www.jasper.ai"),
            "replicate": ("Replicate", "https://replicate.com"),
            "together": ("Together AI", "https://www.together.ai"),
            "mosaic": ("MosaicML", "https://www.mosaicml.com"),
            "ai21": ("AI21 Labs", "https://www.ai21.com"),
            "perplexity": ("Perplexity AI", "https://www.perplexity.ai"),
            "stability": ("Stability AI", "https://stability.ai"),
            "cresta": ("Cresta", "https://cresta.com"),
            "synthesia": ("Synthesia", "https://www.synthesia.io"),
            "elevenlabs": ("ElevenLabs", "https://elevenlabs.io"),
            "replit": ("Replit", "https://replit.com"),
            "mem": ("Mem", "https://get.mem.ai"),
            "glean": ("Glean", "https://www.glean.com"),
            "harvey": ("Harvey", "https://www.harvey.ai"),
            "typeface": ("Typeface", "https://www.typeface.ai"),
            "aleph-alpha": ("Aleph Alpha", "https://www.aleph-alpha.com"),
            "lightricks": ("Lightricks", "https://www.lightricks.com"),
            "writer": ("Writer", "https://writer.com"),
            "reka": ("Reka AI", "https://reka.ai"),
            "mistral": ("Mistral AI", "https://mistral.ai"),
            "poolside": ("Poolside", "https://poolside.ai"),
            "magic": ("Magic", "https://magic.dev"),
            
            # Security/Bug Bounty/Cybersecurity
            "okta": ("Okta", "https://www.okta.com"),
            "auth0": ("Auth0", "https://auth0.com"),
            "crowdstrike": ("CrowdStrike", "https://www.crowdstrike.com"),
            "datadog": ("Datadog", "https://www.datadoghq.com"),
            "elastic": ("Elastic", "https://www.elastic.co"),
            "splunk": ("Splunk", "https://www.splunk.com"),
            "hackerone": ("HackerOne", "https://www.hackerone.com"),
            "bugcrowd": ("Bugcrowd", "https://www.bugcrowd.com"),
            "synack": ("Synack", "https://www.synack.com"),
            "cobalt": ("Cobalt", "https://cobalt.io"),
            "safebreach": ("SafeBreach", "https://safebreach.com"),
            "paloaltonetworks": ("Palo Alto Networks", "https://www.paloaltonetworks.com"),
            "sentinelone": ("SentinelOne", "https://www.sentinelone.com"),
            "trellix": ("Trellix", "https://www.trellix.com"),
            "checkpoint": ("Check Point", "https://www.checkpoint.com"),
            "sophos": ("Sophos", "https://www.sophos.com"),
            "akamai": ("Akamai", "https://www.akamai.com"),
            "cisco": ("Cisco Security", "https://www.cisco.com"),
            "rapid7": ("Rapid7", "https://www.rapid7.com"),
            "tenable": ("Tenable", "https://www.tenable.com"),
            "arcticwolf": ("Arctic Wolf", "https://arcticwolf.com"),
            
            # E-commerce/Marketplaces
            "shopify": ("Shopify", "https://www.shopify.com"),
            "etsy": ("Etsy", "https://www.etsy.com"),
            "instacart": ("Instacart", "https://www.instacart.com"),
            "doordash": ("DoorDash", "https://www.doordash.com"),
            
            # Developer Tools
            "vercel": ("Vercel", "https://vercel.com"),
            "notion": ("Notion", "https://www.notion.so"),
            "linear": ("Linear", "https://linear.app"),
            "retool": ("Retool", "https://retool.com"),
            "webflow": ("Webflow", "https://webflow.com"),
            "miro": ("Miro", "https://miro.com"),
            "docker": ("Docker", "https://www.docker.com"),
            "hashicorp": ("HashiCorp", "https://www.hashicorp.com"),
            "mongodb": ("MongoDB", "https://www.mongodb.com"),
            "postman": ("Postman", "https://www.postman.com"),
            "confluent": ("Confluent", "https://www.confluent.io"),
            "snyk": ("Snyk", "https://snyk.io"),
            "pagerduty": ("PagerDuty", "https://www.pagerduty.com"),
            "new-relic": ("New Relic", "https://newrelic.com"),
            "sentry": ("Sentry", "https://sentry.io"),
            
            # Social/Communication
            "bumble": ("Bumble", "https://bumble.com"),
            "hinge": ("Hinge", "https://hinge.co"),
            "match": ("Match Group", "https://mtch.com"),
            "zoom": ("Zoom", "https://zoom.us"),
            "slack": ("Slack", "https://slack.com"),
            
            # Gaming
            "riotgames": ("Riot Games", "https://www.riotgames.com"),
            "unity": ("Unity Technologies", "https://unity.com"),
            "epicgames": ("Epic Games", "https://www.epicgames.com"),
            "ea": ("Electronic Arts", "https://www.ea.com"),
            "activision": ("Activision Blizzard", "https://www.activisionblizzard.com"),
            "blizzard": ("Blizzard Entertainment", "https://www.blizzard.com"),
            "bungie": ("Bungie", "https://www.bungie.net"),
            "supercell": ("Supercell", "https://supercell.com"),
            "king": ("King", "https://king.com"),
            "zynga": ("Zynga", "https://www.zynga.com")
        }
        
        keywords = ["trust", "safety", "security", "fraud", "risk", "moderation", "abuse", "compliance", "policy", "integrity", "operations", "support", "investigation"]
        
        for company_slug, company_info in companies.items():
            company_name, company_url = company_info
            try:
                url = f"https://boards-api.greenhouse.io/v1/boards/{company_slug}/jobs"
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    for job in data.get("jobs", []):
                        title = job.get("title", "").lower()
                        posted_date = job.get("updated_at", "Unknown")
                        
                        # Filter by keywords and recency
                        if any(keyword in title for keyword in keywords) and self.is_job_recent(posted_date):
                            jobs.append({
                                "company": company_name,
                                "company_url": company_url,
                                "title": job.get("title", ""),
                                "location": job.get("location", {}).get("name", "Unknown"),
                                "url": job.get("absolute_url", ""),
                                "posted_date": posted_date,
                                "source": "Greenhouse",
                                "id": job.get("id", "")
                            })
            except Exception as e:
                print(f"⚠️  Error fetching from Greenhouse for {company_name}: {e}")
                
        return jobs
    
    def fetch_cryptojobslist_jobs(self) -> List[Dict]:
        """Fetch jobs from CryptoJobsList RSS feed"""
        jobs = []
        keywords = ["trust", "safety", "security", "fraud", "risk", "moderation", "abuse", "compliance", "support"]
        
        try:
            # Try the RSS feed first (more accessible than HTML scraping)
            import xml.etree.ElementTree as ET
            
            rss_url = "https://cryptojobslist.com/jobs.rss"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(rss_url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                
                for item in root.findall('.//item')[:100]:  # Limit to first 100
                    try:
                        title = item.find('title').text if item.find('title') is not None else ""
                        
                        # Check if title matches keywords
                        if not any(keyword in title.lower() for keyword in keywords):
                            continue
                        
                        # Extract job details
                        link = item.find('link').text if item.find('link') is not None else ""
                        description = item.find('description').text if item.find('description') is not None else ""
                        pub_date = item.find('pubDate').text if item.find('pubDate') is not None else datetime.now().isoformat()
                        
                        # Try to extract company from title or description
                        company = "Unknown"
                        if " at " in title:
                            company = title.split(" at ")[-1].strip()
                        
                        # Extract location from description if possible
                        location = "Remote"
                        if "location" in description.lower():
                            # Simple extraction, can be improved
                            location = "Remote / Flexible"
                        
                        jobs.append({
                            "company": company,
                            "company_url": f"https://www.google.com/search?q={company.replace(' ', '+')}",
                            "title": title,
                            "location": location,
                            "url": link,
                            "posted_date": pub_date,
                            "source": "CryptoJobsList"
                        })
                    except Exception as e:
                        continue
                        
        except Exception as e:
            print(f"⚠️  Error fetching from CryptoJobsList: {e}")
        
        return jobs
    
    def fetch_remoteok_jobs(self) -> List[Dict]:
        """Fetch jobs from RemoteOK API"""
        jobs = []
        keywords = ["trust", "safety", "security", "fraud", "risk", "moderation", "abuse", "compliance", "support"]
        
        try:
            url = "https://remoteok.com/api"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                # First item is usually metadata, skip it
                jobs_data = data[1:] if isinstance(data, list) and len(data) > 1 else data
                
                for job in jobs_data[:200]:  # Limit to first 200
                    if not isinstance(job, dict):
                        continue
                        
                    title = job.get('position', '').lower()
                    tags = ' '.join(job.get('tags', [])).lower() if job.get('tags') else ''
                    
                    # Filter by keywords in title or tags
                    if not any(keyword in title or keyword in tags for keyword in keywords):
                        continue
                    
                    # Extract date
                    posted_date = job.get('date', datetime.now().isoformat())
                    if isinstance(posted_date, (int, float)):
                        # Convert timestamp to ISO format
                        posted_date = datetime.fromtimestamp(posted_date).isoformat()
                    
                    # Check if recent
                    if not self.is_job_recent(posted_date):
                        continue
                    
                    jobs.append({
                        "company": job.get('company', 'Unknown'),
                        "company_url": job.get('company_url', ''),
                        "title": job.get('position', ''),
                        "location": job.get('location', 'Remote'),
                        "url": job.get('url', f"https://remoteok.com/jobs/{job.get('id', '')}"),
                        "posted_date": posted_date,
                        "source": "RemoteOK"
                    })
        except Exception as e:
            print(f"⚠️  Error fetching from RemoteOK: {e}")
        
        return jobs
    
    def fetch_lever_jobs(self) -> List[Dict]:
        """Fetch jobs from companies using Lever ATS"""
        jobs = []
        companies = {
            "cloudflare": ("Cloudflare", "https://www.cloudflare.com"),
            "affirm": ("Affirm", "https://www.affirm.com"),
            "asana": ("Asana", "https://asana.com"),
            "notion": ("Notion", "https://www.notion.so"),
            "figma": ("Figma", "https://www.figma.com"),
            "gusto": ("Gusto", "https://gusto.com"),
            "benchling": ("Benchling", "https://www.benchling.com"),
            "airtable": ("Airtable", "https://www.airtable.com"),
            "ripple": ("Ripple", "https://ripple.com"),
            "tiktok": ("TikTok", "https://www.tiktok.com"),
            "bytedance": ("ByteDance", "https://www.bytedance.com"),
            "stripe": ("Stripe", "https://stripe.com"),
            "canva": ("Canva", "https://www.canva.com"),
            "linkedin": ("LinkedIn", "https://www.linkedin.com"),
            "netflix": ("Netflix", "https://www.netflix.com"),
            "meta": ("Meta", "https://www.meta.com"),
            "moonpay": ("MoonPay", "https://www.moonpay.com"),
            "github": ("GitHub", "https://github.com")
        }
        
        keywords = ["trust", "safety", "security", "fraud", "risk", "compliance", "policy", "integrity", "operations", "support", "investigation", "moderation"]
        
        for company_slug, company_info in companies.items():
            company_name, company_url = company_info
            try:
                url = f"https://api.lever.co/v0/postings/{company_slug}"
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    for job in data:
                        title = job.get("text", "").lower()
                        posted_date = job.get("createdAt", "Unknown")
                        
                        # Filter by keywords and recency
                        if any(keyword in title for keyword in keywords) and self.is_job_recent(posted_date):
                            jobs.append({
                                "company": company_name,
                                "company_url": company_url,
                                "title": job.get("text", ""),
                                "location": job.get("categories", {}).get("location", "Unknown"),
                                "url": job.get("hostedUrl", ""),
                                "posted_date": posted_date,
                                "source": "Lever"
                            })
            except Exception as e:
                print(f"⚠️  Error fetching from Lever for {company_name}: {e}")
                
        return jobs
    
    def fetch_all_jobs(self) -> List[Dict]:
        """Aggregate jobs from all sources"""
        all_jobs = []
        
        print("🔍 Fetching real job listings...")
        
        # Greenhouse jobs (free, no API key needed)
        print("📋 Checking Greenhouse...")
        greenhouse_jobs = self.fetch_greenhouse_jobs()
        all_jobs.extend(greenhouse_jobs)
        print(f"   Found {len(greenhouse_jobs)} jobs from Greenhouse")
        
        # Lever jobs (free, no API key needed)
        print("📋 Checking Lever...")
        lever_jobs = self.fetch_lever_jobs()
        all_jobs.extend(lever_jobs)
        print(f"   Found {len(lever_jobs)} jobs from Lever")
        
        # CryptoJobsList (free, no API key needed)
        print("📋 Checking CryptoJobsList...")
        crypto_jobs = self.fetch_cryptojobslist_jobs()
        all_jobs.extend(crypto_jobs)
        print(f"   Found {len(crypto_jobs)} jobs from CryptoJobsList")
        
        # RemoteOK (free, no API key needed)
        print("📋 Checking RemoteOK...")
        remoteok_jobs = self.fetch_remoteok_jobs()
        all_jobs.extend(remoteok_jobs)
        print(f"   Found {len(remoteok_jobs)} jobs from RemoteOK")
        
        # Adzuna jobs (requires free API key)
        adzuna_id = os.environ.get("ADZUNA_API_ID")
        adzuna_key = os.environ.get("ADZUNA_API_KEY")
        if adzuna_id and adzuna_key:
            print("📋 Checking Adzuna...")
            adzuna_jobs = self.fetch_adzuna_jobs(adzuna_id, adzuna_key)
            all_jobs.extend(adzuna_jobs)
            print(f"   Found {len(adzuna_jobs)} jobs from Adzuna")
        
        print(f"\n✅ Total jobs found: {len(all_jobs)}")
        return all_jobs
    
    def save_jobs_json(self, filename: str = "jobs_data.json"):
        """Save jobs to JSON file"""
        jobs = self.fetch_all_jobs()
        data = {
            "last_updated": datetime.now().isoformat(),
            "total_jobs": len(jobs),
            "jobs": jobs
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Saved {len(jobs)} jobs to {filename}")
        return jobs

if __name__ == "__main__":
    print("🚀 EpiskoAI Real Job Aggregator\n")
    
    aggregator = JobAggregator()
    jobs = aggregator.save_jobs_json()
    
    if jobs:
        print("\n📊 Sample jobs:")
        for job in jobs[:5]:
            print(f"\n  • {job['title']} at {job['company']}")
            print(f"    📍 {job['location']}")
            print(f"    🔗 {job['url'][:60]}...")
    else:
        print("\n⚠️  No jobs found. Check API credentials or network connection.")
