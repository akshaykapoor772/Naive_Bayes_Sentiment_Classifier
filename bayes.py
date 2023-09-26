import math, os, pickle, re
import sys


class Bayes_Classifier:

   def __init__(self, trainDirectory = "training"):
      '''This method initializes and trains the Naive Bayes Sentiment Classifier.  If a 
      cache of a trained classifier has been stored, it loads this cache.  Otherwise, 
      the system will proceed through training.  After running this method, the classifier 
      is ready to classify input text.'''
      Working_directory = []
      for fFileObj in os.walk(os.getcwd()):
         Working_directory = fFileObj[2]
         break
      if 'negativedict.dat' and 'positivedict.dat' in Working_directory:
         self.positive = self.load('positivedict.dat')
         self.negative = self.load('negativedict.dat')
      else:
         print("Model training in progress...")
         self.train()
         print("System trained successfully, please rerun the program")
         sys.exit()


   def train(self):

      '''Trains the Naive Bayes Sentiment Classifier.'''
      IFileList = []
      positive = {}
      negative = {}
      dir = "review2/db_txt_files/"
      for fFileObj in os.walk(dir):
         IFileList = fFileObj[2]
         break
      for i in IFileList:
         new = i.split("-", 2)[1]
         if new == '1' or new == '2':
            str = self.loadFile(dir + i)
            finalstr = self.tokenize(str)
            for k in finalstr:
               if k not in negative:
                  negative.update({k : 0})
               else:
                  negative[k] += 1

         elif new == '4' or new == '5':
            str = self.loadFile(dir + i)
            finalstr = self.tokenize(str)
            for k in finalstr:
               if k not in positive:
                  positive.update({k: 0})
               else:
                  positive[k] += 1
      self.save(negative, "negativedict.dat")
      self.save(positive, "positivedict.dat")
      return negative, positive

   def classify(self, sText):
      '''Given a target string sText, this function returns the most likely document
      class to which the target string belongs. This function should return one of three
      strings: "positive", "negative" or "neutral".
      '''
      self.positivefinal = 0
      self.negativefinal = 0
      positivewords = sum(self.positive.values())
      negativewords = sum(self.negative.values())
      tokenized = self.tokenize(sText)
      for j in tokenized:

         word = j
         if word in self.positive:
            positiveprob = self.positive[j]/positivewords
            self.positivefinal += math.log1p(positiveprob) #To overcome Underflow
            #positive = positive*positiveprob '''Normal approach to claculate probability which arises the problem of underflow'''
         else:
            pass
         if word in self.negative:
            negativeprob = self.negative[j] / negativewords
            self.negativefinal += math.log1p(negativeprob) #To overcome Underflow
            #negative = negative * negativeprob '''Normal approach to claculate probability which arises the problem of underflow'''
         else:
            pass
      a = round(self.positivefinal, 4)
      b = round(self.negativefinal, 4)
      if a>b:
         return "positive"
      elif a==b:
         return "neutral"
      else:
         return "negative"


   def classifyfolder(self, directory):
      IFileList = []
      filecount = 0
      positivecount = 0
      negativecount = 0
      for fFileObj in os.walk(directory):
         IFileList = fFileObj[2]
         break
      for i in IFileList:
         filecount = filecount + 1
         word = i
         print(word)
         a = self.loadFile(directory + word)
         self.classify(a)
         new = word.split("-", 2)[1]
         if (new == '1' or new == '2') and (self.positivefinal<self.negativefinal):
            negativecount = negativecount+1
         elif (new == '4' or new == '5') and (self.positivefinal>self.negativefinal):
            positivecount = positivecount+1
      print("Total files passed to the model:", filecount)
      print("Correctly predicted positive:", positivecount)
      print("Correctly predicted negative:", negativecount)



   def loadFile(self, sFilename):
      '''Given a file name, return the contents of the file as a string.'''

      f = open(sFilename, "r", encoding="utf8")
      sTxt = f.read()
      f.close()
      return sTxt
   
   def save(self, dObj, sFilename):
      '''Given an object and a file name, write the object to the file using pickle.'''

      f = open(sFilename, "wb")
      p = pickle.Pickler(f)
      p.dump(dObj)
      f.close()
   
   def load(self, sFilename):
      '''Given a file name, load and return the object stored in the file.'''

      f = open(sFilename, "rb")
      u = pickle.Unpickler(f)
      dObj = u.load()
      f.close()
      return dObj

   def tokenize(self, sText): 
      '''Given a string of text sText, returns a list of the individual tokens that 
      occur in that string (in order).'''

      lTokens = []
      sToken = ""
      for c in sText:
         if re.match("[a-zA-Z0-9]", str(c)) != None or c == "\'" or c == "_" or c == '-':
            sToken += c
         else:
            if sToken != "":
               lTokens.append(sToken)
               sToken = ""
            if c.strip() != "":
               lTokens.append(str(c.strip()))
               
      if sToken != "":
         lTokens.append(sToken)

      return lTokens



