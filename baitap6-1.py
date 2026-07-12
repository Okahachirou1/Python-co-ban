text = "iPhone 17 là điện thoại mới của Apple iPhone 17 có camera đẹp iPhone 17 có pin tốt"
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f"{word}: {count}")