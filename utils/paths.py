import os
import tests


def path_to_apk(file_name):
    return os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), f'../apk/{file_name}')
    )

def path_to_env(file_name):
    return os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), f'../{file_name}')
    )
