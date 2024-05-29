revision of option1:

In this revised version, I've made the following changes:

I've combined the parse_capitals_xml and generate_quiz functions into a single script for simplicity.
I've used a list comprehension to create the capitals_list in the parse_capitals_xml function.
I've used the random.shuffle function to randomize the order of questions and options.
I've used the enumerate function to generate the question numbers.
I've used the chr function to generate the letter options.
I've used the copy function to avoid modifying the original list of capitals.
 I've added two sets: used_countries and used_capitals. These sets keep track of the countries and capitals that have already been used in the quiz. Before selecting a random country and capital, the code checks if the country and capital have already been used. If positive, it continues the loop and selects a new pair. This ensures that no wrong answers repeat within a file.