import random
import xml.etree.ElementTree as ET

# Constants
NUM_QUIZZES = 10
NUM_QUESTIONS_PER_QUIZ = 10
XML_FILE = 'european_capitals.xml'

# Function to parse the XML file and return a list of countries and capitals
def parse_capitals_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    capitals_list = []
    for country in root.findall('country'):
        name = country.get('name')
        capital = country.text
        capitals_list.append((name, capital))
    return capitals_list

# Function to generate a quiz file
def generate_quiz(quiz_num, capitals_list):
    filename = f"european_capitals_quiz_{quiz_num + 1}.txt"
    random.shuffle(capitals_list)  # Randomize the order of questions

    with open(filename, 'w') as file:
        file.write(f"European Capitals Quiz {quiz_num + 1}\n\n")

        for question_num in range(NUM_QUESTIONS_PER_QUIZ):
            country, capital = capitals_list[question_num]
            # Generate incorrect answers by picking two other capitals
            incorrect_answers = [value for key, value in capitals_list if key != country and value != capital]
            options = [capital] + random.sample(incorrect_answers, 2)
            random.shuffle(options)

            # Write the question and answers to the file
            file.write(f"{question_num + 1}. What is the capital of {country}?\n")
            for i, option in enumerate(options):
                file.write(f"   {chr(65 + i)}. {option}\n")
            file.write("\n")

    print(f"European Capitals Quiz {quiz_num + 1} has been created.")

# Main function to generate quizzes
def main():
    capitals_list = parse_capitals_xml(XML_FILE)
    for quiz_num in range(NUM_QUIZZES):
        generate_quiz(quiz_num, capitals_list.copy())  # Pass a copy to avoid modifying the original list
    print("All quizzes have been created.")

# Run the main function
if __name__ == "__main__":
    main()
