import pyinputplus as pyip

madLibBase = open('madLibBase.txt').read()

while True:
        if 'adjective' in madLibBase.lower():
            adjective = pyip.inputStr('Please enter an adjective: ')
            madLibBase = madLibBase.replace('ADJECTIVE', adjective, 1)
        elif 'noun' in madLibBase.lower():
            noun = pyip.inputStr('Please enter a noun: ')
            madLibBase = madLibBase.replace('NOUN', noun, 1)
        elif 'verb' in madLibBase.lower():
            verb = pyip.inputStr('Please enter a verb: ')
            madLibBase = madLibBase.replace('VERB', verb, 1)
        elif 'adverb' in madLibBase.lower():
            adverb = pyip.inputStr('Please enter a adverb: ')
            madLibBase = madLibBase.replace('ADVERB', noun, 1)
        else:
            break

createdMadLib = open('createdMadLib.txt', 'w')
createdMadLib.write(madLibBase)


