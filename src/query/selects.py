from db.DBmanager import base_manager

def select_login_(login):
    res = base_manager.execute("select login from user where login=?", args=(login,))
    return res

def select_email_(email):
    res = base_manager.execute("select email from user where email=?", args=(email,))
    return res

def select_user_():
    res = base_manager.execute("select * from user ", args=())
    return res

def post_user(login, password, email, role_id):
    res = base_manager.execute("insert into user values(?, ?, ?, ?)", args=(login, password, email, role_id))
    return res
