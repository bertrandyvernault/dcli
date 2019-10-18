
import os
import sys
from PyInquirer import prompt
from ..logger import error
from ..const import TARGET_FILE_FIELD, TARGET_METHOD_FIELD, TARGET_METHOD_ARGS_FIELD, TARGET_METHOD_RETURN_FIELD

def askJavaQuestions():
    javaQuestions = [
        {
            'type': 'input',
            'name': TARGET_FILE_FIELD,
            'message': 'Main file for the user, entry file for the user (e.g. Main) without extension:',
        },
        {
            'type': 'input',
            'name': TARGET_METHOD_FIELD,
            'message': 'Method for the user, entry point for the user (e.g. methodName):',
        },
        {
            'type': 'input',
            'name': TARGET_METHOD_ARGS_FIELD,
            'message': 'Args list for the previous method, what the user will receive (e.g. int amount, double quantity):',
        },
        {
            'type': 'input',
            'name': TARGET_METHOD_RETURN_FIELD,
            'message': 'Return type of the previous method, what the user will have to return (e.g. String):',
        }
    ]
    answers = prompt(javaQuestions)
    if len(answers) == 0:
        error('Cancelled.')
        sys.exit()
    return answers