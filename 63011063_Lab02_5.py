class game_of_word:

    def check(word):
        mylist = []
        left = []
        re = 0
        for i in range(len(word)):
            if i == 0 or re == 1:
                if "P " in word[i]:
                    subStr = str(word[i])
                    subStr = subStr.replace('P ', '')
                    mylist.append(subStr)
                    left.append(subStr)
                    print("\'", subStr, "\'", " -> ", mylist, sep="")
                    left.clear()
                    tempPreStr = subStr[len(subStr) - 2:len(subStr):1]
                    tempPreStr = tempPreStr.lower()
                    re = 0
                elif "R" in word[i]:
                    del mylist
                    print("game restarted")
                    mylist = []
                    re = 1

            else:

                if "P " in word[i]:
                    subStr = str(word[i])
                    subStr = subStr.replace('P ', '')
                    tempStr = subStr[0:2:1]
                    tempStr = tempStr.lower()
                    if tempPreStr != tempStr:
                        print("\'", subStr, "\' -> game over", sep="")
                        break
                    mylist.append(subStr)
                    left.append(subStr)
                    print("\'", left[0], "\'", " -> ", mylist, sep="")
                    left.clear()

                elif "R" in word[i]:
                    del mylist
                    print("game restarted")
                    mylist = []
                    re = 1

                elif "X" in word[i]:
                    break
                elif 'p ' in word[i]:
                    print("\'", str(word[i]), "\' is Invalid Input !!!", sep="")
                    break


print("*** TorKham HanSaa ***")
str1 = list(input("Enter Input : ").split(','))
game_of_word.check(str1)