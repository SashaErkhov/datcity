from req_import import *

def main():
    while True:
        for i in range(10):
            words = req_func.req_words()
            for j in range(10*(i+1)):
                data = {
                    "data" : 0,
                    "words" : [
                        {
                            "dir": 1,
                            "id": i,
                            "pos": [0, 0, 0]
                        }
                    ]
                }
                ok = False
                if words['mapSize'][0] >= len(words['words'][j]):
                    data['words'][0]['dir'] = 1
                    ok = True
                elif words['mapSize'][1] >= len(words['words'][j]):
                    data['words'][0]['dir'] = 2
                    ok = True
                else:
                    data['words'][0]['dir'] = 3
                    ok = True
                if ok:
                    print(req_func.req_build(data))
                    data = {
                        "data" : 1
                    }
                    print(req_func.req_build(data))
            req_func.req_shuffle()



main()