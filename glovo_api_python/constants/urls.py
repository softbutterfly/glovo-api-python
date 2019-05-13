from .stages import Stage


class URL:
    PREFIX = {
        Stage.PRODUCTION: 'api',
        Stage.TEST: 'stageapi',
    }
    BASE_FORMAT = "https://{prefix}.glovoapp.com"

    WORKING_AREA = "/b2b/working-areas"
    ORDER = "/b2b/orders"

    INVOICE = "/invoices"
    PAYMENTS = "/payments"
    REFUNDS = "/refunds"
    CARD = "/cards"
    CUSTOMER = "/customers"
    TRANSFER = "/transfers"
    VIRTUAL_ACCOUNT = "/virtual_accounts"
    SUBSCRIPTION = "/subscriptions"
    ADDON = "/addons"
    PLAN = "/plans"
    SETTLEMENT = "/settlements"
