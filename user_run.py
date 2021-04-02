#
from service.user_service import UserService

if __name__ == '__main__':
    us = UserService()
    text = input("请输入数据：")
    if text in ['1','新增']:
        print('调用新增逻辑')
        abc = input()
        lst = abc.split(' ')
        us.add_stu(*lst)
    elif text in ['2','修改']:
        print('调用修改逻辑')
        change = input()
        lst = change.split(' ')
        us.mod_stu(*lst)
    elif text in ['3', '删除']:
        print('调用删除逻辑')
        name = input()
        result = us.del_stu(name)
    else:
        print('调用查询逻辑')
        name = input()
        result = (us.get_stu(name))
        for x in result:
            print("学生号：{},学生姓名：{},学生年龄：{},学生性别:{},学生班级:{},学生身份证号：{},城市：{}"
                  .format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))