#!/usr/bin/env python
#! -*- coding: utf-8 -*-
"""
Created on 24.06.2013

@author: Guest007
"""

import sys, os
import argparse
import inspect
import plugins.csv_in
import plugins.base


def get_plugins():
    """Импортируем все модули, получаем кортеж (имя, описание)"""

    plugin_dir = "plugins"

    # Сюда добавляем имена загруженных модулей
    modules = []

    # Возвращаемые плагины
    result = []

    # Перебирем файлы в папке plugins
    for fname in os.listdir(plugin_dir):

        # Нас интересуют только файлы с расширением .py
        if fname.endswith(".py"):

            # Обрежем расширение .py у имени файла
            module_name = fname[: -3]

            # Пропустим файлы base.py, csv_in.py и __init__.py
            if module_name != "base" and module_name != "__init__" and module_name != "csv_in":

                # Загружаем модуль и добавляем его имя в список загруженных модулей
                package_obj = __import__(plugin_dir + "." +  module_name)
                modules.append(module_name)

    # Перебираем загруженные модули
    for modulename in modules:
        module_obj = getattr(package_obj, modulename)

        # Перебираем все, что есть внутри модуля
        for elem in dir(module_obj):
            obj = getattr(module_obj, elem)

            # Это класс?
            if inspect.isclass(obj):

                # Класс производный от baseplugin?
                if issubclass(obj, plugins.base.baseplugin):
                    # Создаем экземпляр и выполняем функцию run
                    a = obj()
                    result.append((a.run(), a))

    return result


def process_command_line():
    """
    Разбирам командную строку.
    Параметры не передаём.
    Возвращаем значения аргументов
    """

    # initialize the parser object:
    parser = argparse.ArgumentParser(description='This is testing for GED',
        epilog='end of using testing-GED', formatter_class=argparse.RawTextHelpFormatter)

    # define options here:
    parser.add_argument('--source_path', type=str, action='store', dest='sp',
        help='Source file name (with path)')

    # here will be a list of avaliable plugins
    parser.add_argument('--plugin', type=str, action='store', dest='plug',
        help='''Plugin for result's formatting from this list:
            '''+'''
            '''.join([n[0][0]+": "+n[0][1] for n in get_plugins()]))

    args = parser.parse_args()

    # show help if less than 2 parameters are given
    if not args.sp or not args.plug:
        parser.print_help()
        sys.exit()

    return args


def main():
    """Main action"""

    # Get all plugins as dict (keys - names from cmd-line)
    all_plugins = dict([(n[0][0], n[1]) for n in get_plugins()])

    # Initialising reader
    cin = plugins.csv_in.cvsImport()

    # Get cmd-args
    args = process_command_line()

    # Initialising corresponding writer
    a = all_plugins[args.plug]

    # write
    a.write(cin.read(args.sp))

    return 0         # success

if __name__ == '__main__':
    status = main()
    sys.exit(status)
