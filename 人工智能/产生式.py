# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月02日
"""

# dic = {'apple':[{'feature': ['圆形', '红色']},
#                      {'feature': ['大', '圆形']}
#                      ]
#             }

# dic = {'apple':[['圆形', '红色'],['大', '圆形']
#                      ]
#             }

# {'apple': [('red', 'big'), ('red', 'cirle')]}
# feture_str = dic.dumps(feature_list, ensure_ascii=False)
import json
dic = {}
def insert_data():
    while True:
        command_input = input("插入数据输入请输入i,退出请输入q\n")
        if command_input == "i":
            command_feature = input("请输入事物特征：\n")
            command_result = input("请输入事物结果：\n")
            feature_list = command_feature.split(',')
            feature_set = set(feature_list)
            feature_list = list(feature_set)
            if command_result in dic.keys():
                dic[command_result].append(feature_list)
            else:
                dic[command_result] = [feature_list]
        else:
            print("结束插入\n")
            break
    return dic


def select_data():
    if dic:
        while True:
            command_input = input("特征查结果输入f\t,结果查特征输入r\t,退出请输入q\n")
            if command_input == "f":
                command_feature = input("请输入事物特征：\n")
                feature_list = command_feature.split(',')
                feature_set = set(feature_list)
                # get_result = [k for k,v in dic.items() if v == feature_set in dic.values()]
                for k, v in dic.items():
                    if feature_set in v:
                        get_result = k
                        print("该动物是%s:"%get_result)
                        break
            elif command_input == "r":
                command_result = input("请输入事物结果：\n")
                for k in dic.keys():
                    if k == command_input:
                        print("该动物的特征是%s"%dic[k][0])
                        break
                else:
                    print("规则库中没有这个结果（key）")
            else:
                print("结束查询")
                break
    else:
        print("字典中没有数据，请先插入输入")
        return False

def delete_data():
    if dic:
        while True:
            command_input = input("删除数据请输入d\n,退出请输入q\n")
            if command_input == "d":
                command_result = input("请输入事物结果：\n")
                for k in dic.keys():
                    if k == command_input:
                        del dic[k]
                        break
                else:
                    print("规则库中没有这个结果（key）")
            else:
                print("结束删除操作")
                break
    else:
        print("字典中没有数据，请先插入输入")
        return False
    return dic

def save_data(dic):
    # print(dic)
    # with open('规则库', 'w+', encoding='utf-8') as fp:
    #     json.dump(dic, fp, ensure_ascii=False)
    print(dic)
    with open('规则库', 'w+', encoding='utf-8') as fp:
        fp.write(dic)


def main():
    while True:
        command_input = input("插入功能I,查询功能S,删除功能D,退出程序Q\n")
        if command_input == "I":
            insert_data()
            save_data(dic)
        elif command_input == "S":
            select_data()
        elif command_input == "D":
            delete_data()
            save_data(dic)
        else:
            print("程序结束!")
            break

if __name__ == '__main__':
    main()











