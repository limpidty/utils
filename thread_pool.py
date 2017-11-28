# -*-coding:utf-8-*-
import threadpool


def get_name(m, n, o):
    print m, n, o


# 传多个参数
# 方法1 使用集合传递参数，参数顺序与方法所需参数一致
lst_vars_1 = ['1', '2', '3']
lst_vars_2 = ['4', '5', '6']
func_var = [(lst_vars_1, None), (lst_vars_2, None)]
# 方法2 使用字典传递,字典键需要和方法中的参数名一致
dict_vars_1 = {'m': '1', 'n': '2', 'o': '3'}
dict_vars_2 = {'m': '4', 'n': '5', 'o': '6'}
func_var = [(None, dict_vars_1), (None, dict_vars_2)]

pool = threadpool.ThreadPool(200)
# argv_list 为参数列表
request_list = threadpool.makeRequests(get_name, func_var)
[pool.putRequest(req) for req in request_list]
pool.wait()
