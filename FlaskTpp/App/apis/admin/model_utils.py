from App.models.admin import AdminUser


def get_admin_user(user_ident):
    if not user_ident:
        return None

    # 根据id
    user = AdminUser.query.get(user_ident)
    if user:
        return user

    # 根据用户名
    user = AdminUser.query.filter(AdminUser.username == user_ident).first()
    if user:
        return user

    return None
