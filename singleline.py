from bayes import Bayes_Classifier

exec(open("bayes.py").read())
bc = Bayes_Classifier()
print("Enter the sentence:")
a = input()
result = bc.classify(a)
print(result)
