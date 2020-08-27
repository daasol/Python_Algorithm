def binary_search(skill,index, ststr) :
    if skill[index] in ststr :
        return True
    #d가 없어



def solution(skill, skill_trees):
    answer = 0
    result = 0


    for i in range(len(skill_trees)) :
        index, j, count =0, 0, 0

        ststr=list(skill_trees[i])
        while index<len(skill)-1 and j<len(ststr)-1:
            if skill[index] == ststr[j] :
                if binary_search(skill, index+1, ststr[:j]) :
                    break
                elif binary_search(skill, index+1, ststr[j:]):
                    count+=1
                    index+=1
                    j+=1
                    continue
                else :
                    index+=1
            else : j+=1

        if count>=1 :
            answer+=1
    print('answer', answer)
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

solution(skill, skill_trees)
