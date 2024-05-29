import random
import xml.etree.ElementTree as ET

# Constants
NUM_QUIZZES = 10
NUM_QUESTIONS_PER_QUIZ = 10
XML_FILE = "european_capitals.xml"


# Function to parse the XML file and return a list of countries and capitals
def parse_capitals_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    capitals_list = [
        (country.get("name"), country.text) for country in root.findall("country")
    ]
    return capitals_list


# Function to generate a quiz file
def generate_quiz(quiz_num, capitals_list):
    filename = f"european_capitals_quiz_{quiz_num + 1}.txt"
    random.shuffle(capitals_list)
    # to avoid repeating the same country and capital
    used_countries = set()
    used_capitals = set()

    with open(filename, "w") as file:
        file.write(f"European Capitals Quiz {quiz_num + 1}\n\n")

        for question_num in range(NUM_QUESTIONS_PER_QUIZ):
            while True:
                country, capital = random.choice(capitals_list)
                if country not in used_countries and capital not in used_capitals:
                    break

            used_countries.add(country)
            used_capitals.add(capital)
            # to avoid repeating the same incorrect answer
            incorrect_answers = [
                value
                for key, value in capitals_list
                if key != country and value not in used_capitals
            ]
            options = [capital] + random.sample(incorrect_answers, 2)
            random.shuffle(options)

            file.write(f"{question_num + 1}. What is the capital of {country}?\n")
            for i, option in enumerate(options):
                file.write(f"   {chr(65 + i)}. {option}\n")
            file.write("\n")

    print(f"European Capitals Quiz {quiz_num + 1} has been created.")


# Main function to generate quizzes
def main():
    capitals_list = parse_capitals_xml(XML_FILE)
    for quiz_num in range(NUM_QUIZZES):
        generate_quiz(quiz_num, capitals_list.copy())
    print("All quizzes have been created.")


# Run the main function
if __name__ == "__main__":
    main()
