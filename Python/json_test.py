import json

a = [i for i in range(10)]

# print(a)

# for i in range(1, 10):
#     a = [k for k in range(i, 10 * i, i)]
#     with open("json.txt", "a") as j:
#         json.dump(a, j)

#         j.write("\n")

with open("json.txt", "w") as json_file:
    # a = json.load(json_file)
    # print(a)
    # a.append("nsindgisndingsd")
    # a.append("NAGSOINGOINASGIO")
    # print(a)
    # aj = json.dumps(a, indent=4)
    # print(aj)
    # json_file.write(aj)
    json_file.write("")
