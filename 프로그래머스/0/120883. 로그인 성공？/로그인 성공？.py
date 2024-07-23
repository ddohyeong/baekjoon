def solution(id_pw, db):
    login_check = False
    
    for member in db :
        if member[0] == id_pw[0] and member[1] == id_pw[1]:
            return "login"
        if member[0] == id_pw[0]:
            login_check = True
            
    if login_check:
        return 'wrong pw'
    return 'fail'