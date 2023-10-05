num = input()
hashmap = {
    "00": 0,
    "25": 0,
    "50": 0,
    "75": 0
}
revNum = num[::-1]  

print(revNum)
if len(num) < 2:
    print(-1)

else:
    val = ""
    ans = float("inf")
    if "2" in revNum and "5" in revNum:
        ans = min(ans, revNum.index("2")+revNum.index("5"))

    if "7" in revNum and "5" in revNum:
        ans = min(ans, revNum.index("7")+revNum.index("5") - 1)
        
    if "5" in revNum and "0" in revNum:
        ans = min(ans, revNum.index("5")+revNum.index("0") - 1)
    
    if revNum.count("0") >= 2:
        index = revNum.index("0")
        ans = min(ans, index + revNum[index:].index("0") - 1)
    
        
    print(ans if ans != float("inf") else -1)    
     
