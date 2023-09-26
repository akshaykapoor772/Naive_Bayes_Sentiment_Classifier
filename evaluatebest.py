import os
from bayesbest import Bayes_Classifier

testFile = "bayesbest.py"
trainDir = "training/"
testDir = "testing/"
negativecount = 0
positivecount = 0
filecount = 0
exec(open(testFile).read())
bc = Bayes_Classifier(trainDir)

iFileList = []

for fFileObj in os.walk(testDir + "/"):
    iFileList = fFileObj[2]
    break
print('%d test reviews.' % len(iFileList))

results = {"negative": 0, "neutral": 0, "positive": 0}

print("\nFile Classifications:")
for filename in iFileList:
    filecount = filecount + 1
    fileText = bc.loadFile(testDir + filename)
    result = bc.classify(fileText)
    print("%s: %s" % (filename, result))
    results[result] += 1
    new = filename.split("-", 2)[1]
    if (new == '1' or new == '2') and (bc.positivefinal < bc.negativefinal):
        negativecount = negativecount + 1
    elif (new == '4' or new == '5') and (bc.positivefinal > bc.negativefinal):
        positivecount = positivecount + 1
print("\nResults Summary:")
for r in results:
    print("%s: %d" % (r, results[r]))
print("Total files passed to the model:", filecount)
print("Correctly predicted positive:", positivecount)
print("Correctly predicted negative:", negativecount)


