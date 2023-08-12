import collections

from markdown_to_json.markdown_to_json import Renderer, CMarkASTNester
from markdown_to_json.vendor.CommonMark import CommonMark
from collections import  *
import json
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *




def get_json_for_menu():
    file_path = ".\\DB\\menu.md"
    with open(file_path, encoding="utf-8") as file:
        ast = CommonMark.DocParser().parse(file.read())
        dictionary = CMarkASTNester().nest(ast)
        stringfield = Renderer().stringify_dict(dictionary)
        file.close()

    value = json.loads(json.dumps(stringfield))



    return value


def create_menu_json_file(jason_value):
    with open('.\\DB\\data_menu.json', 'w', encoding='utf-8') as f:
        json.dump(jason_value, f, ensure_ascii=False, indent=4)
        f.close()