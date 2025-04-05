import req_func
from req_import import *

def main():
    while True:
        words = req_func.req_words()
        same_words = {}
        for i in range(1,1_000):
            same_words[i] = []
        for i in range(len(words['words'])):
            same_words[len(words['words'][i])].append(i)
        supper_same_words = {}
        for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            supper_same_words[i] = [[] for i in range(1_000+2)]
        for i in same_words:
            for j in same_words[i]:
                if words['words'][j][0] == words['words'][j][-1]:
                    supper_same_words[words['words'][j][0]][i].append(j)
        # print(supper_same_words)
        for i in supper_same_words:
            for j in range(len(supper_same_words[i])):
                if len(supper_same_words[i][j])>0:
                    pass
                    # print(supper_same_words[i][j])
                if len(supper_same_words[i][j]) >= 4:
                    # print(words['words'][supper_same_words[i][j][0]])
                    # print(words['words'][supper_same_words[i][j][1]])
                    # print(words['words'][supper_same_words[i][j][2]])
                    data = {
                        "done": False,
                        "words": [
                            {
                                "dir": 1,
                                "id": words['words'][supper_same_words[i][j][0]],
                                "pos":[0,0,0]
                            },
                            {
                                "dir": 3,
                                "id": words['words'][supper_same_words[i][j][1]],
                                "pos":[0,0,j-1]
                            },
                            {
                                "dir": 3,
                                "id": words['words'][supper_same_words[i][j][2]],
                                "pos":[j-1,0,j-1]
                            },
                            {
                                "dir": 1,
                                "id": words['words'][supper_same_words[i][j][3]],
                                "pos":[0,0,j-1]
                            }
                        ]
                    }
                    req_func.req_build(data)
        # print('____')




main()