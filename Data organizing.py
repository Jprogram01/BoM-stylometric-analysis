import re
import nltk
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter

file_path = "BoM.txt"  # Path to your file
speakers_with_verse = {}
authors_with_verse = {}
# Open the file in read mode
with open(file_path, "r", encoding="utf-8") as file:
    # Iterate over each line in the file
    iterator = 0
    for line in file:
        iterator += 1
        # Process each line as needed
        line = line.replace("(", "( ")
        line = line.replace("\t", " ")
        line = line.replace("\n`", " ")
        line = line.replace("\xa0", " ")
        line = line.strip()
        line_split = line.split(" ")
        if line_split[0] == "(" or len(line_split) == 1:
            for i in range(len(line_split)):
                if len(line_split) == 1:
                    name = line
                    if name == "":
                        print("")
                    break
                elif line_split[i] == ")":
                    name = line_split[i + 1:]
                    name = " ".join(name).lower()
                    if name == "":
                        print("")
                    break
        elif  ":" in line:
            if name not in speakers_with_verse:
                    speakers_with_verse[name] = []
            if "THE BOOK OF" not in line:
                speakers_with_verse[name].append((line, line))
        if line_split[0] == "(" or len(line_split) == 1:
            for i in range(len(line_split)):
                if len(line_split) == 1:
                    name = line
                    name = name.lower()
                    if name == "":
                        print("")
                    break
                elif line_split[i] == ")":
                    name = line_split[1]
                    name = name.lower()
                    if name == "":
                        print("")
                    break
        elif ":" in line:
            if name not in authors_with_verse:
                    authors_with_verse[name] = []
            if "THE BOOK OF" not in line:
                authors_with_verse[name].append((line, line))
            # match = re.search(scripture_pattern, line)
            # if match:
            #     scripture_ref = match.group(0).strip()
            #     sentence = line[match.end():].strip()
            #     if name not in speakers_with_verse:
            #         speakers_with_verse[name] = []
            #         if "THE BOOK OF" not in sentence:
            #             speakers_with_verse[name].append((scripture_ref, sentence))
            #     else:
            #         if "THE BOOK OF" not in sentence:
            #             speakers_with_verse[name].append((scripture_ref, sentence))
#speakers_with_verse['JAROM'] = speakers_with_verse.pop('JARED₂')


count = 0
stop_words = set(stopwords.words('english'))
symbols = set(punctuation)


speakers_word_freq = {}
authors_word_freq = {}
for author, verses in speakers_with_verse.items():
    # Combine all verses into a single string for the author
        author_text = " ".join(verse[1] for verse in verses)
        
        # Tokenize the text
        tokens = word_tokenize(author_text)
        
        # Lowercase all tokens for case-insensitive analysis
        tokens = [token.lower() for token in tokens if token.lower() not in symbols]
        
        # Filter out stop words and symbols
        tokens = [token for token in tokens if token not in stop_words]
        
        # Count the frequency of each word
        word_freq = Counter(tokens)
        
        # Store word frequencies for the author
        speakers_word_freq[author] = word_freq
for author, verses in authors_with_verse.items():
    # Combine all verses into a single string for the author
        author_text = " ".join(verse[1] for verse in verses)
        
        # Tokenize the text
        tokens = word_tokenize(author_text)
        
        # Lowercase all tokens for case-insensitive analysis
        tokens = [token.lower() for token in tokens if token.lower() not in symbols]
        
        # # Filter out stop words and symbols
        tokens = [token for token in tokens if token not in stop_words]
        
        # Count the frequency of each word
        word_freq = Counter(tokens)
        
        # Store word frequencies for the author
        authors_word_freq[author] = word_freq
for author, word_freq in speakers_word_freq.items():
    print(f"\nWord frequencies for {author}:")
    for word, freq in word_freq.most_common(5):
        print(f"{word}: {freq}")
for author, word_freq in authors_word_freq.items():
    print(f"\nWord frequencies for {author}:")
    for word, freq in word_freq.most_common(5):
        print(f"{word}: {freq}")


authors_word_variance = {}
speakers_word_variance = {}
# Iterate over each author's word frequencies
for author, word_freq in speakers_word_freq.items():
    # Extract word frequencies
    word_frequencies = np.array(list(word_freq.values()))
    
    # Calculate variance of word frequencies
    variance = np.var(word_frequencies)
    
    # Store word variance for the author
    speakers_word_variance[author] = variance

# Iterate over each author's word frequencies
for author, word_freq in authors_word_freq.items():
    # Extract word frequencies
    word_frequencies = np.array(list(word_freq.values()))
    
    # Calculate variance of word frequencies
    variance = np.var(word_frequencies)
    
    # Store word variance for the author
    authors_word_variance[author] = variance


total = 0
average_count = 0
for key, value in speakers_word_freq.items():
     average_count += 1
     total += len(value)
average = total / average_count
print(average)
note_worthy_speakers = []
# for key, value in speakers_word_freq.items():
#      note_worthy_speakers.append(key) if len(value) > 250 else None
# for author, variance in authors_word_variance.items():
#     if author in note_worthy_speakers:
#         speakers_word_freq[author]
#         print(f"Word variance for {author}: {variance}, word count: {len(speakers_word_freq[author])} ")

for author, variance in authors_word_variance.items():
        print(f"Word variance for {author}: {variance}, word count: {len(authors_word_freq[author])} ")
     