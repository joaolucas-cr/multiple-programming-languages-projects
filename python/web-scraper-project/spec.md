# Project 02 — Python Web Scraper
**Software Requirements Specification (SRS)**

Version: 1.0  
Language: Python 3.11+  
Difficulty: Beginner–Intermediate  
Development Methodology: Specification-Driven Development (SDD)

---

## 1. Project Overview

### 1.1 Purpose
Develop a command-line web scraping application capable of retrieving, parsing, validating, and storing publicly accessible website information.

The application must allow users to extract structured data from supported websites without manually copying information.

### 1.2 Scope
The initial implementation will target [Books to Scrape](https://books.toscrape.com/), a website designed for practicing web scraping.

The application will extract:
- Book title
- Price
- Availability
- Product URL
- Rating

The application must support pagination, persistent storage, error handling, and command-line configuration.

### 1.3 Out of Scope
- JavaScript-rendered websites
- Authentication and login
- CAPTCHA solving
- Proxy rotation
- Distributed scraping
- Graphical user interface
- Database servers

---

## 2. Business Rules (BR)

### BR-001 — Supported Websites
The system shall scrape only explicitly configured, publicly accessible websites.

**Acceptance Criteria:**
- Unsupported domains are rejected.
- Users cannot redirect the scraper to arbitrary domains.
- The initial supported domain is `books.toscrape.com`.

### BR-002 — Required Book Information
Each successfully extracted book record must contain:
- Title
- Price
- Availability
- Product URL
- Rating

**Acceptance Criteria:**
- Records missing required fields are rejected.
- Prices are stored as numeric values.
- Product URLs are stored as absolute URLs.

### BR-003 — Unique Records
Each book must be uniquely identified by its canonical product URL.

**Acceptance Criteria:**
- Duplicate URLs cannot create multiple records.
- Repeated scraping runs must not duplicate existing records.
- Existing records may be updated with newly scraped information.

### BR-004 — Price Validation
All extracted prices must be valid, nonnegative monetary amounts.

**Acceptance Criteria:**
- Negative prices are rejected.
- Invalid price strings are rejected.
- Prices are stored with two decimal places in the JSON output.
- The currency is recorded as GBP.

### BR-005 — Availability Normalization
Book availability must be normalized to a consistent representation.

**Allowed values:**
- `IN_STOCK`
- `OUT_OF_STOCK`

**Acceptance Criteria:**
- Raw website availability text is converted to the appropriate value.
- Unrecognized availability values cause record validation to fail.

### BR-006 — Rating Normalization
Ratings must be represented as integers from 1 to 5.

**Acceptance Criteria:**
- Written ratings such as `Three` are converted to `3`.
- Ratings outside the supported range are rejected.
- Missing ratings cause record validation to fail.

### BR-007 — Pagination Limits
Users must be able to configure the maximum number of pages processed.

**Acceptance Criteria:**
- The minimum page limit is 1.
- The default page limit is 1.
- The maximum configurable limit is 50.
- The scraper stops when the limit is reached or no next page exists.

### BR-008 — Responsible Scraping
The scraper must follow responsible request practices.

**Acceptance Criteria:**
- The scraper checks applicable `robots.txt` rules before scraping.
- The application does not bypass website access restrictions.
- A minimum delay of 1 second is enforced between requests.
- Requests use a descriptive User-Agent.
- HTTP 429 responses trigger termination of the current run rather than bypass attempts.

### BR-009 — Persistent Storage
Scraped records must remain available after the application terminates.

**Acceptance Criteria:**
- Results are saved in JSON format.
- Existing valid data is preserved when new records are added.
- Corrupted storage files are reported without silently overwriting them.
- Storage writes use a temporary file and replacement to reduce corruption risk.

### BR-010 — Data Consistency
All stored records must follow the same schema.

**Acceptance Criteria:**
- Every record has the same required fields.
- Prices, ratings, and availability use consistent formats.
- Records are validated before being saved.

### BR-011 — Error Isolation
A malformed book record must not terminate an otherwise valid scraping run.

**Acceptance Criteria:**
- Invalid records are skipped and counted.
- Errors are logged with sufficient context.
- Fatal errors, such as an inaccessible target website, terminate the run with a clear message.

### BR-012 — Scraping Summary
Every completed run must produce a summary of its execution.

**Required metrics:**
- Pages processed
- Books extracted
- New records saved
- Existing records updated
- Invalid records skipped
- Total execution time

---

## 3. Functional Requirements (FR)

### FR-001 — Command-Line Interface
The application shall provide a CLI through which users can initiate scraping operations.

Example:

`python main.py scrape --pages 5`

Supported commands:

| Command | Description |
|---|---|
| `scrape` | Start a scraping session |
| `list` | Display stored books |
| `search` | Search saved books by title |
| `stats` | Display dataset statistics |
| `export` | Export saved records to CSV |

### FR-002 — HTTP Retrieval
The system shall retrieve HTML documents using HTTP GET requests.

The system must:
- Configure a request timeout.
- Check HTTP response status codes.
- Reject unsupported content types.
- Handle connection failures.

### FR-003 — HTML Parsing
The system shall parse retrieved HTML using BeautifulSoup.

The parser must extract each required field from individual product listings.

### FR-004 — Pagination
The system shall identify and follow the website's next-page links until the configured limit is reached.

### FR-005 — Record Validation
The system shall validate extracted records according to BR-002, BR-004, BR-005, and BR-006.

### FR-006 — JSON Storage
The system shall serialize validated book records into a local JSON file.

### FR-007 — Search
Users shall be able to search saved books by title using case-insensitive partial matching.

Example:

`python main.py search "python"`

### FR-008 — Statistics
The system shall calculate:
- Total number of books
- Average price
- Minimum price
- Maximum price
- Number of in-stock books
- Number of out-of-stock books

### FR-009 — CSV Export
Users shall be able to export all saved records into a CSV file with a header row.

### FR-010 — Logging
The application shall log relevant events, including:
- Scraping start and completion
- HTTP failures
- Parsing failures
- Storage failures
- Skipped records

---

## 4. Non-Functional Requirements (NFR)

### NFR-001 — Maintainability
The application must separate networking, parsing, validation, storage, and CLI responsibilities.

### NFR-002 — Reliability
The application must preserve existing valid data if a scraping session fails.

### NFR-003 — Testability
Core validation, parsing, and storage logic must be independently testable without live network access.

### NFR-004 — Performance
For a local fixture containing 20 book listings, HTML parsing should complete within 1 second on a typical development computer, excluding network latency.

### NFR-005 — Security
The application must reject unsupported domains and must not execute downloaded scripts or HTML.

### NFR-006 — Portability
The application must run on Windows, macOS, and Linux with Python 3.11 or newer.

---

## 5. Data Model

### Entity: Book

| Field | Type | Constraints |
|---|---|---|
| `title` | string | Nonempty |
| `price` | string | Nonnegative decimal, two places |
| `currency` | string | `GBP` |
| `availability` | string | Defined enum |
| `rating` | integer | 1–5 |
| `url` | string | Unique absolute URL |

Example JSON record:

```json
{
  "title": "Example Book",
  "price": "25.99",
  "currency": "GBP",
  "availability": "IN_STOCK",
  "rating": 4,
  "url": "https://books.toscrape.com/catalogue/example_1/index.html"
}
```

Prices must be processed using decimal arithmetic rather than binary floating-point arithmetic.

---

## 6. Suggested Architecture

```text
web-scraper/
├── main.py
├── scraper.py
├── parser.py
├── validator.py
├── storage.py
├── models/
│   └── book.py
├── tests/
│   ├── test_parser.py
│   ├── test_validator.py
│   ├── test_storage.py
│   └── fixtures/
├── data/
│   └── books.json
├── requirements.txt
└── README.md
```

### Component Responsibilities

**main.py**
- Handle CLI arguments
- Coordinate application operations
- Display results

**scraper.py**
- Retrieve HTML
- Manage pagination
- Enforce request limits and delays

**parser.py**
- Extract book information
- Normalize website-specific HTML values

**validator.py**
- Enforce business rules
- Reject invalid records

**storage.py**
- Read and write JSON
- Prevent duplicates
- Export CSV

**models/book.py**
- Define the Book data structure

---

## 7. Acceptance Test Scenarios

### AC-001 — Successful Scraping
**Given** a valid supported webpage containing 20 valid books  
**When** the user executes the scrape command  
**Then** the application extracts and validates 20 records.

### AC-002 — Duplicate Prevention
**Given** 20 books already stored  
**When** the same 20 books are scraped again  
**Then** the total stored record count remains 20.

### AC-003 — Invalid Price
**Given** a book with price `INVALID`  
**When** the record is validated  
**Then** the record is rejected and the failure is logged.

### AC-004 — Pagination Limit
**Given** a website containing 10 pages  
**When** the user requests 3 pages  
**Then** the scraper processes no more than 3 pages.

### AC-005 — Network Failure
**Given** a network connection failure  
**When** the scraper attempts to retrieve a page  
**Then** an appropriate error is reported and existing stored data remains unchanged.

### AC-006 — Search
**Given** saved books containing the title `Learning Python`  
**When** the user searches for `python`  
**Then** the matching book is displayed.

### AC-007 — CSV Export
**Given** validated saved records  
**When** the user executes the export command  
**Then** a CSV file containing all records and column headers is generated.

### AC-008 — Corrupted Storage
**Given** a malformed JSON storage file  
**When** the application attempts to load records  
**Then** it reports a storage error without overwriting the file.

---

## 8. Development Milestones

### Milestone 1 — HTTP and HTML
Implement FR-002 and FR-003.

**Definition of Done:** Retrieve and parse one supported webpage.

### Milestone 2 — Data Extraction
Implement FR-005 and BR-002 through BR-006.

**Definition of Done:** Extract and validate complete book records.

### Milestone 3 — Persistence
Implement FR-006 and BR-003, BR-009, and BR-010.

**Definition of Done:** Save records to JSON and prevent duplicates.

### Milestone 4 — Pagination
Implement FR-004 and BR-007 through BR-008.

**Definition of Done:** Scrape multiple pages while respecting request limits.

### Milestone 5 — CLI Features
Implement FR-001 and FR-007 through FR-009.

**Definition of Done:** Scrape, list, search, calculate statistics, and export records.

### Milestone 6 — Testing and Reliability
Implement FR-010 and NFR-001 through NFR-006.

**Definition of Done:** All acceptance tests pass and the README documents installation and usage.

---

## 9. Project Completion Criteria

The project is considered complete when:

- All 12 business rules are implemented.
- All 10 functional requirements are implemented.
- All 6 non-functional requirements are satisfied.
- All 8 acceptance scenarios pass.
- The application can scrape multiple pages.
- Records persist correctly between runs.
- Repeated scraping does not introduce duplicates.
- All CLI commands work.
- The project includes automated tests and a README.

**Final Deliverable:** A fully functional Python CLI web scraper with structured JSON storage, CSV export, automated tests, and documented business rules.