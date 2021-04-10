from App.models.movie_user import MovieUser


def get_movie_user(user_ident):
    if not user_ident:
        return None

    # 根据id
    user = MovieUser.query.get(user_ident)
    if user:
        return user

    # 根据用户名
    user = MovieUser.query.filter(MovieUser.username == user_ident).first()
    if user:
        return user

    # 根据手机号
    user = MovieUser.query.filter(MovieUser.phone == user_ident).first()
    if user:
        return user

    return None
