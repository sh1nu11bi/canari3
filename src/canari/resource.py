from imghdr import what
from utils.stack import calling_package
from pkg_resources import resource_filename, resource_listdir, resource_isdir

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2015, Canari Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'

__all__ = [
    'external_resource',
    'image_resource',
    'icon_resource',
    'image_resources',
    'global_config'
]


def external_resource(name, package=None):
    """
    Returns the absolute path to the external resource requested. If a package is not explicitly specified then the
    calling package name is used.

    :param name: path relative to package path of the external resource.
    :param package: package name in dotted format.
    :return: the absolute path to the external resource.
    """
    if not package:
        package = '%s.resources.external' % calling_package()
    return resource_filename(package, name)


def image_resource(name, package=None):
    """
    Returns the absolute path to an image. If a package is not explicitly specified then the calling package name is
    used.

    :param name: path relative to package path of the image resource.
    :param package: package name in dotted format.
    :return: the absolute path to the image resource.
    """
    if not package:
        package = '%s.resources.images' % calling_package()
    return resource_filename(package, name)


def icon_resource(name, package=None):
    """
    Returns the absolute URI path to an image. If a package is not explicitly specified then the calling package name is
    used.

    :param name: path relative to package path of the image resource.
    :param package: package name in dotted format.
    :return: the file URI path to the image resource (i.e. file:///foo/bar/image.png).
    """
    if not package:
        package = '%s.resources.images' % calling_package()
    name = resource_filename(package, name)
    if not name.startswith('/'):
        return 'file:///%s' % name
    return 'file://%s' % name


def image_resources(package=None, directory='resources'):
    """
    Returns all images under the directory relative to a package path. If no directory or package is specified then the
    resources module of the calling package will be used. Images are recursively discovered.

    :param package: package name in dotted format.
    :param directory: path relative to package path of the resources directory.
    :return: a list of images under the specified resources path.
    """
    if not package:
        package = calling_package()
    package_dir = '.'.join([package, directory])
    images = []
    for i in resource_listdir(package, directory):
        fname = resource_filename(package_dir, i)
        if resource_isdir(package_dir, i):
            images.extend(image_resources(package_dir, i))
        elif what(fname):
            images.append(fname)
    return images


# etc
global_config = resource_filename('canari.resources.etc', 'canari.conf')