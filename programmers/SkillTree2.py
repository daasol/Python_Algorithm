
#시간을 더 줄여서 다시 풀어보기 (1초 안나오게)
def solution(skill, skill_trees):
    answer = 0
    sstr = list(skill) #2
    for i in range(len(skill_trees)) :
        check=[]
        ststr = skill_trees[i]
        j, index=0, 0
        while True :
            if(j==len(ststr)) :
                answer += checksum(check)
                break

            elif index==(len(sstr)-1):
                answer += checksum(check)
                break

            #index가 sstr을 초과하는 경우 막아야함.
            if(sstr[index] in ststr[j]) :
                check.append(j)
                index+=1

                # if (j == len(ststr)-1):
                #     answer += checksum(check)
                #     break
                j=0

            else : j+=1
    print(answer)




def checksum(check) :
    count=0
    for i in range(len(check)-1) :
        if (len(check)-1)==0 or i==len(check)-1 : count+=1
        else :
            n, m = check[i], check[i + 1]
            if n>m : break
            count+=1
    return count




skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
#skill_trees = ["BACDE",  "AECB", "BDA"]

solution(skill, skill_trees)

