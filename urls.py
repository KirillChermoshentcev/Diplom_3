class Endpoints:

    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    LOGIN = f'{BASE_URL}/login'

    ACCOUNT = f'{BASE_URL}/account/profile'

    ORDER_HISTORY = f'{BASE_URL}/account/order-history'

    FORGOT_PASSWORD = f'{BASE_URL}/forgot-password'

    RESET_PASSWORD = f'{BASE_URL}/reset-password'

    CREATE_USER = f'{BASE_URL}/api/auth/register'

    DELETE_USER = f'{BASE_URL}/api/auth/user'

    INGREDIENTS = f'{BASE_URL}/api/ingredients'

    CREATE_ORDER = f'{BASE_URL}/api/orders'