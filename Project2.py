import random
import csv
class main():
    
    def __init__(self):
        self.scraper()
        self.comparer()
    def scraper(self):
        """This is the file scraper that turns a note file into a csv file with the frequency of each word"""
        filename = input("What is the file name (including extension) that you would like to use:")
        scraping = open(filename, "r", encoding = "utf-8")
        filename = filename.split(".")
        self.scrappedname = filename[0] + "scrapped.csv"
        scrapinglines = scraping.readlines()
        scrappeddict = {}
        for line in scrapinglines:
            linelist = line.split()
            for word in linelist:
                word = word.lower()
                word = word.strip('"')
                word = word.strip('“')
                word = word.strip('”')
                word = word.strip(".")
                word = word.strip(",")
                if word == "u.s":
                    if "u.s." in scrappeddict:
                        scrappeddict["u.s."] += 1
                    else:
                        scrappeddict["u.s."] = 1
                elif word[-2:] == "'t":
                    word = word.split("'")
                    if word[0] in scrappeddict:
                        scrappeddict[word[0]] += 1
                    else:
                        scrappeddict[word[0]] = 1
                    if "n''t" in scrappeddict:
                        scrappeddict["n''t"] += 1
                    else:
                        scrappeddict["n''t"] = 1
                    
                elif word[-2:] == "'s":
                    word = word.split("'")
                    if word[0] in scrappeddict:
                        scrappeddict[word[0]] += 1
                    else:
                        scrappeddict[word[0]] = 1
                    if "''s" in scrappeddict:
                        scrappeddict["''s"] += 1
                    else:
                        scrappeddict["''s"] = 1
                elif word[-3:] == "'re":
                    word = word.split("'")
                    if word[0] in scrappeddict:
                        scrappeddict[word[0]] += 1
                    else:
                        scrappeddict[word[0]] = 1
                    if "''re" in scrappeddict:
                        scrappeddict["''re"] += 1
                    else:
                        scrappeddict["''re"] = 1
                elif word[-2:] == "'m":
                    word = word.split("'")
                    if word[0] in scrappeddict:
                        scrappeddict[word[0]] += 1
                    else:
                        scrappeddict[word[0]] = 1
                    if "''re" in scrappeddict:
                        scrappeddict["''m"] += 1
                    else:
                        scrappeddict["''m"] = 1
                elif word[-3:] == "'ve":
                    word = word.split("'")
                    if word[0] in scrappeddict:
                        scrappeddict[word[0]] += 1
                    else:
                        scrappeddict[word[0]] = 1
                    if "''re" in scrappeddict:
                        scrappeddict["''ve"] += 1
                    else:
                        scrappeddict["''ve"] = 1
                elif word[-3:] == "'ll":
                    word = word.split("'")
                    if word[0] in scrappeddict:
                        scrappeddict[word[0]] += 1
                    else:
                        scrappeddict[word[0]] = 1
                    if "''ll" in scrappeddict:
                        scrappeddict["''ll"] += 1
                    else:
                        scrappeddict["''ll"] = 1
                elif word[-2:] == "'d":
                    word = word.split("'")
                    if word[0] in scrappeddict:
                        scrappeddict[word[0]] += 1
                    else:
                        scrappeddict[word[0]] = 1
                    if "''d" in scrappeddict:
                        scrappeddict["''d"] += 1
                    else:
                        scrappeddict["''d"] = 1
                elif word in scrappeddict:
                    scrappeddict[word] += 1
                else:
                    scrappeddict[word] = 1
        with open(self.scrappedname, 'w') as f:
            for key in scrappeddict.keys():
                f.write("%s, %s\n" % (key, scrappeddict[key]))
        
        scraping.close()
    def comparer(self):
        """This function compares the scrapped .csv file with an expected word frequency file that follows Zipf's law"""
        wordlist = open("wordlist.csv", "r")
        scrapped = open(self.scrappedname, "r")
        scrappedlines = scrapped.readlines()
        linesnum = 0
        words = 0
        maximum = 0
        for lines in scrappedlines:
            linelist = lines.split(",")
            linelist[1] = linelist[1].rstrip()
            wc = linelist[1]
            wordcount = int(wc)
            words += wordcount
            linesnum +=1
            if int(wordcount) > int(maximum):
                maximum = wc
        maximum = int(maximum)  
        rand = random.randint(0, 974)
        wordval = wordlist.readlines()
        wordvallist = wordval[rand].split(",")
        wordvallist[1] = wordvallist[1][:-1]
        wordvallist[0] = wordvallist[0].strip('"')
        t=0
        for line in scrappedlines:
            linelist = line.split(",")
            linelist[1] = linelist[1].rstrip()
            if wordvallist[0] in linelist[0]:
                print(f"Your random word is {wordvallist[0]} and it shows up {linelist[1]} times")
                print(f"{wordvallist[0]} is expected {int((1/(rand + 1))*maximum)} times as thus it shows up {int((int((1/(rand + 1))*maximum)/int(linelist[1]))*100)}% compared to the expected value")
            else:
                t +=1
        if linesnum == t:
            print(f"Your random word {wordvallist[0]} does not appear in your file")
        wordlist.close()
        scrapped.close()
    
    
if __name__ == "__main__":
    main()