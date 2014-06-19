__author__ = 'yiqing'

import pkg_my.pkg_b


if __name__ == '__main__':
    # pass
    print('now we will import a module in the nested dir ')
    import pkg_my.pkg_b.mod

    print('reload the package pkg_my')
    from importlib import reload
    reload(pkg_my)
    reload(pkg_my.pkg_b)
