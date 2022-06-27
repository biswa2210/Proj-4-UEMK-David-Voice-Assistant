import random
import json
import torch
from CentralPoint import Brain
from NeuralNetwork import bag_of_words, tokenize


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("emotions.json", 'r') as json_data:
    emotions = json.load(json_data)


FILE = "Model.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = Brain(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-----------------------

NAME = "David"
from Tasks import NonInputExe
from Tasks import InputExe
from NCS_PART_1 import NCS_1
from ALGOS_PART1 import  ALGOS_1
from NCS_PART_2 import NCS_2
from Listen import takeCommand
from say import speak,wish
from ALGOS_PART2 import ALGOS_2
from techniqaltalks import Tt
from casualtalks import Ct
from AdditionalFunctionality import addition,multiplication,substraction,division,pascaltriangle
def Main():
    sentence = takeCommand()
    result = str(sentence)

    if "quit" in sentence:
        exit()
    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]
    
    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for emotion in emotions['emotions']:
            if tag == emotion["tag"]:
                reply = random.choice(emotion["responses"])
                #-------------------Added By Pati
                if "time" in reply:
                    NonInputExe(reply)
                elif "date" in reply:
                    NonInputExe(reply)
                elif "day" in reply:
                    NonInputExe(reply)
                elif "wikipedia" in reply:
                    InputExe(reply,result)
                elif "google" in reply:
                    InputExe(reply,result)
                elif "youtube" in reply:
                    InputExe(reply,result)
                elif "maps" in reply:
                    InputExe(reply,result)
                elif "open" in reply:
                    InputExe(reply,result)
                elif "temperature" in reply:
                    InputExe(reply,result)
                elif "alarm" in reply:
                    InputExe(reply,result)
                elif "shutdown" in reply:
                    NonInputExe(reply)
                elif "restart" in reply:
                    NonInputExe(reply)
                elif "lockscreen" in reply:
                    NonInputExe(reply)
                elif "countdown" in reply:
                    InputExe(reply, result)
                # casual talks By Ankita--------->
                elif "hbd" in reply:
                    Ct(reply, result)
                elif "morning" in reply:
                    Ct(reply, result)
                elif "afternoon" in reply:
                    Ct(reply, result)
                elif "evening" in reply:
                    Ct(reply, result)
                elif "night" in reply:
                    Ct(reply, result)
                elif "movie" in reply:
                    Ct(reply, result)
                elif "stop" in reply:
                    Ct(reply, result)
                elif "webseries" in reply:
                    Ct(reply, result)
                elif "tvshow" in reply:
                    Ct(reply, result)
                elif "drink" in reply:
                    Ct(reply, result)
                elif "loveyou" in reply:
                    Ct(reply, result)
                elif "game" in reply:
                    Ct(reply, result)
                elif "covid" in reply:
                    Ct(reply, result)
                elif "india" in reply:
                    Ct(reply, result)
                elif "programming" in reply:
                    Ct(reply, result)
                elif "food" in reply:
                    Ct(reply, result)
                elif "cs" in reply:
                    Ct(reply, result)
                elif "ott" in reply:
                    Ct(reply, result)
                elif "actor" in reply:
                    Ct(reply, result)
                elif "book" in reply:
                    Ct(reply, result)
                elif "company" in reply:
                    Ct(reply, result)
                elif "subject" in reply:
                    Ct(reply, result)
                elif "music" in reply:
                    Ct(reply, result)
                elif "sport" in reply:
                    Ct(reply, result)
                elif "festival" in reply:
                    Ct(reply, result)
                # techinical talks by Ankita--->
                elif "key" in reply:
                    Tt(reply, result)
                elif "python" in reply:
                    Tt(reply, result)
                elif "java" in reply:
                    Tt(reply, result)
                elif "html" in reply:
                    Tt(reply, result)
                elif "aiml" in reply:
                    Tt(reply, result)
                elif "js" in reply:
                    Tt(reply, result)
                elif "android" in reply:
                    Tt(reply, result)
                elif "kotlin" in reply:
                    Tt(reply, result)
                elif "sql" in reply:
                    Tt(reply, result)
                elif "flutter" in reply:
                    Tt(reply, result)
                elif "bootstrap" in tag:
                    Tt(reply, result)
                elif "firebase" in reply:
                    Tt(reply, result)
                elif "mongodb" in reply:
                    Tt(reply, result)
                elif "sass" in reply:
                    Tt(reply, result)
                elif "netlify" in tag:
                    Tt(reply, result)
                elif "github" in reply:
                    Tt(reply, result)
                elif "drone" in reply:
                    Tt(reply, result)
                elif "deep" in reply:
                    Tt(reply, result)
                elif "ar" in reply:
                    Tt(reply, result)
                elif "vr" in reply:
                    Tt(reply, result)
                elif "dbms" in reply:
                    Tt(reply, result)
                elif "api" in reply:
                    Tt(reply, result)
                elif "dsa" in reply:
                    Tt(reply, result)
                elif "btree" in reply:
                    Tt(reply, result)
                elif "tran" in reply:
                    Tt(reply, result)
                elif "mine" in reply:
                    Tt(reply, result)
                elif "block" in reply:
                    Tt(reply, result)
                elif "nlp" in reply:
                    Tt(reply, result)
                elif "link" in reply:
                    Tt(reply, result)
                elif "matrix" in reply:
                    Tt(reply, result)
                elif "hash" in reply:
                    Tt(reply, result)
                elif "numpy" in reply:
                    Tt(reply, result)
                elif "pandas" in reply:
                    Tt(reply, result)
                elif "gui" in reply:
                    Tt(reply, result)
                elif "tensorflow" in reply:
                    Tt(reply, result)
                elif "file" in reply:
                    Tt(reply, result)
                elif "poly" in reply:
                    Tt(reply, result)
                elif "xml" in reply:
                    Tt(reply, result)
                elif "regret" in reply:
                    Tt(reply, result)
                elif "ann" in reply:
                    Tt(reply, result)
                elif "bloom" in reply:
                    Tt(reply, result)
                elif "spatial" in reply:
                    Tt(reply, result)
                elif "view" in reply:
                    Tt(reply, result)
                elif "flash" in reply:
                    Tt(reply, result)
                elif "dead" in reply:
                    Tt(reply, result)
                elif "entity" in reply:
                    Tt(reply, result)
                elif "dml" in reply:
                    Tt(reply, result)
                elif "attribute" in reply:
                    Tt(reply, result)
                elif "ddl" in reply:
                    Tt(reply, result)
                elif "dba" in reply:
                    Tt(reply, result)
                elif "jdbc" in reply:
                    Tt(reply, result)
                elif "normal" in tag:
                    Tt(reply, result)
                elif "object" in tag:
                    Tt(reply, result)
                elif "class" in tag:
                    Tt(reply, result)
                #---NCS_1--->by Ankita
                elif "evenOddCheck" in reply:
                    NCS_1(reply, result)
                elif "primecheck" in reply:
                    NCS_1(reply, result)
                elif "proniccheck" in reply:
                    NCS_1(reply, result)
                elif "automorphiccheck" in reply:
                    NCS_1(reply, result)
                elif "neoncheck" in reply:
                    NCS_1(reply, result)
                elif "buzzcheck" in reply:
                    NCS_1(reply, result)
                elif "negativecheck" in reply:
                    NCS_1(reply, result)
                elif "amicablecheck" in reply:
                    NCS_1(reply, result)
                elif "strongcheck" in reply:
                    NCS_1(reply, result)
                elif "spycheck" in reply:
                    NCS_1(reply, result)
                elif "uglycheck" in reply:
                    NCS_1(reply, result)
                elif "positivecheck" in reply:
                    NCS_1(reply, result)
                # ------------>
                # ---NCS_2--->by Rahul
                elif "amstrong" in reply:
                    NCS_2(reply, result)
                elif "happy" in reply:
                    NCS_2(reply, result)
                elif "magic" in reply:
                    NCS_2(reply, result)
                elif "perfect" in reply:
                    NCS_2(reply, result)
                elif "palindrome" in reply:
                    NCS_2(reply, result)
                elif "smith" in reply:
                    NCS_2(reply, result)
                elif "duck" in reply:
                    NCS_2(reply, result)
                elif "strong" in reply:
                    NCS_2(reply, result)
                elif "composite" in reply:
                    NCS_2(reply, result)
                elif "harshad" in reply:
                    NCS_2(reply, result)

                # ------------>
                #---ALGOS_1--->by Subhadip
                elif "algoLinearSearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoJumpSearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoInterpolationSearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoBinarySearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoExponentialSearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoSublistSearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoFibonacciSearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoKSearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoUbiquitousBinarySearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoAStarSearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoBreadtheFirstSearch" in reply:
                    ALGOS_1(reply, result)
                elif "algoDepthFirstSearch" in reply:
                    ALGOS_1(reply, result)

                    # Algos1.2-->Sorting Algorithms-->by Subhadip
                elif "algoBubbleSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoSelectionSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoQuickSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoInsertionSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoMergeSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoHeapSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoCountingSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoRadixSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoBucketSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoCombSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoTimSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoCycleSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoBitonicSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoSleepSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoCoctailSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoStrandSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoShellSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoTreeSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoPermutationSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoPancakeSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoGnomeSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoBrickSort" in reply:
                    ALGOS_1(reply, result)
                elif "algoPegionholeSort" in reply:
                    ALGOS_1(reply, result)
                #------------>
                # ---ALGOS_2--->by Arijit
                elif "algoDijkstra" in reply:
                    ALGOS_2(reply, result)
                elif "algoFloydWarshall" in reply:
                    ALGOS_2(reply, result)
                elif "algoAstar" in reply:
                    ALGOS_2(reply, result)
                elif "algoBFS" in reply:
                    ALGOS_2(reply, result)
                elif "algoDFS" in reply:
                    ALGOS_2(reply, result)
                elif "algoGreedy" in reply:
                    ALGOS_2(reply, result)
                elif "algoHuffman" in reply:
                    ALGOS_2(reply, result)
                elif "algoBitwise" in reply:
                    ALGOS_2(reply, result)
                elif "algoGraph" in reply:
                    ALGOS_2(reply, result)
                elif "algoRandomized" in reply:
                    ALGOS_2(reply, result)
                elif "algoKarger" in reply:
                    ALGOS_2(reply, result)
                elif "algoHamiltonianCycle" in reply:
                    ALGOS_2(reply, result)
                elif "algoFleury" in reply:
                    ALGOS_2(reply, result)
                elif "algoEulerianPath" in reply:
                    ALGOS_2(reply, result)
                elif "algoTarjan" in reply:
                    ALGOS_2(reply, result)
                elif "algoTransitiveClosure" in reply:
                    ALGOS_2(reply, result)
                elif "algoBiconnectedGraph" in reply:
                    ALGOS_2(reply, result)
                elif "algoJohnson" in reply:
                    ALGOS_2(reply, result)
                elif "algoBellmanFord" in reply:
                    ALGOS_2(reply, result)
                elif "algoFordFulkerson" in reply:
                    ALGOS_2(reply, result)
                elif "algoHopcroftKarp" in reply:
                    ALGOS_2(reply, result)
                elif "algoBoruvka" in reply:
                    ALGOS_2(reply, result)
                elif "algoKaratsuba" in reply:
                    ALGOS_2(reply, result)
                elif "algoFloodFill" in reply:
                    ALGOS_2(reply, result)
                elif "algoKruskal" in reply:
                    ALGOS_2(reply, result)
                elif "algoTopologicalSort" in reply:
                    ALGOS_2(reply, result)
                elif "algoPrims" in reply:
                    ALGOS_2(reply, result)
                elif "algoKSmallest" in reply:
                    ALGOS_2(reply, result)
                elif "algoStrassen" in reply:
                    ALGOS_2(reply, result)
                elif "algoCooleyTukeyFFT" in reply:
                    ALGOS_2(reply, result)
                elif "algoDivideAndConquer" in reply:
                    ALGOS_2(reply, result)
                elif "algoChineseRemainder" in reply:
                    ALGOS_2(reply, result)
                elif "algoAmicablePair" in reply:
                    ALGOS_2(reply, result)
                elif "algoBrent" in reply:
                    ALGOS_2(reply, result)
                elif "algoReverseDelete" in reply:
                    ALGOS_2(reply, result)
                elif "algoEdmonds" in reply:
                    ALGOS_2(reply, result)
                # ------------>
                elif "addition" in reply:
                    addition()
                elif "substraction" in reply:
                    substraction()
                elif "division" in reply:
                    division()
                elif "multiplication" in reply:
                    multiplication()
                elif "pascaltriangle" in reply:
                    pascaltriangle()
                #--------------------------------------------->

                else:
                    speak(reply)
wish()
while True:
    Main()

#-------->Structured by Biswa