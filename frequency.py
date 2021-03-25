def frequency(string):
    stringArray = string.split()
    words = set(stringArray)
    for word in words:
        print(word, " appears ", stringArray.count(word), " time")

testString = "input words you want to test into here"
frequency(testString)