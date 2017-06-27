from willblog.settings.bases import *

HAYSTACK_CONNECTIONS = {

    'default': {
        'ENGINE': 'willblog.libs.index.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(BASE_DIR), 'whoosh_index'),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'index.signals.RealtimeSignalProcessor'
