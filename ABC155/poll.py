N = int(input())

count = 0
words_dict = {}
top_words = []

for i in range(N):
    word = input()

    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

    if words_dict[word] == count:
        top_words.append(word)
    if words_dict[word] > count:
        top_words = [word]
        count += 1

for word in sorted(top_words):
    print(word)
