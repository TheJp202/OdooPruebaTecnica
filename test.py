import pkg_resources
print("pkg_resources cargado OK")
print("Versión de setuptools: ",
      pkg_resources.get_distribution("setuptools").version)