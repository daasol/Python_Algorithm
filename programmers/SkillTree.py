
#시간을 더 줄여서 다시 풀어보기 (1초 안나오게)
def solution(skill, skill_trees):
    answer = 0
    sstr = list(skill) #2

    for i in range(len(skill_trees)) :
        ststr = skill_trees[i]

        index, j = 0, 0
        temp=[]

        while True :
            #ststr에 sstr이 있을 때
            #index가 3일때 자꾸 걸림
            if index<len(sstr) and (sstr[index] in ststr[j])  :
                temp.append(j)
                j=0

                if not index==0 :
                    n=index-1
                    m=index
                    if (temp[n] > temp[m]) :
                        break
                    else : j+=1
                index+=1

            else :
                j += 1
                if j==len(ststr) :
                    if index>=1 :
                        answer+=1
                    break




skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

solution(skill, skill_trees)
