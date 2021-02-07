from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # Override the ready module and import signals module
    def ready(self):
        import checkout.signals
