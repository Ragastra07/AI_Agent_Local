def count_py_files(directory):
    import os
    return len([f for f in os.listdir(directory) if f.endswith(".py")])
