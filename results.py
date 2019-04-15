with open("chatbotlogs.txt") as logs:
    with open("chatboteval.txt") as stat:
        mylogs = logs.read().split("$$$")
        log = []
        for x in range(0, len(mylogs),4):
            log.append(mylogs[x:x+4])
        myeval=stat.read().split("$$$")
        stats = []
        for x in range(0, len(mylogs),4):
            stats.append(myeval[x:x+4])
        myeval = stats[:]
        for x in range(0,len(log)):
            if log[x] == []:
                del log[x]
        for x in range(len(stats)-1,-1,-1):
            if stats[x] == []:
                del stats[x]
        for x in range(0,len(log)): 
            for ev in stats:
                
                if str(int(log[x][0])+1)==str(ev[0]) and log[x][3] == ev[2]:
                    log[x].append(ev[3])
            print(log[x])
        with open("eval.csv", "w") as out:
            for message in log:
                out.write(";".join(message))
                out.write("\n")
            
