from willblog.settings.dev import BASE_DIR as dev_dir
from willblog.settings.prod import BASE_DIR as prod_dir


def dir():
    print('Develop:\n{}\n'.format(dev_dir))
    print('Product:\n{}\n'.format(dev_dir))


if __name__ == '__main__':
    dir()
