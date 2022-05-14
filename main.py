import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

interview_question_url = "https://www.interviewbit.com/python-interview-questions/"
result = requests.get(url=interview_question_url)
result.raise_for_status()

soup = BeautifulSoup(result.text, 'html.parser')  # Soup
tag_h3_list = soup.find_all("h3")  # List with elements of Type 'bs4.element.Tag'
question_list = [str(question.get_text()) for question in tag_h3_list[3: len(tag_h3_list) - 1]]  # List
question_list = [question for question in question_list if question[0].isdigit()]  # Remove bad categorized <h3> text



pdf = FPDF()
pdf.add_font("Arial", "", "arial/arial.ttf", uni=True)
pdf.set_font("Arial", size=15)

for question in question_list:
    pdf.add_page()
    pdf.multi_cell(0, 5, txt=question, align="L")

pdf.output("Python-Interview-Questions.pdf").encode('latin-1', 'ignore')


