text = "X-DSPAM-Confidence:    0.8475"
a = text.find(' ')
b = text[a+1:]
c = b.lstrip()
print(float(c))
