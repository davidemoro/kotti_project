def kotti_configure(settings):
    settings['kotti.asset_overrides'] += ' kotti_project:kotti-overrides/'


def includeme(config):
    config.add_static_view('docs',
                           'kotti_project:docs/html',
                           permission='admin')
