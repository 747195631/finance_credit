# -*- coding:utf-8 -*-
from common.dbHandles.MysqlHandler import MysqlHandler
import pytest


def test_insert_str():
    table = "table_name"
    data_dict = {"key1": "value1", "key2": "value2"}
    sql = MysqlHandler.insert_str_generation(table=table, data_dict=data_dict)
    assert sql == "insert into table_name (key1,key2) values ('value1','value2')"


def test_delete_str():
    table = "table_name"
    condition_dict = {"key1": "value1", "key2": "value2"}
    condition = MysqlHandler.condition_function(condition_dict)
    sql = MysqlHandler.delete_str_generation(table, condition)
    assert sql == "delete from table_name where key1='value1' and key2='value2'"


def test_update_str():
    table = "table_name"
    values_dict = {"key1": "value1", "key2": "value2"}
    condition_dict = {"key1": "value1", "key2": "value2"}
    condition = MysqlHandler.condition_function(condition_dict)
    # condition = "key1=\'value1\' and key2=\'value2\'"
    sql = MysqlHandler.update_str_generation(table, values_dict, condition)
    assert sql == "update table_name set key1='value1',key2='value2' where key1='value1' and key2='value2'"


def test_select_str():
    table = "table_name"
    field_list = ['field1', 'field2']
    condition_dict = {"key1": "value1", "key2": "value2"}
    condition = MysqlHandler.condition_function(condition_dict)
    sql = MysqlHandler.select_str_generation(table,field_list,condition)
    assert sql == "select field1,field2 from table_name where key1='value1' and key2='value2'"

