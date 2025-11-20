from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ntwf&-*x-x&p@0sen%pc6ea!tq7z4#bwoq_pv17d%e9ns53sfh"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = ["apps.expenses", "apps.users"]

THIRD_PARTY_APPS = [
    "rest_framework",
    "allauth",
    "allauth.account",
    "allauth.headless",
    "allauth.socialaccount",
    "corsheaders",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# allauth
HEADLESS_ONLY = True
HEADLESS_FRONTEND_URLS = {
    "account_signup": "http://127.0.0.1:5173/signup",
    "account_confirm_email": "http://127.0.0.1:5173/confirm/{key}",
    "account_reset_password": "http://127.0.0.1:5173/password/reset",
    "account_reset_password_from_key": "http://127.0.0.1:5173/password/reset/{key}",
}

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGIN_METHODS = ["email"]
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

HEADLESS_TOKEN_STRATEGY = "allauth.headless.tokens.strategies.jwt.JWTTokenStrategy"
HEADLESS_JWT_PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQChXxaJGfC8qXw9
jvuBgBltG/GbVyLwzt4FdnvoKatUoEsjbWYw8MsyieysUfNTOrGwSBCrHlrH35Bt
V4d8PqnaSz35r6yvozwLMBe3EP45vfoorCtfcKeEdiaLsARXJJTc8CH4A/3vFDDF
DaBzcvpfENcLyKU508NhQaqvRkTc9LQP+n+WSIVWuVm6vuSNHbHTdjI3cgPxISg3
BJ9KLmhc2zq+RGq6z9XHCGE6KuidrxgwRHDZx36wBaYxw9queYskBX3ShCi5zrrP
hPk1Fj+K5QuQPeetMWD1ZQpKMr74VpeV3J9eim29CnsSeJ2oqELY5Z24NvJWAdX6
jlWk5cibAgMBAAECggEACcP1WyqktOYUzKzgb3/PChlMz7fAN45tRStcaDpNUfu5
UFWIf6GyykYqemsjLIA6zI4v5AscN0hCNzu6yTwJj1pKT9ffvWlFcu/gH4X5vIjQ
oLF6lnX8zTlRL9bhDFz8XTpy881aCqPQJ7yhXxswJ5yfRulHhm5YPoR4zc6U0EIu
Au1LJiU2I9SrMWxsr3JIl+HOcpdIP04qcH7rF3IERG0ZrHVbizzTajynJAgkX7js
Kms69qgHkVnMJnMA5+K+IkAOqcuLCOgdOkD3rsnqNhG+oU8Er2edTiSWa+o1robV
7BWyngeTs/RDB8MIgK4VBLS8JMRp0XcJNvRGCPegkQKBgQDgYtPSMTVvPcJYthfV
GTC9RUOA7jEQc5IsTFY+TfXYBe10NuxrbjUuGdUtCZudOPkU6LmmbZcG2Gcx0CYy
ml4oAx8YzNtLG/tewgbsxI/Pl6SGhXls13HZWT2Ctgi5ZuPYAmf384LSWkv08se9
euokITDqPXu2G54tscebZ8NBPwKBgQC4G3HvqHCp2MBUaLpJ8TdxH6o3ImmxGLT0
g/YN88ISLtIDXKzQZgMug8FhVF2x58pJzyIh9ToBwhnGV5nTRMyi97SiGDx/3OFL
HgEWIzjJB0PUwZeN6f9CCsw4qvk/vlc4vS279lAtS8RmGysdIZHb7GS8KTwqa6Y6
S0MdDBmFpQKBgQDbS3rdKD6i02cHMB+mopHhyLmqXiARhgHLzWdUSPkGAPUK6Uqx
y+mpfpG7DHLLe4zjhHc8UkqR5Bkms9lBB2ESFcrkgAGqLFTFTTdbWtd5+ShQWE5N
s1mPJApbnvBz0jzHNcLKr3ChiKJHaKcRZflDCjU2GJS5a9BxtBfyp7xKHQKBgGr6
96/tTtpDKy9hU66XzkGbxssW4heYZb4X2CivVjw+nKZ7eaf3Py4OPZaS8YbpS7Cr
/geBed1/rn6EdMxBFDA2g+4U60LZVMjTfIoimWKnKBE/FRPPvxXfNGBRaVhTAFfm
BedM77YCavNyIhFhamJC8R4tT9rOht8k0LDWURZJAoGBAK9t2JEH6ZnK5SwtA59d
el8NnpodHvF1XErDLPCafK7cP5xOdPJ0PVYdsjUhA8iiQy6nLn00VmRv6OXenOqa
ZJ/rgsnedLYc+qlmFrZRDqhvgqrpBkQojpTlBL6/5nPaGe6ONHsPxeKWJidTgWfe
tubZOXUFnPTVcbQsrB1hryFS
-----END PRIVATE KEY-----
"""

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
