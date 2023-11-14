 passage = open("passage.txt", "r")
str_pass = passage.read()

lower_case = str_pass.lower()

lis = list(str_pass.split())

total_words = len(lis)
print("Total number of words:", total_words)

count_dict = {}

for char in lower_case:
    if char.isalpha():
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

print("Count of each alphabet:", count_dict)

ratio_dict = {}

for key, value in count_dict.items():
    ratio = "{:.2%}".format(value / total_words)
    ratio_dict[key] = ratio

print("Ratio of each alphabet:", ratio_dict)
