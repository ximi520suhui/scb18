# 封装成一个函数
# lesson7里面后面的具体的执行操作可以单独放在这里执行

from Python1.lesson7 import read_case,api_fun,write_result   # 复制前面的执行函数，报红的部分也就是之前封装的函数导入就可以了

def execute_fun(filename,sheetname,):        # 测试执行
    cases=read_case(filename,sheetname)
    for case in cases:           # 直接在上面获取到的表格生成的list数据，循环取出要的单个数据,,得出的数据都是字符串数据类型
        case_id=case['case_id']
        url=case['url']           # 定义变量名为url，获取表格里的’url‘的值
        data=eval(case['data'])       # 获取data的值,,把字符串转成字典
        expect=eval(case['expect'])    #'''获取expect的值,(他的值不是在表格直接取，而是在上面def read_case下的循环里定义的expect值，也是字符串形式，需要转换成字典)'''
        # print(url,data,expect)
        # print(case_id, expect)
        expect_msg=expect['msg']      # 读到预期结果的msg信息
        real_result=api_fun(url=url,data=data)
        real_msg = real_result['msg']  # 获取实际结果的msg信息
        print('期望结果为:{}'.format(expect_msg))
        print('实际结果为:{}'.format(real_msg))
        # print(case_id,expect_msg,real_msg)
        # if expect_msg==real_msg:
        #     print('passed!')
        # else:
        #     print('fail')

        if expect_msg==real_msg:
            print('第{}条用例通过!'.format(case_id))
            final_re='passed'
        else:
            print('第{}条用例不通过!'.format(case_id))
            final_re='failed'
        write_result(filename,sheetname,case_id+1,8,final_re)      #    比对预期结果和实际结果后，写入结果到测试用例
        print('*'*20)
# 调用函数
execute_fun('D:\\python workspace\\scb18\\test_data\\test_case_api.xlsx', 'register')        # 跑通注册接口，并写回结果
execute_fun('D:\\python workspace\\scb18\\test_data\\test_case_api.xlsx', 'login')          # 跑通登陆接口，并写回结果

# 找到test_case_api.xlsx的绝对路径：1）点击需要打开的文件按右键  2）点击file path   3）选中要打开的文件点击  4）复制显示的绝对路径
# 特殊符号前+\进行转义