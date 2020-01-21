def ask_question(question='Please choose', options=['Y', 'N'], default=None):
    opt_list = []
    for opt in options:
        if opt not in opt_list:
            opt_list.append(opt)
    opt_list = [x.upper() for x in opt_list]
    if len(opt_list) < 1:
        raise Exception('No options provided!')
    if default != None:
        default = default.upper()
        if default not in opt_list:
            raise Exception('Default value is invalid!')
    opt_string = ''
    for i,opt in enumerate(opt_list):
        if opt == default:
            opt_string += '[' + opt + ']'
        else:
            opt_string += opt
        if i+1 < len(opt_list):
            opt_string += '/'
    answer = None
    error_string = 'That is not a valid option.'
    while answer not in opt_list:
        answer = input(question + ' ({}): '.format(opt_string)).strip().upper()
        if answer in opt_list:
            return answer
        else:
            if answer == '':
                if (default == None) or (default not in opt_list):
                    print(error_string)
                else:
                    return default
            else:
                print(error_string)