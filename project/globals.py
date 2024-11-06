cancel_ag_flag=None
tokenized_flag=None

def get_cancel_flag():
    global cancel_ag_flag
    return cancel_ag_flag

def set_cancel_flag(flag):
    global cancel_ag_flag
    cancel_ag_flag=flag

def get_tokenized_flag():
    global tokenized_flag
    return tokenized_flag

def set_tokenized_flag(flag):
    global tokenized_flag
    tokenized_flag=flag