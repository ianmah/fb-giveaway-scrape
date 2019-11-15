import re

f = open("bpgoing.txt", "r", encoding="utf8")

text = f.read()

text = re.sub("[\<].*?[\>]", " ", text)
text = re.sub("Remove", "", text)
text = re.sub("Invited by [a-zA-Z]* [a-zA-Z]*", "", text)
text = re.sub("    ", "", text)
text = re.sub("  ", "\n", text)

data = text.splitlines(True)
outFile = open("output.txt", "w", encoding="utf8")
outFile.writelines(data)

print(data)
