# Answers
1. Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file. Write in any programming language (preferably in Python) - make any assumptions, but remember to state them.

In this program, we define two main functions:

calculate_profanity_degree(tweet, racial_slurs): This function takes a tweet and the set of racial slurs as input. It removes non-alphanumeric characters, converts the tweet to lowercase, and splits it into individual words. It then counts the number of racial slurs present in the tweet and calculates the profanity degree as a percentage of racial slurs to total words. The profanity degree is returned.

analyze_tweets(file_path, racial_slurs): This function reads the file containing the Twitter tweets line by line. It strips each line to remove leading/trailing whitespace and passes the tweet along with the set of racial slurs to the calculate_profanity_degree function. It then prints the tweet and the corresponding profanity degree.


2. Which is an interesting data set you discovered recently? Why is it your favorite? No datasets on Kaggle, please.

One interesting data set I recently discovered is the "Open Images Dataset V6" released by Google. It is one of the largest publicly available image datasets, containing millions of labeled images across a wide range of categories. Here's why it is one of my favorites:

1. Scale and Diversity: The Open Images Dataset V6 comprises over 9 million images with annotations for 6,000+ object categories, making it an incredibly large and diverse data set. This scale and diversity offer ample opportunities for training and evaluating machine learning models across various domains.

2. Annotations and Labels: The data set includes rich annotations such as bounding boxes, object segmentation masks, and visual relationships. These annotations make it valuable for tasks like object detection, instance segmentation, and visual understanding.

3. Data Quality and Consistency: Google has put significant effort into ensuring data quality and consistency in the dataset. The images are sourced from various online platforms, and a thorough annotation process has been followed to maintain high-quality labels.

4. Research and Benchmarking: Due to its size and comprehensive annotations, the Open Images Dataset V6 has become a popular choice for research and benchmarking in the computer vision community. Many state-of-the-art models and techniques have been trained and evaluated on this dataset, allowing for meaningful comparisons and advancements.

5. Open and Accessible: The dataset is openly available for download and usage, enabling researchers, students, and developers to access a large-scale image dataset without restrictions. This openness fosters collaboration, innovation, and the democratization of computer vision research.

While Kaggle hosts numerous excellent datasets, the Open Images Dataset V6 stands out due to its size, diversity, quality, and the impact it has had on advancing computer vision research and applications.

3. This question is to test your aptitude for writing small shell scripts on Unix. You are given this URL amfiindia.com/spages/NAVAll.txt
Write a shell script that extracts the Scheme Name and Asset Value fields only and saves them in a csv file.

Here's how the script works:

The script starts by setting the URL (amfiindia.com/spages/NAVAll.txt) and the desired output file name (scheme_data.csv).

It uses the curl command to fetch the data from the given URL and saves it to a temporary file (temp_file).

The awk command is used to extract the Scheme Name (field 4) and Asset Value (field 5) from each line of the temporary file. The fields are separated by semicolons (;). The extracted fields are then saved to the output file (output_file), with each field separated by a comma (,) to form a CSV format.

Finally, the script cleans up by removing the temporary file and displays a message indicating the completion of the extraction process, along with the name of the generated CSV file.

To run the script, save it to a file (e.g., extract_scheme_data.sh), make it executable (chmod +x extract_scheme_data.sh), and execute it (./extract_scheme_data.sh). The extracted Scheme Name and Asset Value fields will be saved in the scheme_data.csv file.







