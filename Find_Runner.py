n = 5
arr = [8,7,6,5,4]  # [2,3,6,6,5] [8,7,6,5,4]


def ViceCampeao(arr):
     resultado = list(dict.fromkeys(arr))
     resultado.sort(reverse = True)
     return resultado.pop(1)


print(ViceCampeao(arr))