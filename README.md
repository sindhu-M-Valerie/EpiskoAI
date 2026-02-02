![EpiskoAI Logo](assets/logo.png)

# EpiskoAI

EpiskoAI — a vigilant AI agent that scouts Trust & Safety opportunities and filters signal from noise.

Meaning: From episkopos — “the watcher / overseer”

---

## What is EpiskoAI?

EpiskoAI is a personal AI observer that continuously watches the web for high-signal Trust & Safety roles, filters out noise (moderation farms, vendors, spammy listings), scores roles for personal relevance, and alerts you when something high-value appears.

It behaves like a junior threat analyst whose only job is to watch the job market for you.

Why this exists:
- Most job alerts are keyword-based and produce noisy results.
- EpiskoAI understands Trust & Safety nuance, explains why a role matches you, and prioritizes the highest-value leads.

---

## Key differences vs. standard job alerts

- Not just keyword matching — semantic classification into Trust & Safety subdomains.
- Vendor / BPO / moderation farm detection to reduce false positives.
- Personal matching using background and seniority signals.
- Human-friendly explanations for each match.

---

## Mental model / Agents

EpiskoAI is designed as four small cooperating agents:

1. The Watcher (Discovery)
   - Scrapes company career pages, ATS pages (Greenhouse, Lever...), job boards, and Google Jobs.
   - Output: raw job listing objects (title, company, description, url, posted_date).

2. The Interpreter (AI filtering)
   - Classifies listing into categories (Trust & Safety Ops, Threat Intel, Abuse/Fraud, Policy, Safety Engineering).
   - Detects seniority, flags vendor/BPO/moderation farms, extracts signals (telemetry, investigations, nation-state abuse).
   - Output: structured, scored job object.

3. The Matcher (Personal relevance)
   - Scores jobs against a personal preference/memory profile (titles, companies, locations, background).
   - Output: fit score, one-line reasoning.

4. The Messenger (Delivery)
   - Sends instant alerts for high-fit roles and daily/weekly digests for broader context.
   - Example channels: email / Slack / Notion.

---

## Architecture (text diagram)

Watcher -> Raw DB -> Interpreter (LLM) -> Scored DB -> Matcher -> Notification Queue -> Messenger (email/Slack/Notion)

Text diagram:

  +---------+     +--------+     +-------------+     +--------+     +-------------+
  | Watcher | --> | Raw DB | --> | Interpreter | --> | DB(ML) | --> | Messenger   |
  | (scrapes)|    | (sqlite)|    | (LLM classify)|   |(scored)|     | (email/Slack)|
  +---------+     +--------+     +-------------+     +--------+     +-------------+

Notes:
- The Interpreter writes structured JSON (category, seniority, flags, signals, score).
- The Matcher augments with personal-fit using the preference file.
- The Messenger only sends items above a threshold (e.g., fit >= 75%).

---

## MVP (3–5 days) — recommended plan

Phase 1 (MVP)
1. Preference file (YAML) — memory for matching.
2. Watcher (day 1–2) — scrape 5–10 companies, persist new listings to SQLite.
3. Interpreter (day 3) — send job description to an LLM for structured classification and score.
4. Notifications (day 4) — simple email or Notion delivery for high-fit roles.

Phase 2
- README, sample outputs, screenshots, short “why I built this” blurb for portfolio.

Phase 3
- Feedback loop, trend analysis, resume-to-JD matching, public demo.

---

## Example preference file (memory.yaml)

```yaml
preferred_titles:
  - trust and safety analyst
  - trust operations
  - threat intelligence
  - abuse investigator

exclude_keywords:
  - content moderator
  - bpo
  - night shift
  - vendor

preferred_companies:
  - GitHub
  - CrowdStrike
  - Stripe
  - Google
  - OpenAI

locations:
  - remote
  - india
  - global

min_fit_score: 75
```

---

## Sample job flow and sample output

1. Watcher obtains a new posting from a company career page.
2. Raw posting saved in SQLite.
3. Interpreter runs: sends description to the LLM prompt and saves structured output.
4. Matcher computes fit with the preference file.
5. If fit >= min_fit_score, Messenger sends immediate alert; otherwise it's included in daily digest.

Sample structured output (stored in DB):

```json
{
  "id": "job_20260101_001",
  "title": "Senior Trust & Safety Analyst",
  "company": "Security SaaS",
  "url": "https://careers.securitysaas/jobs/1234",
  "posted_date": "2026-01-30",
  "category": "Trust & Safety Ops",
  "seniority": "senior",
  "flags": {
    "vendor": false,
    "bpo": false,
    "moderation_language": false
  },
  "signals": ["telemetry-driven investigations", "cross-functional incident response"],
  "interpreter_score": 0.92,
  "fit_score": 0.91,
  "match_reason": "Strong overlap with abuse investigations + telemetry analysis. Seniority aligned. Security-first org."
}
```

Example email notification:

Subject: 🔥 High-fit role detected — Senior Trust & Safety Analyst @ Security SaaS (Fit: 91%)

Body:
- Company: Security SaaS
- Role: Senior Trust & Safety Analyst
- Score: 91%
- Why it matches: Telemetry-driven investigations, cross-functional response, no moderation language.
- Link: https://careers.securitysaas/jobs/1234

---

## LLM prompt template (Interpreter)

Goal: Given a job title and description, return a strict JSON object with category, seniority, flags, key signals, an interpreter confidence score (0–1), and a one-line human explanation.

System / Instruction (short):

- You are an expert Trust & Safety systems analyst. Given a job title and full description, classify the role and extract structured signals. Only output valid JSON conforming to the schema below. Do not include extra text or explanations.

Example JSON schema expected:

```json
{
  "category": "Trust & Safety Ops | Threat Intelligence | Abuse/Fraud | Policy/Governance | Safety Engineering",
  "seniority": "junior | mid | senior | lead | manager | director",
  "flags": {
    "vendor": true | false,
    "bpo": true | false,
    "moderation_language": true | false
  },
  "signals": ["telemetry", "investigations", "nation-state", "fraud-analytics"],
  "interpreter_score": 0.0,
  "explanation": "One-line reasoning for classification and score"
}
```

Prompt example (payload sent to the LLM):

```
Title: <job title>
Company: <company>
Location: <location>
Description: <full job description>

Return JSON that follows the schema exactly. interpreter_score should be a float between 0.0 and 1.0 representing confidence that this role fits into Trust & Safety as classified. explanation should be tight and domain-relevant.
```

Notes:
- Use temperature 0 and a response format enforcer (or schema validation) to ensure valid JSON.
- Post-process the LLM output: validate fields, clamp scores, and log low-confidence outputs for human review.

---

## Quickstart (MVP — local)

Requirements:
- Python 3.10+
- SQLite (local file)
- Optional: Playwright for JS-heavy career pages
- API key for an LLM provider (OpenAI-compatible or other)

Steps:
1. Clone the repo.
2. Create a virtualenv and install requirements.
3. Configure `memory.yaml` with your preferences.
4. Run the Watcher for a few seed companies (or use the provided sample scraper).
5. Run the Interpreter worker to classify unprocessed raw postings.
6. Run the Matcher / Messenger to send notifications.

Example minimal commands (placeholder):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python episko/watcher.py --companies seeds/companies.json
python episko/interpreter.py
python episko/messenger.py
```

---

## Folder structure (recommended)

- episko/
  - watcher.py        # Scrapers + scheduler that writes raw listings
  - interpreter.py    # LLM prompt wrapper and JSON validation
  - matcher.py        # Computes personal fit using memory.yaml
  - messenger.py      # Sends emails / Slack / Notion notifications
  - db.py             # DB helpers (SQLite)
  - config/
    - memory.yaml     # Personal preference file
    - companies.json  # Seed company career page list
  - tests/
- requirements.txt
- README.md

---

## Safety & ethics

- Respect robots.txt and terms of service for any site you scrape.
- Throttle requests to avoid abuse and IP blocking.
- When using LLMs, do not post personally identifiable information (PII) to public or shared models without redaction.

---

## Why I built this (short blurb)

EpiskoAI is for people who care about Trust & Safety but are tired of noise and low-context job alerts. It codifies domain knowledge—what makes a role truly Trust & Safety—so you spend time applying, not filtering.

---

## Next steps

- Decide the first 5–10 companies to seed the Watcher.
- Choose a datastore for the MVP (SQLite suggested).
- I can generate the repo scaffold and starter Python scripts for Watcher + Interpreter matched to this README.

---

## License

MIT
