import streamlit as st
from duckduckgo_search import DDGS
import google.generativeai as genai
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

print("KEY:", os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key = st.secrets.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def search_web(query):
    sources = []
    content = []
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)
        for r in results:
            content.append(r["body"])

            sources.append({
                "title": r["title"],
                "url": r["href"]
            })
    return "\n".join(content), sources


def research_agent(topic):

    web_data, sources = search_web(topic)

    prompt = f"""
    Research the following topic:

    {topic}

    Information:
    {web_data}

    Create:
    1. Executive Summary
    2. Key Insights
    3. Challenges
    4. Future Directions
    """

    response = model.generate_content(prompt)
    print("Sources:", sources)
    return response.text, sources

st.title("AI Research Assistant")

topic = st.text_input("Enter Research Topic")

def create_pdf(report):
    filename = "research_report.pdf"
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = [
        Paragraph(report, styles["BodyText"])
    ]
    doc.build(elements)
    return filename

if st.button("Research"):
    report, sources = research_agent(topic)
    st.write(report)
    st.subheader("Sources")
    for source in sources:
        st.markdown(
            f"- [{source['title']}]({source['url']})"
        )
    pdf_file = create_pdf(report)
    with open(pdf_file, "rb") as f:
        st.download_button(
            label="Download PDF Report",
            data=f,
            file_name="research_report.pdf",
            mime="application/pdf"
        )

