import os
import sys
from ..language import Language
from PyInquirer import prompt
from ...logger import error
from ...const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD, TARGET_METHOD_ARGS_FIELD, TARGET_METHOD_RETURN_FIELD


TEMPLATE_PATH = '/src/template'
SUCCESS_PATH = '/src/success'
APP_PATH = '/src/app'

SOLVE_PATH = '/src/app/main.c'
RUN_PATH = '/src/app/main.c'

ASSET_PATHS = ['src/Makefile', 'src/template/Target.h', 'src/app/Logger.c', 'src/app/Logger.h']

TARGET_FILE = 'Target'

class C(Language):
    def __init__(self):
        Language.__init__(self,
            'c',
            TEMPLATE_PATH,
            SUCCESS_PATH,
            APP_PATH,
            SOLVE_PATH,
            RUN_PATH,
            TARGET_FILE,
            'c',
            ASSET_PATHS
        )

    def ask_questions(self):
        cQuestions = [
            {
                'type': 'input',
                'name': TARGET_METHOD_FIELD,
                'message': 'Method for the user, entry point of the program (e.g. methodName):',
            },
            {
                'type': 'input',
                'name': TARGET_METHOD_ARGS_FIELD,
                'message': 'Input: args list for the previous method, what the user will receive (e.g. int amount, double quantity):',
            },
            {
                'type': 'input',
                'name': TARGET_METHOD_RETURN_FIELD,
                'message': 'Output type: return type of the previous method, what the user will have to return (e.g. int):',
            }
        ]
        answers = prompt(cQuestions)
        if len(answers) == 0:
            error('Cancelled.')
            sys.exit()
        return answers

    def need_to_generate_new_type(self):
        return False