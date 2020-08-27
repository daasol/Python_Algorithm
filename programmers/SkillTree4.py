def search(skill,index, ststr) :
    if index>=len(skill)-1 : return False
    elif skill[index] in ststr :
        return True
    else : return False

def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)) :
        result = 0
        index, j=0, 0
        ststr=list(skill_trees[i])
        while index<=len(skill)-1 and j<len(ststr) :
            if skill[index] == ststr[j] :
                #j-1이 리스트를 역행했음.
                if search(skill, index+1, ststr[:j]) :
                    result=0
                    break
                else :
                    index+=1
                    j+=1
                    result += 1
                    continue
            else : j+=1


        if result>=1 : answer+=1

    print('answer', answer)
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
#skill_trees = ["BDA"]

solution(skill, skill_trees)
