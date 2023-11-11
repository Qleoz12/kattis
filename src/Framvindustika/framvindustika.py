p, w = map(int, input().split()); g = p*w//100
print(f'[{"#"*g+"-"*(w-g)}] |{" "*(4-len(str(p)))}{p}%')