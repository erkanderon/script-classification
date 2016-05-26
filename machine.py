import os
import string
input = raw_input("Please Type your arff file (For Example sonuc.arff):")
os.system("echo "+ input)

print "Data Preprocessing"
os.system("java -cp weka-3-8-0/weka.jar weka.filters.unsupervised.attribute.NumericToNominal -R first-last -i try.arff > "+input)
print "Classify Time"

def get_result(command):
    comm = os.popen(command)
    filt = filter(lambda x: 'Correctly Classified Instances' in x, comm)
    splitted = [word.strip(string.punctuation) for word in filt[1].split()]
    cci = splitted[4]
    return cci

rc = get_result("java -cp weka-3-8-0/weka.jar weka.classifiers.meta.RandomCommittee -t "+ input+" -c 1")
print "Correctly Classified Instance RandomCommittee: " + "%" + rc
j48 = get_result("java -cp weka-3-8-0/weka.jar weka.classifiers.trees.J48 -t "+ input +" -c 1")
print "Correctly Classified Instance J48: " + "%" + j48
rep = get_result("java -cp weka-3-8-0/weka.jar weka.classifiers.trees.REPTree -t "+ input +" -c 1")
print "Correctly Classified Instance REPTree: " + "%" + rep
dt = get_result("java -cp weka-3-8-0/weka.jar weka.classifiers.rules.DecisionTable -t "+ input +" -c 1")
print "Correctly Classified Instance DecisionTable: " + "%" + dt
print "SMO function can takes some time please wait.."
smo = get_result("java -cp weka-3-8-0/weka.jar weka.classifiers.functions.SMO -t "+ input +" -c 1")
print "Correctly Classified Instance SMO: " + "%" + smo

while True:
    choose = int(raw_input("Choose a number to see output: \n"+"0-Exit \n"+ "1-RandomCommittee \n" +"2-J48 \n"+"3-REPTree\n"+"4-Decision Table \n"+"5-SMO \n" ))

    if choose==1:
        os.system("java -cp weka-3-8-0/weka.jar weka.classifiers.meta.RandomCommittee -t "+ input+ " -c 1")
    elif choose==2:
        os.system("java -cp weka-3-8-0/weka.jar weka.classifiers.trees.J48 -t "+input+" -c 1")
    elif choose==3:
        os.system("java -cp weka-3-8-0/weka.jar weka.classifiers.trees.REPTree -t "+ input +" -c 1")
    elif choose==4:
        os.system("java -cp weka-3-8-0/weka.jar weka.classifiers.rules.DecisionTable -t "+ input +" -c 1")
    elif choose==5:
        os.system("java -cp weka-3-8-0/weka.jar weka.classifiers.functions.SMO -t "+ input +" -c 1")
    elif choose==0:
        break
    else:
        print "You have a bad input"


#b = os.popen('java -cp weka-3-8-0/weka.jar weka.classifiers.bayes.NaiveBayes -t sonuc.arff -c 1').readlines()
#c = filter(lambda x: 'Correctly Classified Instances' in x, b)
#print c[1]
#cci = [word.strip(string.punctuation) for word in c[1].split()]
#print cci[4]
##Needs to be run
##java -cp Downloads/weka-3-8-0/weka.jar weka.filters.unsupervised.attribute.NumericToNominal -R first-last -i Desktop/Applied\ Machine\ Learning/try.arff > Desktop/Applied\ Machine\ Learning/sonuc.arff
##java -cp Downloads/weka-3-8-0/weka.jar weka.classifiers.bayes.NaiveBayes -t Desktop/Applied\ Machine\ Learning/sonuc.arff -c 1

##NumericToNominal
##A filter for turning numeric attributes into nominal ones. Unlike discretization,
##it just takes all numeric values and adds them to the list of nominal values of that attribute.
##Useful after CSV imports,
##to enforce certain attributes to become nominal, e.g., the class attribute, containing values from 1 to 5.
