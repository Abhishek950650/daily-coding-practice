from collections import Counter

words = ["a", "b", "a", "c", "b", "a", "d", "b"]
word_freq = Counter(words)
# print(word_freq)
# print(word_freq.most_common(2))

# filtered = {word: count for word, count in word_freq.items() if count >=2 }
# print(filtered)

# filterd_list = [word for word, count, index in word_freq.items() if count >=2]
# print(filterd_list)

list_of_tuples = data = [("apple", 10), ("banana", 5), ("mango", 20)]

sorted_with_value_ass = sorted(list_of_tuples, key = lambda x : x[1])
print(sorted_with_value_ass)
sorted_with_value_dsc = sorted(list_of_tuples, key = lambda x : x[1], reverse=True)
print(sorted_with_value_dsc)
sorted_with_value = sorted(list_of_tuples)
print(sorted_with_value)

