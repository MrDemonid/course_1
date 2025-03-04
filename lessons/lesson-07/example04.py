# запись через write
t = "The three color is a red, green. blue\n"
l = ["red", "green", "blue"]

with open("./datas/data04.txt", "w", encoding="utf-8") as f:
    res = f.write(t)
    print(f"{res = }, {len(t) =}")


# запись через writelines
with open("./datas/data04.txt", "a", encoding="utf-8") as f:
    f.writelines(l)
    f.write('\n')
    f.writelines("\n".join(l))
    f.write('\n-----------\n')

# запись через print
with open("./datas/data04.txt", "a", encoding="utf-8") as f:
    print(* l, file=f)
    for s in l:
        print("print >", s, file=f, end=" < \n")
