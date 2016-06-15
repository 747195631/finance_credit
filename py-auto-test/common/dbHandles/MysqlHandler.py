# -*- coding:utf-8 -*-
import pymysql


class MysqlHandler(object):
    def __init__(self, mysql_user=None, mysql_host=None, mysql_port=3306, mysql_password=None, mysql_db=None,
                 charset=None):
        self.__mysql_user = mysql_user
        self.__mysql_host = mysql_host
        self.__mysql_port = mysql_port
        self.__mysql_password = mysql_password
        self.__mysql_db = mysql_db
        self.__charset = charset

    def get_mysql_data(self, sql):
        '''
        :param sql: sql语句
        :return: 返回结果list，每组结果存在一个元组里
        '''
        mysql_object = pymysql.connect(user=self.__mysql_user, passwd=self.__mysql_password, host=self.__mysql_host,
                                       port=self.__mysql_port, db=self.__mysql_db, charset=self.__charset)
        cursor = mysql_object.cursor()
        cursor.execute(sql)
        data_list = list()
        for data in cursor:
            data_list.append(data)
        cursor.close()
        mysql_object.close()
        return data_list

    def update_mysql_data(self, sql):
        mysql_object = pymysql.connect(user=self.__mysql_user, passwd=self.__mysql_password, host=self.__mysql_host,
                                       port=self.__mysql_port, db=self.__mysql_db, charset=self.__charset)
        cursor = mysql_object.cursor()
        cursor.execute(sql)
        mysql_object.commit()
        cursor.close()
        mysql_object.close()

    def insert_mysql_data(self, sql):
        mysql_object = pymysql.connect(user=self.__mysql_user, passwd=self.__mysql_password, host=self.__mysql_host,
                                       port=self.__mysql_port, db=self.__mysql_db, charset=self.__charset)
        cursor = mysql_object.cursor()
        cursor.execute(sql)
        mysql_object.commit()
        cursor.close()
        mysql_object.close()

    def delete_mysql_data(self, sql):
        mysql_object = pymysql.connect(user=self.__mysql_user, passwd=self.__mysql_password, host=self.__mysql_host,
                                       port=self.__mysql_port, db=self.__mysql_db, charset=self.__charset)
        cursor = mysql_object.cursor()
        cursor.execute(sql)
        mysql_object.commit()
        cursor.close()
        mysql_object.close()

    @staticmethod
    def insert_str_generation(table, data_dict):
        keys = ""
        values = ""
        for i in data_dict.keys():
            keys = keys + i + ","

        for i in data_dict.values():
            values = values + "'" + i + "'" + ","

        sql = "insert into " + table + " (" + keys[:-1] + ")" + " values (" + values[:-1] + ")"
        return sql

    @staticmethod
    def delete_str_generation(table, condition):
        if condition:
            sql = "delete from " + table + " where " + condition
        else:
            sql = "delete from " + table
        return sql

    @staticmethod
    def update_str_generation(table, values_dict, condition):
        values = ""
        for i in values_dict:
            values = values + i + "=" + "'" + values_dict[i] + "'" + ","
        if condition:
            sql = "update " + table + " set " + values[:-1] + " where " + condition
        else:
            sql = "update " + table + " set " + values_dict
        return sql

    @staticmethod
    def select_str_generation(table, field_list, condition=None):
        sql_head = "select "
        for i in field_list:
            sql_head = sql_head + i + ","
        if condition:
            sql = sql_head[:-1] + " from " + table + " where " + condition
        else:
            sql = sql_head[:-1] + " from " + table
        return sql

    @staticmethod
    def condition_function(condition_dict):
        condition = ""
        for i in condition_dict:
            condition = condition + i + "=" + "'" + condition_dict[i] + "'" + " and "
        return condition[:-5]
