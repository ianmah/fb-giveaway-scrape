import re

# This script takes an HTML element of facebook comments and creates output.txt
# with TAGGER+TAGGED_ID+TAGGED COMMENT data
# ie Angela Chang+100001245425506+Johnny Kim

f = open("data2.txt", "r", encoding="utf8")

text = f.read()


# clearreact = "[1-9]</span>"
# text = re.sub(clearreact, "</span>", text)

regex = "(?!<a class=\"\" data-hovercard=\"\/ajax\/hovercard\/user\.php\?id=)[\<].*?[\>]"
regex2 = "<a class=\"\" data-hovercard=\"/ajax/hovercard/user.php\?"
regex3 = "\" href=\".*?\">"

text = re.sub(regex, " ", text)
text = re.sub(regex2, " ", text)

text = re.sub(regex3, "+", text)

text = re.sub("&nbsp;", "", text)
text = re.sub("·", "", text)
text = re.sub("Show more reactions", "", text)
text = re.sub("Delete or hide this", "", text)
text = re.sub("Like", "", text)
text = re.sub("Message", "\n", text)
text = re.sub("[1-9]h", "", text)
text = re.sub("10h", "", text)
text = re.sub("[1-9]d", "", text)
text = re.sub("[1-99]m", "", text)
text = re.sub("Active Now", "", text)
text = re.sub(" [1-9]{1,4} ", "", text)
text = re.sub("Viewmore reply", "", text)
text = re.sub("Viewmore replies", "", text)
text = re.sub("Reply", "", text)
text = re.sub("  ", " ", text)
text = re.sub("  ", " ", text)
text = re.sub("  ", " ", text)
text = re.sub("  ", " ", text)
text = re.sub("  ", " ", text)
text = re.sub("  ", " ", text)

text = re.sub(" id=", "+", text)

text = re.sub("\n ", "\n", text)
text = re.sub("﻿ Comments ", "", text)

data = text.splitlines(True)
data = data[:-1]
outFile = open("output.txt", "w", encoding="utf8")
outFile.writelines(data)

print(data)
