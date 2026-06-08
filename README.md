# AI Research Assistant

An AI-powered Research Assistant that autonomously gathers information from the web, analyzes it using Google's Gemini model, and generates structured research reports with key insights, challenges, and future directions.

## Features

* Web-based information retrieval using DuckDuckGo Search
* AI-generated research reports using Gemini 2.5 Flash
* Executive summaries and key insights
* Challenges and future research directions
* Source citation and reference listing
* PDF export functionality
* Interactive Streamlit user interface

## Tech Stack

* Python
* Streamlit
* Google Gemini API
* DuckDuckGo Search
* ReportLab

## Project Workflow

1. User enters a research topic.
2. The agent searches the web for relevant information.
3. Retrieved content is processed and summarized.
4. Gemini analyzes the information and generates a structured report.
5. Sources are displayed for transparency.
6. Users can download the report as a PDF.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/research-assistant.git
cd research-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a Google Gemini API key from Google AI Studio.

Set the environment variable:

### Windows

```cmd
set GOOGLE_API_KEY=your_api_key
```

### Linux/macOS

```bash
export GOOGLE_API_KEY=your_api_key
```

## Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## Example Output

The generated report includes:

* Executive Summary
* Key Insights
* Challenges
* Future Directions
* References

## Future Improvements

* Multi-agent workflow
* Research question generation
* Academic paper retrieval
* Citation generation in APA/IEEE formats
* Report history and storage
* Integration with vector databases for long-term memory

## Project Structure

```text
research-assistant/
│
├── app.py
├── requirements.txt
├── README.md
└── research_report.pdf
```

## Learning Outcomes

This project demonstrates:

* Large Language Model integration
* Tool-augmented AI agents
* Information retrieval workflows
* Prompt engineering
* Streamlit application development
* API integration
* Automated report generation

## Author

Manika Jain
