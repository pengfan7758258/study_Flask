from App.models.cinema_admin import CinemaUser


def get_cinema_user(user_ident):
    if not user_ident:
        return None

    # 根据id
    user = CinemaUser.query.get(user_ident)
    if user:
        return user

    # 根据用户名
    user = CinemaUser.query.filter(CinemaUser.username == user_ident).first()
    if user:
        return user

    # 根据手机号
    user = CinemaUser.query.filter(CinemaUser.phone == user_ident).first()
    if user:
        return user

    return None
