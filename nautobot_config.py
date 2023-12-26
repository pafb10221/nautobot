"""Nautobot development configuration file."""
import os

from nautobot.core.settings import *  # noqa: F403
from nautobot.core.settings_funcs import is_truthy

SECRET_KEY = os.getenv("NAUTOBOT_SECRET_KEY", "012345678901234567890123456789012345678901234567890123456789")
ALLOWED_HOSTS = ["*"]
#
# Debugging defaults to True rather than False for the development environment
#
DEBUG = is_truthy(os.getenv("NAUTOBOT_DEBUG", "True"))


# Django Debug Toolbar - enabled only when debugging
if DEBUG:
    if "debug_toolbar" not in INSTALLED_APPS:  # noqa: F405
        INSTALLED_APPS.append("debug_toolbar")  # noqa: F405
    if "debug_toolbar.middleware.DebugToolbarMiddleware" not in MIDDLEWARE:  # noqa: F405
        MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa: F405
    # By default the toolbar only displays when the request is coming from one of INTERNAL_IPS.
    # For the Docker dev environment, we don't know in advance what that IP may be, so override to skip that check
    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _request: DEBUG}

# Do *not* send anonymized install metrics when post_upgrade or send_installation_metrics management commands are run
INSTALLATION_METRICS_ENABLED = is_truthy(os.getenv("NAUTOBOT_INSTALLATION_METRICS_ENABLED", "False"))

#
# Logging for the development environment, taking into account the redefinition of DEBUG above
#

LOG_LEVEL = "DEBUG" if DEBUG else "INFO"
LOGGING["loggers"]["nautobot"]["handlers"] = ["verbose_console" if DEBUG else "normal_console"]  # noqa: F405
LOGGING["loggers"]["nautobot"]["level"] = LOG_LEVEL  # noqa: F405


#
# Plugins
#
PLUGINS = [
    "nautobot_firewall_models",
    "nautobot_ssot",
    "nautobot_golden_config",
    "nautobot_plugin_nornir",
    "nautobot_device_onboarding",
    "example_plugin"
]


#
# Databases config
#

DATABASES = {
    'default': {
        'NAME': 'nautobot',                         # Database name
        'USER': 'nautobot',                         # Database username
        'PASSWORD': 'nautobot',                     # Database password
        'HOST': 'gateway.rancher-desktop.internal', # Database server
        'PORT': '5432',                             # Database port (leave blank for default)
        'CONN_MAX_AGE': 300,                        # Max database connection age
        'ENGINE': 'django.db.backends.postgresql',  # Database driver ("mysql" or "postgresql")
    }
}
 
 
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://gateway.rancher-desktop.internal:6379/1",
        "TIMEOUT": 300,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Uncomment the following lines to configure TLS/SSL
            # "CONNECTION_POOL_KWARGS": {
            #     "ssl_cert_reqs": ssl.CERT_REQUIRED,
            #     "ssl_ca_certs": "/opt/nautobot/redis/ca.crt",
            #     "ssl_certfile": "/opt/nautobot/redis/tls.crt",
            #     "ssl_keyfile": "/opt/nautobot/redis/tls.key",
            # },
        },
    }
}


PLUGINS_CONFIG = {
    "nautobot_firewall_models": {
        "default_status": "Active"
    },
    "nautobot_ssot": {
        "hide_example_jobs": True
    },
    "nautobot_plugin_nornir": {
        "use_config_context": {"secrets": True},
        "nornir_settings": {
            "credentials": "nautobot_plugin_nornir.plugins.credentials.nautobot_secrets.CredentialsNautobotSecrets",
            "runner": {
                "plugin": "threaded",
                "options": {
                    "num_workers": 20,
                },
            },
        },
    },
    "nautobot_golden_config": {
        "per_feature_bar_width": 0.15,
        "per_feature_width": 13,
        "per_feature_height": 4,
        "enable_backup": True,
        "enable_compliance": True,
        "enable_intended": True,
        "enable_sotagg": True,
        "enable_plan": True,
        "enable_deploy": True,
        "enable_postprocessing": False,
        "sot_agg_transposer": None,
        "postprocessing_callables": [],
        "postprocessing_subscribed": [],
        "jinja_env": {
            "undefined": "jinja2.StrictUndefined",
            "trim_blocks": True,
            "lstrip_blocks": False,
        },
        # "default_deploy_status": "Not Approved",
        # "get_custom_compliance": "my.custom_compliance.func"
    },
}

CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://localhost:8000"]
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SAMESITE = None

#
# Development Environment for SSO
# Configure `invoke.yml` based on example for SSO development environment
#

# OIDC Dev ENV
if is_truthy(os.getenv("ENABLE_OIDC", "False")):
    import requests

    AUTHENTICATION_BACKENDS = (
        "social_core.backends.keycloak.KeycloakOAuth2",
        "nautobot.core.authentication.ObjectPermissionBackend",
    )
    SOCIAL_AUTH_KEYCLOAK_KEY = "nautobot"
    SOCIAL_AUTH_KEYCLOAK_SECRET = "7b1c3527-8702-4742-af69-2b74ee5742e8"
    SOCIAL_AUTH_KEYCLOAK_PUBLIC_KEY = requests.get("http://keycloak:8087/realms/nautobot/", timeout=15).json()[
        "public_key"
    ]
    SOCIAL_AUTH_KEYCLOAK_AUTHORIZATION_URL = "http://localhost:8087/realms/nautobot/protocol/openid-connect/auth"
    SOCIAL_AUTH_KEYCLOAK_ACCESS_TOKEN_URL = "http://keycloak:8087/realms/nautobot/protocol/openid-connect/token"
    SOCIAL_AUTH_KEYCLOAK_VERIFY_SSL = False

METRICS_ENABLED = True

CELERY_WORKER_PROMETHEUS_PORTS = [8080]
