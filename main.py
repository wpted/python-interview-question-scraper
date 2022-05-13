import requests
from bs4 import BeautifulSoup

interview_question_url = "https://www.interviewbit.com/python-interview-questions/"
result = requests.get(url=interview_question_url)
result.raise_for_status()

soup = BeautifulSoup(result.text, 'html.parser')  # Soup
tag_h3_list = soup.find_all("h3")  # List with elements of Type 'bs4.element.Tag'
question_list = [str(question.get_text()) for question in tag_h3_list[3: len(tag_h3_list) - 1]]  # List


def main():
    for question in question_list:
        print(question)


if __name__ == '__main__':
    main()
