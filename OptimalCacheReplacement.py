frameSize=int(input("Enter frame size: "))
pages=input("Enter pages to be browsed: ").split()
pages = [int(i) for i in pages]
pageCount = len(pages)
pagesinFrame=0
frame = []
hits=0
miss=0
framePageCount=0
pagesVisited=0
print("PAges: ",pages)
for i in pages:
    pagesVisited+=1
    if framePageCount<frameSize:
        if i not in frame:
            miss+=1
            framePageCount+=1
            frame.append(i)
            print("Page: ",i)
            print("Frame: ",frame)
        else:
            hits+=1
            print("Page: ",i)
            print("Frame: ",frame)
            continue
    else:
        if i not in frame:
            miss+=1
            dist = [-1]*frameSize
            temp = []
            for j in range(len(frame)):
                try:
                    dist[j] = pages.index(frame[j],pagesVisited-1)
                except ValueError:
                    dist[j] = 999
                    temp.append(pages.index(frame[j]))
            if(len(temp)>1):
                firstOcc = min(temp)
                framePageCount+=1
                frame[temp.index(firstOcc)]=i
            else:
                longestOcc = max(dist)
                framePageCount+=1
                frame[dist.index(longestOcc)]=i
            print("Page: ",i)
            print("Frame: ",frame)
        else:
            hits+=1
            print("Page: ",i)
            print("Frame: ",frame)
            continue
    

print("Total Pages: ",pageCount)
print("Total Pages Visited: ",pagesVisited)
print("Hits: ",hits)
print("Miss: ",miss)
print("Hit Ratio: ",(hits/pageCount))
print("Miss Ratio: ",(miss/pageCount))

            
    
